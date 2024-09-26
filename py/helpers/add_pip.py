import os
import subprocess

scripts_path = "to_change"


def add_to_path(new_path):
    """Add the provided path to the system PATH environment variable."""
    current_path = os.environ.get('PATH', '')
    if new_path not in current_path:
        command = f'setx PATH "{current_path};{new_path}"'
        subprocess.run(command, shell=True)
        print(f"Added '{new_path}' to the system PATH.")
    else:
        print(f"'{new_path}' is already in the system PATH.")


def main():
    # Find the Scripts directory where pip is located
    global scripts_path

    if os.path.exists(scripts_path):
        print(f"Found Scripts directory at: {scripts_path}")
        add_to_path(scripts_path)
    else:
        print("Error: Scripts directory not found.")


if __name__ == "__main__":
    main()
