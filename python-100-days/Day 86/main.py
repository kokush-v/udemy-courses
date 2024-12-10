import tkinter as tk
from tkinter import messagebox
import time

words = [
    "apple", "mountain", "river", "galaxy", "window", "system", "bicycle", "adventure",
    "technology", "ocean", "elephant", "wonderful", "keyboard", "thunderstorm",
    "pineapple", "imagination", "software", "friendship", "rainbow", "university",
    "forest", "computer", "library", "science", "fantasy", "strawberry", "dinosaur",
    "butterfly", "coffee", "fireplace", "telephone", "chocolate", "musician", "airplane",
    "symphony", "volcano", "television", "astronaut", "jungle", "fireworks", "backpack",
    "sunshine", "mountainous", "exploration", "calculator", "dictionary", "photograph",
    "carousel", "spaceship", "whisper"
]


class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("500x450")
        self.timer = 60

        self.sample_text = " ".join(words)
        self.start_words_count = len(words)
        self.start_time = None

        self.label = tk.Label(
            root, text="Type the following text as fast as you can:")
        self.label.pack(pady=10)

        self.text_display = tk.Text(root, wrap="word", height=2, width=40)
        self.text_display.pack(pady=10)
        self.text_display.insert(tk.END, self.sample_text)
        self.text_display.config(state=tk.DISABLED)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<space>", self.pass_word)
        self.entry.bind("<Return>", self.pass_word)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
        self.timer_label = tk.Label(root, text="60")
        self.timer_label.pack(pady=10)

    def pass_word(self, event):
        global words

        word = words[0]
        typed_text = self.entry.get().strip()

        if word == typed_text:
            words = words[1::]
            self.text_display.config(state=tk.NORMAL)
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, " ".join(words))
            self.text_display.config(state=tk.DISABLED)

            self.result_label.config(text="Nice!")

        else:
            self.result_label.config(text='Wrong')

        self.entry.delete(0, tk.END)

    def reset_test(self):
        self.start_time = None
        self.entry.delete(0, tk.END)

    def countdown(self):
        self.timer_label.config(text=str(self.timer))
        if self.timer == 0:
            self.result_label.config(text=f"Great job you got {
                                     self.start_words_count - len(words)} words/min")
            self.entry.config(state=tk.DISABLED)
            self.entry.unbind("<space>")
            self.entry.unbind("<Return>")

            return
        self.timer -= 1
        self.root.after(1000, self.countdown)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    app.countdown()
    root.mainloop()
