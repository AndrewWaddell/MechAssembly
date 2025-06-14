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

        # Vertical table on the right (8 rows x 2 columns: Register name + Value)
        self.columns = ["Register", "Value"]
        self.tree = ttk.Treeview(self.right_frame, columns=self.columns, show="headings", height=8)
        
        # Configure columns
        self.tree.heading("Register", text="Register")
        self.tree.heading("Value", text="Value")
        self.tree.column("Register", width=80, anchor="center")
        self.tree.column("Value", width=80, anchor="center")

        self.tree.pack(padx=10, pady=10)

        # Add 8 rows for R1-R8
        for i in range(8):
            self.tree.insert("", "end", iid=f"row{i}", values=[f"R{i+1}", ""])
            
        self.root.mainloop()

    def on_text_change(self, event):
        user_input = self.text_input.get("1.0", "end-1c").strip()
        self.compiler.interpretText(user_input)
        self.update_table()

    def update_table(self):
        registers = self.compiler.getRegisters()
        # Update each row with the corresponding register value
        for i, value in enumerate(registers):
            if i < 8:  # Safety check
                self.tree.item(f"row{i}", values=[f"R{i+1}", value])