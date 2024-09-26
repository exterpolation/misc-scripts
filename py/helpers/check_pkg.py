import subprocess
import sys
import importlib.util


def is_package_installed(package_name):
    """Check if a package is installed."""
    package_spec = importlib.util.find_spec(package_name)
    return package_spec is not None


def install_package(package_name):
    """Install a package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")
        install_pip = input("This is most likely caused by pip not being correctly installed, would you like to "
                            "install pip? (y/n): ").lower().strip()
        if install_pip == "n":
            sys.exit(1)
        elif install_pip == "y":
            pass
        # todo


def main():
    package_name = "colorama"

    if is_package_installed(package_name):
        print(f"'{package_name}' is already installed.")
    else:
        print(f"'{package_name}' not found. Installing...")
        install_package(package_name)
        print(f"'{package_name}' has been installed.")


if __name__ == "__main__":
    main()
