import yaml
from pathlib import Path
import sys

def load_yaml_plan(path_str):
    """Loads and safely parses a YAML file."""
    plan_path = Path(path_str)
    if not plan_path.exists():
        print(f"Plan not found: {plan_path}", file=sys.stderr)
        return None
    try:
        with open(plan_path, "r") as f:
            return yaml.safe_load(f) or {}
    except Exception as e:
        print(f"Error loading YAML file {path_str}: {e}", file=sys.stderr)
        return None