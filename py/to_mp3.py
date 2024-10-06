import os
import subprocess
import sys
import argparse
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from moviepy.editor import VideoFileClip
from pathlib import Path
from colorama import Fore, init
from time import sleep

# Initialize colorama
init(autoreset=True)

logo = (fr"""{Fore.WHITE}
                     __                           ________                    
                   _/  |_  ____       _____ ______\_____  \     ______ ___.__.
                   \   __\/  _ \     /     \\____ \ _(__  <     \____ <   |  |
                    |  | (  <_> )   |  Y Y  \  |_> >       \    |  |_> >___  |
                    |__|  \____/____|__|_|  /   __/______  / /\ |   __// ____|
                              /_____/     \/|__|         \/  \/ |__|   \/     

{Fore.RESET}""")


def setup_console(length: int = 0, width: int = 0) -> None:
    if os.name == 'nt':  # For Windows
        os.system("cls")
    else:  # For Linux and other Unix-like systems
        os.system("clear")
    os.system(f"mode con: cols={length} lines={width}")  # Set the console size


# Custom ArgumentParser to format error messages
class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        # Print error message in red
        sys.stderr.write(f"{Fore.RED}error: {message}{Fore.RESET}\n")
        self.print_help()  # Print the help message
        sys.exit(1)  # Exit with error


# Function to convert video to mp3
def convert_video_to_mp3(input_video_path, output_mp3_path):
    try:
        video = VideoFileClip(input_video_path)
        video.audio.write_audiofile(output_mp3_path)
        video.close()
        print(f"{Fore.GREEN}Conversion complete: {Fore.WHITE}{output_mp3_path}")
        sleep(1)

        # Open the converted MP3 file using VLC
        open_with_vlc(output_mp3_path)

    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Fore.RESET}")


# Function to open the converted MP3 file using VLC
def open_with_vlc(file_path):
    vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"  # Change this to your VLC path
    try:
        # Check if VLC is installed
        # subprocess.check_call([vlc_path, "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # TODO: The line above makes a window pop up and the user has to press enter to close it, needs a fix

        # Construct the VLC command with the full file path
        vlc_command = [vlc_path, os.path.abspath(file_path)]

        # Create startupinfo to suppress console window
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW  # Suppress the window

        # Use subprocess.Popen with startupinfo to suppress the console window
        subprocess.Popen(vlc_command, startupinfo=startupinfo, shell=True)
    except FileNotFoundError:
        print(f"{Fore.RED}VLC is not found at {vlc_path}. Please check the path.{Fore.RESET}")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}VLC is not installed. Please install VLC before opening the file.{Fore.RESET}")


# Function to get default download directory
def get_default_download_dir():
    if sys.platform == 'nt':
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    else:
        return os.path.join(Path.home(), 'Downloads')


# Tkinter file chooser for video
def choose_file():
    root = Tk()

    # Set window title and icon
    root.title("Select a Video File")

    root.withdraw()  # Hide the root window initially
    file_path = askopenfilename(filetypes=[("Video files", "*.mp4 *.mkv *.avi *.mov *.flv")])
    root.destroy()  # Close the Tkinter window after the file selection
    return file_path


# Function to print help message
def print_help():
    print(f"{Fore.YELLOW}Usage: py video_to_mp3.py <flag> <argument>\n{Fore.RESET}")
    print(f"{Fore.CYAN}Flags:")
    print(f"{Fore.WHITE} └── {Fore.CYAN}-d    Specify the video file directory")
    print(f"{Fore.WHITE} │   └── {Fore.CYAN}-dp   Use a file dialog to choose the video file")
    print(f"{Fore.WHITE} └── {Fore.CYAN}-o    Specify the output directory for the MP3 file (default: Downloads)")
    print(f"{Fore.WHITE} └── {Fore.CYAN}-v    Open the converted MP3 file using VLC (requires VLC installation)")
    print(f"{Fore.WHITE} └── {Fore.CYAN}-h    Print this help page")


# Main function to handle arguments and convert video
def main():
    setup_console(length=100, width=30)
    print(logo)

    # Default to -h if no arguments are provided
    if len(sys.argv) == 1:
        sys.argv.append("-h")

    # Argument parsing with custom -h argument
    parser = CustomArgumentParser(description="Convert video to MP3 format", add_help=False)
    parser.add_argument('-d', '--directory', help="Specify the video file directory")
    parser.add_argument('-dp', '--dialog', action='store_true', help="Use a file dialog to choose the video file")
    parser.add_argument('-o', '--output', help="Specify the output directory for the MP3 file")
    parser.add_argument('-v', '--view', action='store_true', help="Open the converted MP3 file using VLC")
    parser.add_argument('-h', '--help', action='store_true', help="Print the help message")

    args = parser.parse_args()

    # Handle custom help flag
    if args.help:
        print_help()
        return 0

    # Pattern matching with match-case
    match sys.argv[1] if len(sys.argv) > 1 else None:
        case "-d":
            input_video = args.directory
            if not input_video or not os.path.isfile(input_video):
                parser.error("Invalid or missing video file path.")  # This will now use the custom error method
                return 1
        case "-dp":
            input_video = choose_file()
            if not input_video:
                print(f"{Fore.RED}No file selected.{Fore.RESET}")
                return 1
        case _:
            parser.error("Invalid flag provided.")  # This will now use the custom error method
            return 1

    # Determine output path for MP3
    output_dir = args.output if args.output else get_default_download_dir()
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_mp3 = os.path.join(output_dir, f"{Path(input_video).stem}.mp3")

    # Convert video to MP3
    convert_video_to_mp3(input_video, output_mp3)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        pass
