# Import basic Tkinter library for GUI
import tkinter as tk  # (Python Software Foundation, 2023)

# Create main application class
class StudentTrackerApp:
    def __init__(self, root):
        self.root = root
        
        # Set window title
        self.root.title("Student Progress Tracker")  # simple title
        
        # Set window size
        self.root.geometry("800x500")  # standard window size
        
        # Set background color
        self.root.configure(bg="#1e1e2e")  # dark theme (student style choice)
        
        # Create basic label
        self.title_label = tk.Label(
            root, 
            text="Student Progress Tracker",
            font=("Arial", 18),
            fg="white",
            bg="#1e1e2e"
        )
        self.title_label.pack(pady=20)  # add spacing

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentTrackerApp(root)
    root.mainloop()