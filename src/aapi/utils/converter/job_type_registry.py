import inspect
import sys
from aapi import Job

def build_job_type_map():
    import types

    def extract_type_from_field(cls):
        """
        Try to extract the default value of the '_type' field from the attrs definition,
        without needing to instantiate the class.
        """
        import attr
        for field in attr.fields(cls):
            if field.name == "_type":
                return field.default
        return None

    job_map = {}

    for module in list(sys.modules.values()):
        if not isinstance(module, types.ModuleType):
            continue
        if not getattr(module, "__name__", "").startswith("aapi"):
            continue

        for name, cls in inspect.getmembers(module, inspect.isclass):
            if not issubclass(cls, Job) or cls is Job:
                continue

            # --- NEW: Try static extraction via attr field default ---
            job_type_field = extract_type_from_field(cls)
            if isinstance(job_type_field, str):
                job_map[job_type_field] = cls
                continue  # Don't fall back to instantiation if already resolved

            # --- OLD fallback: Try to instantiate ---
            try:
                instance = cls(object_name="dummy")
                job_type = getattr(instance, "_type", None)

                if isinstance(job_type, str):
                    job_map[job_type] = cls
                else:
                    pass
            except Exception as e:
                pass

    return job_map



def resolve_type(obj: dict, type_map: dict, label: str = "type"):
    """
    Resolves the appropriate subclass using the provided type hint ("Type" or "_type")
    from the input dictionary. Raises if no match is found in the type_map.
    """
    type_hint = obj.get("Type") or obj.get("_type")

    cls = type_map.get(type_hint)
    if cls is None:
        raise ValueError(f"Unknown {label}: {type_hint}")

    return cls