import importlib
import pkg_resources

# Load plugins
for entry_point in pkg_resources.iter_entry_points("zmath_plugins"):
    try:
        entry_point.load()
    except ImportError as e:
        print(f"Could not load plugin {entry_point.name}: {e}")


from .add import add
from .subtract import substract
