import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
from core.operations import Lockbox


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lockbox — Encrypt Files & Folders")
        self.geometry("680x300")

        self.path_var = tk.StringVar()
        self.pw_var = tk.StringVar()
        self.pw2_var = tk.StringVar()
        self.delete_var = tk.BooleanVar(value=False)

        self._build_ui()

    def _build_ui(self):
        pad = 10
        frm = ttk.Frame(self, padding=pad)
        frm.pack(fill=tk.BOTH, expand=True)

        # Path
        row1 = ttk.Frame(frm)
        row1.pack(fill=tk.X, pady=(0, pad))

        ttk.Label(row1, text="Target:").pack(side=tk.LEFT)
        ttk.Entry(row1, textvariable=self.path_var).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=pad)
        ttk.Button(row1, text="Browse", command=self._browse).pack(side=tk.LEFT)

        # Password
        row2 = ttk.Frame(frm)
        row2.pack(fill=tk.X, pady=(0, pad))

        ttk.Label(row2, text="Password:").pack(side=tk.LEFT)
        ttk.Entry(row2, textvariable=self.pw_var, show="*").pack(side=tk.LEFT, fill=tk.X, expand=True, padx=pad)

        ttk.Label(row2, text="Confirm:").pack(side=tk.LEFT)
        ttk.Entry(row2, textvariable=self.pw2_var, show="*").pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Checkbox
        ttk.Checkbutton(
            frm,
            text="Delete originals after operation",
            variable=self.delete_var
        ).pack(anchor=tk.W)

        # Buttons
        row3 = ttk.Frame(frm)
        row3.pack(pady=pad)

        ttk.Button(row3, text="Encrypt", command=self._encrypt).pack(side=tk.LEFT, padx=5)
        ttk.Button(row3, text="Decrypt", command=self._decrypt).pack(side=tk.LEFT, padx=5)

    def _browse(self):
        path = filedialog.askopenfilename()
        if not path:
            path = filedialog.askdirectory()
        if path:
            self.path_var.set(path)

    def _encrypt(self):
        if self.pw_var.get() != self.pw2_var.get():
            messagebox.showerror("Error", "Passwords do not match")
            return

        path = Path(self.path_var.get())
        if not path.exists():
            messagebox.showerror("Error", "Invalid path")
            return

        Lockbox.encrypt_path(path, self.pw_var.get(), self.delete_var.get())
        messagebox.showinfo("Success", "Encryption done")

    def _decrypt(self):
        path = Path(self.path_var.get())
        if not path.exists():
            messagebox.showerror("Error", "Invalid path")
            return

        Lockbox.decrypt_path(path, self.pw_var.get(), self.delete_var.get())
        messagebox.showinfo("Success", "Decryption done")