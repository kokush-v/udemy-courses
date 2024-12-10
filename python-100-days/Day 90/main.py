import tkinter as tk
from threading import Timer

TIME_LIMIT = 5


class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Most Dangerous Writing App")

        self.text_widget = tk.Text(
            root, wrap="word", font=("Arial", 14), undo=True)
        self.text_widget.pack(expand=True, fill="both", padx=10, pady=10)

        self.text_widget.bind("<Key>", self.reset_timer)

        self.timer_label = tk.Label(text=0)
        self.timer_label.pack()

        self.remaining_time = TIME_LIMIT
        self.timer = None
        self.update_timer()

    def update_timer(self):
        if self.remaining_time > 0:
            self.timer_label.config(
                text=f"Time Left: {self.remaining_time} seconds")
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.erase_text()

    def reset_timer(self, event=None):
        self.remaining_time = TIME_LIMIT

    def erase_text(self):
        self.text_widget.delete("1.0", tk.END)
        self.start_timer()


root = tk.Tk()
app = DangerousWritingApp(root)

root.mainloop()
