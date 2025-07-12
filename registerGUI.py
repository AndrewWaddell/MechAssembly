import tkinter as tk
from tkinter import ttk
from compiler import Compiler
from tkinter import Canvas


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

        # New drawing frame
        self.drawing_frame = tk.Frame(self.root)
        self.drawing_frame.pack(side="right", fill="both", expand=True)

        # Canvas for drawing
        self.canvas = Canvas(self.drawing_frame, bg="white", width=600, height=400)
        self.canvas.pack(fill="both", expand=True, padx=10, pady=10)

        # Drawing parameters
        self.cell_width = 60
        self.cell_height = 40
        self.start_x = 70
        self.start_y = 50

        # Text input on the left
        self.text_input = tk.Text(self.left_frame, width=30, height=20)
        self.text_input.pack(padx=10, pady=10)
        self.text_input.bind("<KeyRelease>", self.on_text_change)

        # Vertical table on the right (8 rows x 2 columns: Register name + Value)
        self.columns = ["Register", "Value"]
        self.tree = ttk.Treeview(
            self.right_frame, columns=self.columns, show="headings", height=8
        )

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
        self.compiler.resetRegisters()
        user_input = self.text_input.get("1.0", "end-1c").strip()
        self.compiler.interpretText(user_input)
        self.update_table()
        self.update_drawing()

    def update_table(self):
        registers = self.compiler.getRegisters()
        # Update each row with the corresponding register value
        for i, value in enumerate(registers):
            if i < 8:  # Safety check
                self.tree.item(f"row{i}", values=[f"R{i+1}", value])

    def calculate_grid_dimensions(self):
        """Calculate the maximum columns needed based on data"""
        max_col = 0

        # Check instructions for max column
        for row, col, text in self.compiler.gridInstructions:
            max_col = max(max_col, col)

        # Check axis for max column (start_col + span - 1)
        for start_col, span, text in self.compiler.axis:
            max_col = max(max_col, start_col + span - 1)

        return max_col

    def draw_cell(self, row, col, text=""):
        """Draw a single cell with optional text"""
        x1 = self.start_x + (col - 1) * self.cell_width
        y1 = self.start_y + (row - 1) * self.cell_height
        x2 = x1 + self.cell_width
        y2 = y1 + self.cell_height

        # Draw rectangle
        self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)

        # Draw text if provided
        if text:
            center_x = x1 + self.cell_width // 2
            center_y = y1 + self.cell_height // 2
            self.canvas.create_text(
                center_x, center_y, text=text, font=("Arial", 12, "bold"), fill="black"
            )

    def draw_axis_cell(self, start_col, span, text=""):
        """Draw an axis cell that spans multiple columns"""
        row = 0  # Axis is always on row 1
        x1 = self.start_x + (start_col - 1) * self.cell_width
        y1 = self.start_y + (row - 1) * self.cell_height
        x2 = x1 + span * self.cell_width
        y2 = y1 + self.cell_height

        # Draw rectangle
        self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)

        # Draw text if provided
        if text:
            center_x = x1 + (span * self.cell_width) // 2
            center_y = y1 + self.cell_height // 2
            self.canvas.create_text(
                center_x, center_y, text=text, font=("Arial", 12, "bold"), fill="black"
            )


def update_drawing(self):
    """Update the drawing display with current data"""
    self.canvas.delete("all")

    # Fixed canvas size
    canvas_width = 600
    canvas_height = 400

    # Get max number of columns and rows
    max_col = max(self.calculate_grid_dimensions(), 1)
    max_row = max((row for row, _, _ in self.compiler.gridInstructions), default=1)

    # Calculate dynamic cell size based on how much space we have
    self.cell_width = (canvas_width - 2 * self.start_x) / max_col
    self.cell_height = (canvas_height - 2 * self.start_y) / max_row

    # Draw axis cells (row 0)
    for start_col, span, text in self.compiler.axis:
        self.draw_axis_cell(start_col, span, text)

    # Draw rail cells
    for row, col, text in self.compiler.gridInstructions:
        self.draw_cell(row, col, text)
