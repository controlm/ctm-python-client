from aapi.utils.converter.shared_converter import converter
from aapi.utils.converter.discovery import discover_attrs_classes
from aapi.utils.converter.registry import register_structure_hooks
from aapi.utils.converter.job_type_registry import build_job_type_map
import sys

# Shared job type map initialized after converter setup
JOB_TYPE_MAP = None

def initialize_converter():
    """
    Initializes the shared converter by:
    1. Discovering all @attrs classes in the aapi module.
    2. Registering structure hooks for each class.
    3. Building a job type mapping for runtime type resolution.
    """
    global JOB_TYPE_MAP

    # Discover all classes decorated with @attr.s within the aapi module
    all_attrs_classes = discover_attrs_classes(sys.modules["aapi"])

    # Register structure hooks for each discovered @attrs class
    register_structure_hooks(converter, all_attrs_classes)

    # Build the mapping from _type to Job subclass for dynamic resolution
    JOB_TYPE_MAP = build_job_type_map()