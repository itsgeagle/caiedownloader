import tkinter as tk
from modules.GUI import root
import webbrowser


# Function to create a popup window displaying the latest version of the software
def versionPopup(latest):
    print()
    version = tk.Toplevel(root)
    version.title("New Version Available")

    version.grab_set()
    version.focus_set()

    tk.Label(
        version,
        text=f'A new version of CAIE Downloader ({latest}) is available! To download the latest version, click the '
             f'button below to visit the releases page!',
        font=("Helvetica", 16)
    ).pack()

    releaseButton = tk.Button(
        version,
        text="Open Releases Page",
        command=lambda: webbrowser.open_new_tab("https://github.com/itsgeagle/caiedownloader/releases")
    )
    releaseButton.pack(pady=10)

    cancelButton = tk.Button(
        version,
        text="Cancel",
        command=version.destroy
    )
    cancelButton.pack(pady=10)

    version.mainloop()
