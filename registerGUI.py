import tkinter as tk
from tkinter import ttk
from compiler import Compiler

class RegisterGUI:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Register GUI")

        self.compiler = Compiler()

        # Layout frames
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side="left", fill="both", expand=True)

        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Text input on the left
        self.text_input = tk.Text(self.left_frame, width=30, height=20)
        self.text_input.pack(padx=10, pady=10)
        self.text_input.bind("<KeyRelease>", self.on_text_change)

        # Table on the right (1 rows x 8 columns)
        self.columns = [f"R{i+1}" for i in range(8)]
        self.tree = ttk.Treeview(self.right_frame, columns=self.columns, show="headings", height=1)
        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=60, anchor="center")

        self.tree.pack(padx=10, pady=10)

        # Add 1 empty row
        self.tree.insert("", "end", iid="row0", values=[""] * 8)
        self.root.mainloop()

    def on_text_change(self, event):
        user_input = self.text_input.get("1.0", "end-1c").strip()
        self.compiler.interpretText(user_input)
        self.update_table()

    def update_table(self):
        self.tree.item("row0", values=self.compiler.registers)
