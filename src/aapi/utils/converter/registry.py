import attr
from cattrs import Converter
from aapi.utils.converter.job_type_registry import resolve_type

def make_structure_hook(cls, converter: Converter):
    """
    Generates a structure hook for the given @attrs class.
    This hook transforms raw JSON-like dicts into properly typed instances,
    supporting dynamic type resolution for nested fields.
    """
    def hook(data, _):
        from aapi.utils.converter import JOB_TYPE_MAP

        # Create field mapping from JSON keys to attribute names
        field_map = {
            f.metadata.get("_aapi_repr_", f.metadata.get("_aapi_alias_", f.name)): f.name
            for f in attr.fields(cls)
        }

        init_fields = {f.name for f in attr.fields(cls) if f.init}
        type_map_ = {f.name: f.type for f in attr.fields(cls)}

        kwargs = {}

        # Iterate over the input data, mapping it to constructor kwargs
        for json_key, field_name in field_map.items():
            if json_key not in data or field_name not in init_fields:
                continue

            value = data[json_key]
            field_type = type_map_.get(field_name)

            try:
                # Handle nested object (dict) deserialization
                if isinstance(value, dict) and attr.has(field_type):
                    try:
                        resolved_cls = resolve_type(value, JOB_TYPE_MAP, label="Type")
                    except Exception:
                        resolved_cls = field_type
                    kwargs[field_name] = converter.structure(value, resolved_cls)

                # Handle lists of nested objects
                elif isinstance(value, list) and hasattr(field_type, '__args__'):
                    item_type = field_type.__args__[0]
                    if attr.has(item_type):
                        structured_list = []
                        for item in value:
                            try:
                                resolved_cls = resolve_type(item, JOB_TYPE_MAP, label="Type")
                            except Exception:
                                resolved_cls = item_type
                            structured_list.append(converter.structure(item, resolved_cls))
                        kwargs[field_name] = structured_list
                    else:
                        kwargs[field_name] = value  # fallback for plain lists

                else:
                    kwargs[field_name] = value  # assign simple fields as-is

            except Exception:
                kwargs[field_name] = value  # fallback on failure to deserialize

        return cls(**kwargs)

    return hook

def register_structure_hooks(converter: Converter, classes: list):
    """
    Registers structure hooks for a list of @attrs classes with the given converter.
    These hooks allow for dynamic construction of instances from raw dict data.
    """
    for cls in classes:
        converter.register_structure_hook(cls, make_structure_hook(cls, converter))