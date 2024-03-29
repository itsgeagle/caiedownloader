# Contains helper methods for creating popups
import os
import tkinter as tk
import webbrowser
from tkinter import filedialog

from modules.gui import root


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


def message_popup(message, title):
    error_window = tk.Toplevel(root)
    error_window.title(title)

    tk.Label(
        error_window,
        text=message,
        font=("Montserrat", 16)
    ).pack()

    cancel_button = tk.Button(
        error_window,
        text="Close",
        command=error_window.destroy
    )
    cancel_button.pack(pady=10)

    error_window.wait_visibility()
    error_window.grab_set()
    error_window.focus_set()
    error_window.wait_window()


# Function to allow user to browse for download path
def browse_path(file_name):
    # Create Toplevel window for file dialog
    file_dialog = tk.Toplevel()
    file_dialog.withdraw()

    # Browse file path from save dialog
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    file_path = filedialog.asksaveasfilename(initialdir=downloads_folder, initialfile=file_name, defaultextension=".pdf")
    file_dialog.destroy()

    # Return file path
    return file_path
