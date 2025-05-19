import importlib
import inspect
import pkgutil
import sys
from types import ModuleType
import attrs

def is_attrs_class(cls):
    """
    Check if a class is an `@attrs` class defined in the 'aapi' package.
    """
    return (
        inspect.isclass(cls)              # Is it a class?
        and attrs.has(cls)                # Is it an `@attrs` class?
        and cls.__module__.startswith("aapi")  # Belongs to the 'aapi' package?
    )

def import_all_submodules(package: ModuleType):
    """
    Dynamically import all submodules in the given package.
    This ensures all classes (even deeply nested) are loaded into sys.modules.
    """
    for _, module_name, _ in pkgutil.walk_packages(package.__path__, package.__name__ + "."):
        try:
            importlib.import_module(module_name)
        except Exception:
            pass  # Skip modules that fail to import (optional: log if needed)

def collect_attrs_classes(cls, seen):
    """
    Recursively collect all nested `@attrs` classes starting from a given class.
    Args:
        cls: A class to inspect.
        seen: A set to store already-discovered classes and avoid duplicates.
    This walks inside inner classes (e.g., Job.RerunLimit) to register everything.
    """
    if cls in seen or not is_attrs_class(cls):
        return
    seen.add(cls)

    # Inspect all members of the class — looking for nested `@attrs` classes
    for name, member in inspect.getmembers(cls):
        if inspect.isclass(member) and attrs.has(member):
            collect_attrs_classes(member, seen)

def discover_attrs_classes(package: ModuleType):
    """
    Discover all `@attrs` classes (including nested ones) in a package.
    Args:
        package: The root module (e.g., `import aapi; discover_attrs_classes(aapi)`)
    Returns:
        A list of all discovered `@attrs` classes.
    """
    import_all_submodules(package)  # Make sure all submodules are imported
    seen = set()  # Use a set to avoid duplicates

    for module in list(sys.modules.values()):
        if not isinstance(module, ModuleType):
            continue
        if not getattr(module, "__name__", "").startswith("aapi"):
            continue

        # For every class in this module, collect it and its nested @attrs classes
        for _, obj in inspect.getmembers(module, inspect.isclass):
            collect_attrs_classes(obj, seen)

    return list(seen)