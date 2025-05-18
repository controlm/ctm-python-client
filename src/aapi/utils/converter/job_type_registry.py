import inspect
import sys
from aapi import Job

# def build_job_type_map():
#     """
#     Builds a mapping from _type string to each Job subclass in the aapi module.
#     This enables dynamic resolution of job types based on serialized data.
#     """
#     job_map = {}

#     # Inspect all classes defined in the aapi module
#     for name, cls in inspect.getmembers(sys.modules['aapi'], inspect.isclass):
#         # Only consider subclasses of Job, excluding the base Job class itself
#         if issubclass(cls, Job) and cls is not Job:
#             job_type_field = getattr(cls, "_type", None)

#             if isinstance(job_type_field, str):
#                 # Use the declared _type string
#                 job_map[job_type_field] = cls
#                 print(f"Registering job type: {job_type_field} -> {cls.__qualname__}")
#             else:
#                 # Attempt to instantiate the class and extract _type dynamically
#                 try:
#                     instance = cls(object_name="dummy")
#                     job_type = getattr(instance, "_type", None)
#                     if isinstance(job_type, str):
#                         job_map[job_type] = cls
#                         print(f"Registering job type (via instance): {job_type} -> {cls.__qualname__}")
#                 except Exception:
#                     pass  # Skip classes that cannot be instantiated

#     return job_map
def build_job_type_map():
    import types
    job_map = {}

    for module in list(sys.modules.values()):
        if not isinstance(module, types.ModuleType):
            continue
        if not getattr(module, "__name__", "").startswith("aapi"):
            continue

        for name, cls in inspect.getmembers(module, inspect.isclass):
            if not issubclass(cls, Job) or cls is Job:
                continue

            print(f"Inspecting Job subclass: {cls.__qualname__} from module {cls.__module__}")

            job_type_field = getattr(cls, "_type", None)
            if isinstance(job_type_field, str):
                print(f"Found static _type: {job_type_field} on {cls.__qualname__}")
                job_map[job_type_field] = cls
                print(f"Registering job type: {job_type_field} -> {cls.__qualname__}")
            else:
                print(f"No static _type for {cls.__qualname__}, trying to instantiate...")

                try:
                    instance = cls(object_name="dummy")
                    job_type = getattr(instance, "_type", None)

                    if isinstance(job_type, str):
                        print(f"Found instance _type: {job_type} from instance of {cls.__qualname__}")
                        job_map[job_type] = cls
                        print(f"Registering job type (via instance): {job_type} -> {cls.__qualname__}")
                    else:
                        print(f"No _type found on instance of {cls.__qualname__}")
                except Exception as e:
                    print(f"Failed to instantiate {cls.__qualname__}: {e}")

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