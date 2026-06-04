from tkinter import *
from tkinter import ttk
from modules.config_handler import fetch_from_config

BG      = "#0f172a"
CARD    = "#1e293b"
PRIMARY = "#3b82f6"
PRI_ACT = "#2563eb"
TEXT    = "#f1f5f9"
MUTED   = "#94a3b8"
BORDER  = "#334155"
HDR_BG  = "#020617"
FONT    = "Montserrat"

root = Tk()
root.title("CAIE Downloader")
root.resizable(False, False)
root.configure(bg=BG)

style = ttk.Style()
style.theme_use("clam")

style.configure("Card.TLabelframe",
    background=CARD, bordercolor=BORDER, relief="solid", borderwidth=1)
style.configure("Card.TLabelframe.Label",
    background=CARD, foreground=MUTED, font=(FONT, 9, "bold"))

style.configure("Primary.TButton",
    background=PRIMARY, foreground="white",
    font=(FONT, 11, "bold"), borderwidth=0, padding=(20, 10))
style.map("Primary.TButton",
    background=[("active", PRI_ACT), ("disabled", "#94a3b8")],
    foreground=[("disabled", "white")])

style.configure("Ghost.TButton",
    background=CARD, foreground=MUTED,
    font=(FONT, 11), borderwidth=1, relief="solid", padding=(16, 10))
style.map("Ghost.TButton", background=[("active", BG)])

style.configure("Blue.Horizontal.TProgressbar",
    troughcolor=BORDER, background=PRIMARY, borderwidth=0, thickness=6)

subject_var       = StringVar()
paper_var         = StringVar()
start_year        = StringVar()
end_year          = StringVar()
paper_type        = StringVar(value="Question Papers")
feb_march         = StringVar(value="N")
may_june          = StringVar(value="N")
oct_nov           = StringVar(value="N")
remove_blank      = StringVar()
remove_additional = StringVar()
remove_formula    = StringVar()
progress_var      = DoubleVar()


def refresh_config_data():
    remove_blank.set(fetch_from_config("remove_blank"))
    remove_additional.set(fetch_from_config("remove_additional"))
    remove_formula.set(fetch_from_config("remove_formula"))


refresh_config_data()


def _section(parent, title):
    lf = ttk.LabelFrame(parent, text=f"  {title}  ",
                         style="Card.TLabelframe", padding=(16, 12))
    lf.pack(fill=X, pady=(0, 10))
    return lf


def _field(parent, label, textvariable):
    Label(parent, text=label, font=(FONT, 9), bg=CARD,
          fg=MUTED, anchor="w").pack(fill=X)
    e = Entry(parent, textvariable=textvariable, font=(FONT, 12),
              bg=BG, fg=TEXT, relief="flat", bd=0,
              highlightthickness=1, highlightbackground=BORDER,
              highlightcolor=PRIMARY, insertbackground=TEXT)
    e.pack(fill=X, ipady=7, pady=(2, 10))
    return e


def _check(parent, text, variable):
    return Checkbutton(parent, text=text, variable=variable,
                       onvalue="Y", offvalue="N", font=(FONT, 11),
                       bg=CARD, fg=TEXT, activebackground=CARD,
                       selectcolor=CARD, cursor="hand2")


def _radio(parent, text, variable, value):
    return Radiobutton(parent, text=text, variable=variable, value=value,
                       font=(FONT, 11), bg=CARD, fg=TEXT,
                       activebackground=CARD, selectcolor=CARD,
                       cursor="hand2")


header = Frame(root, bg=HDR_BG)
header.pack(fill=X)
Label(header, text="CAIE Downloader",
      font=(FONT, 22, "bold"), bg=HDR_BG, fg="white").pack(pady=(22, 3))
Label(header, text="Past paper compiler  ·  @itsgeagle",
      font=(FONT, 10), bg=HDR_BG, fg="#94a3b8").pack(pady=(0, 22))

# bottom packed before main so tkinter reserves its space correctly
bottom = Frame(root, bg=CARD, padx=20, pady=16)
bottom.pack(fill=X, side=BOTTOM)

Frame(bottom, bg=BORDER, height=1).pack(fill=X, pady=(0, 14))

status_label = Label(bottom, text="", font=(FONT, 9), bg=CARD, fg=MUTED, anchor="e")
status_label.pack(fill=X)

progress_bar = ttk.Progressbar(bottom, variable=progress_var,
                                mode="determinate",
                                style="Blue.Horizontal.TProgressbar")
progress_bar.pack(fill=X, pady=(4, 14))

btn_row = Frame(bottom, bg=CARD)
btn_row.pack(fill=X)

config_btn = ttk.Button(btn_row, text="⚙  Config", style="Ghost.TButton")
config_btn.pack(side=LEFT)

sub_btn = ttk.Button(btn_row, text="Download  ▶", style="Primary.TButton")
sub_btn.pack(side=RIGHT)

main_frame = Frame(root, bg=BG, padx=20)
main_frame.pack(fill=BOTH, expand=True, pady=16)

sec = _section(main_frame, "SUBJECT")
_field(sec, "Subject code  (e.g. 9701)", subject_var)
_field(sec, "Paper code(s)  (e.g. 1  or  1, 2, 4)", paper_var)

sec = _section(main_frame, "YEAR RANGE")
yr_row = Frame(sec, bg=CARD)
yr_row.pack(fill=X)
yr_left = Frame(yr_row, bg=CARD)
yr_left.pack(side=LEFT, fill=X, expand=True, padx=(0, 8))
_field(yr_left, "From", start_year)
yr_right = Frame(yr_row, bg=CARD)
yr_right.pack(side=LEFT, fill=X, expand=True, padx=(8, 0))
_field(yr_right, "To", end_year)

sec = _section(main_frame, "PAPER TYPE")
pt_row = Frame(sec, bg=CARD)
pt_row.pack(fill=X)
_radio(pt_row, "Question Papers", paper_type, "Question Papers").pack(side=LEFT, padx=(0, 24))
_radio(pt_row, "Mark Schemes",    paper_type, "Mark Schemes").pack(side=LEFT)

sec = _section(main_frame, "EXAM SERIES")
ser_row = Frame(sec, bg=CARD)
ser_row.pack(fill=X)
_check(ser_row, "Feb / March", feb_march).pack(side=LEFT, padx=(0, 16))
_check(ser_row, "May / June",  may_june).pack(side=LEFT, padx=(0, 16))
_check(ser_row, "Oct / Nov",   oct_nov).pack(side=LEFT)

sec = _section(main_frame, "OUTPUT OPTIONS")
_check(sec, "Remove blank pages",      remove_blank).pack(anchor="w", pady=2)
_check(sec, "Remove additional pages", remove_additional).pack(anchor="w", pady=2)
_check(sec, "Remove formula pages",    remove_formula).pack(anchor="w", pady=2)
