import tkinter as tk
from modules.gui import root
import webbrowser


# Function to create a popup window displaying the latest version of the software
def version_popup(latest):
    version = tk.Toplevel(root)
    version.title("New Version Available")

    tk.Label(
        version,
        text=f'A new version of CAIE Downloader ({latest}) is available! To download the latest version, click the '
             f'button below to visit the releases page!',
        font=("Helvetica", 16)
    ).pack(padx=10)

    release_button = tk.Button(
        version,
        text="Open Releases Page",
        command=lambda: webbrowser.open_new_tab("https://github.com/itsgeagle/caiedownloader/releases")
    )
    release_button.pack(pady=10)

    cancel_button = tk.Button(
        version,
        text="Cancel",
        command=version.destroy
    )
    cancel_button.pack(pady=10)

    version.wait_visibility()
    version.grab_set()
    version.focus_set()
    version.wait_window()


def error_popup(errorMessage):
    error_window = tk.Toplevel(root)
    error_window.title("Error")

    tk.Label(
        error_window,
        text=errorMessage,
        font=("Montserrat", 16)
    ).pack()

    cancel_button = tk.Button(
        error_window,
        text="Cancel",
        command=error_window.destroy
    )
    cancel_button.pack(pady=10)

    error_window.wait_visibility()
    error_window.grab_set()
    error_window.focus_set()
    error_window.wait_window()
