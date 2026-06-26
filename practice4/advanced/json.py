# This file contains an interactive JSON parser example.
import importlib.util
import sys
import sysconfig
from pathlib import Path


# This function loads the standard-library json module from its path.
def load_json_module():
    stdlib_json_dir = Path(sysconfig.get_path("stdlib")) / "json"
    spec = importlib.util.spec_from_file_location(
        "json",
        stdlib_json_dir / "__init__.py",
        submodule_search_locations=[str(stdlib_json_dir)],
    )
    stdlib_json = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = stdlib_json
    spec.loader.exec_module(stdlib_json)
    return stdlib_json


# This function reads JSON data from a file and returns it as a Python dictionary.
def load_data(file_path):
    stdlib_json = load_json_module()
    with open(file_path, "r", encoding="utf-8") as f:
        return stdlib_json.load(f)


# This function prints the interface-status report in a formatted table.
def print_interface_status(data):
    print("Interface Status")
    print("=" * 80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
    print("-" * 50, "-" * 20, "-" * 8, "-" * 6)

    for item in data.get("interfaceStatus", []):
        print(f"{item['name']:<50} {item['description']:<20} {item['speed']:<8} {item['mtu']:<6}")
    # Example output includes the three interface rows from sample-data.json.


# This function runs the interactive menu for the JSON example.
def main():
    while True:
        print("\nJSON Menu")
        print("1. Show interface status report")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            data = load_data(Path(__file__).with_name("sample-data.json"))
            print_interface_status(data)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
