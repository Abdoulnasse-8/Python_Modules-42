import sys
import os
import site
from typing import List


def is_in_venv() -> bool:
    return (
        hasattr(sys, "real_prefix")
        or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)
    )


def get_venv_name() -> str:
    venv_path: str = os.environ.get("VIRTUAL_ENV", "")
    if venv_path:
        return os.path.basename(venv_path)
    return "Unknown"


def get_package_path() -> str:
    try:
        packages: List[str] = site.getsitepackages()
        if packages:
            return packages[0]
    except Exception:
        pass
    return site.getusersitepackages()


def show_inside_venv() -> None:
    venv_path: str = os.environ.get("VIRTUAL_ENV", "")
    venv_name: str = get_venv_name()

    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print("Package installation path:")
    print(get_package_path())


def show_outside_venv() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate  # On Windows")
    print("Then run this program again.")


def main() -> None:
    if is_in_venv():
        show_inside_venv()
    else:
        show_outside_venv()


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"ERROR: {err}")
