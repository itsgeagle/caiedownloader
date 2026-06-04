# Contains helper methods for creating popups
import tkinter as tk
from tkinter import ttk, filedialog
import webbrowser

from modules.config_handler import fetch_from_config, save_to_config
from modules.gui import root, refresh_config_data, CARD, BG, PRIMARY, PRI_ACT, TEXT, MUTED, BORDER, FONT

download_directory = fetch_from_config("download_directory")


def _make_popup(title, width=400):
    win = tk.Toplevel(root)
    win.title(title)
    win.configure(bg=CARD)
    win.resizable(False, False)
    root.update_idletasks()
    x = root.winfo_x() + (root.winfo_width() - width) // 2
    y = root.winfo_y() + root.winfo_height() // 3
    win.geometry(f"+{x}+{y}")
    win.minsize(width, 0)
    return win


def _popup_btn(parent, text, command, primary=False):
    style = "Primary.TButton" if primary else "Ghost.TButton"
    return ttk.Button(parent, text=text, command=command, style=style)


def _divider(parent):
    tk.Frame(parent, bg=BORDER, height=1).pack(fill=tk.X, pady=(0, 16))


def version_popup(latest):
    win = _make_popup("New Version Available", width=440)

    tk.Frame(win, bg=PRIMARY, height=4).pack(fill=tk.X)

    body = tk.Frame(win, bg=CARD, padx=28, pady=24)
    body.pack(fill=tk.BOTH, expand=True)

    tk.Label(body, text="Update Available",
             font=(FONT, 16, "bold"), bg=CARD, fg=TEXT).pack(anchor="w")
    tk.Label(body,
             text=f"Version {latest} is now available on GitHub.",
             font=(FONT, 11), bg=CARD, fg=MUTED,
             wraplength=380, justify="left").pack(anchor="w", pady=(6, 20))

    btn_row = tk.Frame(body, bg=CARD)
    btn_row.pack(fill=tk.X)
    _popup_btn(btn_row, "Open Releases Page",
               lambda: webbrowser.open_new_tab(
                   "https://github.com/itsgeagle/caiedownloader/releases"),
               primary=True).pack(side=tk.LEFT)
    _popup_btn(btn_row, "Dismiss", win.destroy).pack(side=tk.LEFT, padx=(10, 0))

    win.wait_visibility()
    win.grab_set()
    win.focus_set()
    win.wait_window()


def message_popup(message, title):
    is_error = title.lower() == "error"
    accent = "#dc2626" if is_error else PRIMARY

    win = _make_popup(title, width=400)
    tk.Frame(win, bg=accent, height=4).pack(fill=tk.X)

    body = tk.Frame(win, bg=CARD, padx=28, pady=24)
    body.pack(fill=tk.BOTH, expand=True)

    tk.Label(body, text=title,
             font=(FONT, 15, "bold"), bg=CARD, fg=TEXT).pack(anchor="w")
    tk.Label(body, text=message,
             font=(FONT, 11), bg=CARD, fg=MUTED,
             wraplength=344, justify="left").pack(anchor="w", pady=(6, 20))

    _popup_btn(body, "Close", win.destroy, primary=True).pack(anchor="w")

    win.wait_visibility()
    win.grab_set()
    win.focus_set()
    win.wait_window()


def browse_path(file_name):
    dlg = tk.Toplevel(root)
    dlg.withdraw()
    file_path = filedialog.asksaveasfilename(
        initialdir=download_directory,
        initialfile=file_name,
        defaultextension=".pdf"
    )
    dlg.destroy()
    return file_path


def browse_folder():
    dlg = tk.Toplevel(root)
    dlg.withdraw()
    file_path = filedialog.askdirectory(initialdir=download_directory)
    dlg.destroy()
    return file_path


def edit_download_path():
    global download_directory
    file_path = browse_folder()
    while file_path == '':
        message_popup("The directory cannot be blank!", "Error")
        file_path = browse_folder()
    download_directory = file_path
    save_to_config("download_directory", download_directory)
    message_popup(f"Default download directory set to:\n{download_directory}", "Success")


def edit_config():
    rb = tk.StringVar(value=fetch_from_config("remove_blank"))
    ra = tk.StringVar(value=fetch_from_config("remove_additional"))
    rf = tk.StringVar(value=fetch_from_config("remove_formula"))

    win = _make_popup("Preferences", width=420)
    tk.Frame(win, bg=PRIMARY, height=4).pack(fill=tk.X)

    body = tk.Frame(win, bg=CARD, padx=28, pady=24)
    body.pack(fill=tk.BOTH, expand=True)

    tk.Label(body, text="Preferences",
             font=(FONT, 16, "bold"), bg=CARD, fg=TEXT).pack(anchor="w")
    tk.Label(body, text="Default settings applied on each new session.",
             font=(FONT, 10), bg=CARD, fg=MUTED).pack(anchor="w", pady=(4, 18))

    def _pref_check(text, var):
        tk.Checkbutton(body, text=text, variable=var,
                       onvalue="Y", offvalue="N",
                       font=(FONT, 11), bg=CARD, fg=TEXT,
                       activebackground=CARD, selectcolor=CARD,
                       cursor="hand2").pack(anchor="w", pady=3)

    _pref_check("Remove blank pages by default",      rb)
    _pref_check("Remove additional pages by default", ra)
    _pref_check("Remove formula pages by default",    rf)

    tk.Frame(body, bg=BORDER, height=1).pack(fill=tk.X, pady=(18, 16))

    _popup_btn(body, "⚙  Change Default Download Folder",
               edit_download_path).pack(anchor="w")

    tk.Frame(body, bg=BORDER, height=1).pack(fill=tk.X, pady=(16, 18))

    def save():
        save_to_config("remove_blank",      rb.get())
        save_to_config("remove_additional", ra.get())
        save_to_config("remove_formula",    rf.get())
        refresh_config_data()
        win.destroy()

    btn_row = tk.Frame(body, bg=CARD)
    btn_row.pack(fill=tk.X)
    _popup_btn(btn_row, "Save", save, primary=True).pack(side=tk.LEFT)
    _popup_btn(btn_row, "Cancel", win.destroy).pack(side=tk.LEFT, padx=(10, 0))

    win.wait_visibility()
    win.grab_set()
    win.focus_set()
    win.wait_window()
