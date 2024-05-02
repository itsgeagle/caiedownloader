# Contains helper methods for creating popups
import os
import tkinter as tk
import webbrowser
from tkinter import filedialog
from modules.config_handler import fetch_from_config, save_to_config
from modules.gui import root, refresh_config_data

download_directory = fetch_from_config("download_directory")

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
    file_dialog = tk.Toplevel(root)
    file_dialog.withdraw()

    # Browse file path from save dialog
    file_path = filedialog.asksaveasfilename(initialdir=download_directory, initialfile=file_name, defaultextension=".pdf")
    file_dialog.destroy()

    # Return file path
    return file_path


# Function to allow user to browse a directory for default download
def browse_folder():
    file_dialog = tk.Toplevel(root)
    file_dialog.withdraw()
    file_path = filedialog.askdirectory(initialdir=download_directory)
    file_dialog.destroy()
    return file_path

def edit_download_path():
    global download_directory
    file_path = browse_folder()
    while file_path == '':
        message_popup("The directory cannot be blank!", "Error")
        file_path = browse_folder()
    download_directory = file_path
    save_to_config("download_directory", download_directory)
    message_popup(f"Set default download directory to {download_directory}", "Success")


def edit_config():
    remove_blank = tk.StringVar()
    remove_blank.set(fetch_from_config("remove_blank"))
    remove_additional = tk.StringVar()
    remove_additional.set(fetch_from_config("remove_additional"))
    remove_formula = tk.StringVar()
    remove_formula.set(fetch_from_config("remove_formula"))

    def save_config():
        save_to_config(item="remove_blank", value=remove_blank.get())
        save_to_config(item="remove_additional", value=remove_additional.get())
        save_to_config(item="remove_formula", value=remove_formula.get())
        refresh_config_data()
        config_editor.destroy()

    config_editor = tk.Toplevel(root)

    tk.Label(
        config_editor,
        text="Edit your default configuration here. These are the values which load in when you first run the program.",
        font=("Montserrat", 16)
    ).pack()

    tk.Checkbutton(config_editor, text='Remove Blank Pages', variable=remove_blank, onvalue='Y', offvalue='N').pack(pady=10)
    tk.Checkbutton(config_editor, text='Remove Additional Pages', variable=remove_additional, onvalue='Y', offvalue='N').pack(pady=10)
    tk.Checkbutton(config_editor, text='Remove Formula Pages', variable=remove_formula, onvalue='Y', offvalue='N').pack(pady=10)

    tk.Button(
        config_editor,
        text='Edit Default Download Path',
        command=edit_download_path
    ).pack()

    submit = tk.Button(
        config_editor,
        text="Save",
        command=save_config
    )
    submit.pack(pady=10)

    cancel_button = tk.Button(
        config_editor,
        text="Close",
        command=config_editor.destroy
    )
    cancel_button.pack(pady=10)

