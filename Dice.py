import tkinter as tk
from tkinter import Label, Button
import random

class DiceSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Rolling Simulator")

        self.label = Label(self.master, text="Welcome to Dice Rolling Simulator!", font=("Arial", 18))
        self.label.pack(pady=20)

        self.result_label = Label(self.master, text="", font=("Arial", 24, "bold"))
        self.result_label.pack(pady=50)

        self.roll_button = Button(self.master, text="Roll the Dice", command=self.roll_dice, font=("Arial", 16))
        self.roll_button.pack()

    def roll_dice(self):
        # Generate a random number between 1 and 6 (simulating a dice roll)
        dice_value = random.randint(1, 6)
        self.result_label.config(text=f"Result: {dice_value}")

def main():
    root = tk.Tk()
    dice_simulator = DiceSimulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# This example assumes a standard six-sided die (hence, numbers range from 1 to 6).