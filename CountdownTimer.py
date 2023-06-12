import tkinter as tk
from tkinter import Label, Button, Entry
import time
from threading import Thread

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")

        self.label = Label(self.master, text="Enter time in seconds:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = Entry(self.master, font=("Arial", 14), width=10)
        self.entry.pack(pady=10)

        self.start_button = Button(self.master, text="Start", command=self.start_timer, font=("Arial", 14))
        self.start_button.pack()

        self.timer_label = Label(self.master, text="", font=("Arial", 24, "bold"), fg="blue")
        self.timer_label.pack(pady=20)

        self.running = False

    def start_timer(self):
        if not self.running:
            try:
                self.seconds = int(self.entry.get())
            except ValueError:
                self.timer_label.config(text="Please enter a valid number")
                return

            if self.seconds > 0:
                self.running = True
                self.countdown_thread = Thread(target=self.run_timer)
                self.countdown_thread.start()
            else:
                self.timer_label.config(text="Please enter a positive number")

    def run_timer(self):
        while self.seconds > 0 and self.running:
            self.timer_label.config(text=f"Time left: {self.seconds} seconds")
            time.sleep(1)
            self.seconds -= 1

        if self.running:
            self.timer_label.config(text="Time's up!")
            self.running = False

def main():
    root = tk.Tk()
    countdown_timer = CountdownTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# This example assumes a standard six-sided die (hence, numbers range from 1 to 6).
# You can extend this simulator to include multiple dice, different types of dice (e.g., 10-sided, 20-sided),