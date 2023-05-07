import tkinter as tk
from tkinter import Label, Entry, OptionMenu, Button, messagebox
from forex_python.converter import CurrencyRates

class CurrencyConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")

        self.c = CurrencyRates()

        self.label_from = Label(self.master, text="From:", font=("Arial", 14))
        self.label_from.grid(row=0, column=0, padx=10, pady=10)
        self.label_to = Label(self.master, text="To:", font=("Arial", 14))
        self.label_to.grid(row=1, column=0, padx=10, pady=10)
        self.label_amount = Label(self.master, text="Amount:", font=("Arial", 14))
        self.label_amount.grid(row=2, column=0, padx=10, pady=10)
        self.label_result = Label(self.master, text="", font=("Arial", 16, "bold"), fg="green")
        self.label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.from_currency = tk.StringVar()
        self.to_currency = tk.StringVar()
        self.amount = tk.DoubleVar()

        currencies = ["USD", "EUR", "GBP", "INR", "AUD"]  # Example currencies
        self.from_currency_menu = OptionMenu(self.master, self.from_currency, *currencies)
        self.from_currency_menu.grid(row=0, column=1, padx=10, pady=10)
        self.to_currency_menu = OptionMenu(self.master, self.to_currency, *currencies)
        self.to_currency_menu.grid(row=1, column=1, padx=10, pady=10)

        self.amount_entry = Entry(self.master, textvariable=self.amount, font=("Arial", 14))
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)

        self.convert_button = Button(self.master, text="Convert", command=self.convert, font=("Arial", 14))
        self.convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def convert(self):
        try:
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            amount = self.amount.get()

            if from_curr and to_curr and amount:
                result = self.c.convert(from_curr, to_curr, amount)
                self.label_result.config(text=f"{amount} {from_curr} = {result:.2f} {to_curr}")
            else:
                messagebox.showerror("Error", "Please select currencies and enter amount.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    currency_converter = CurrencyConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# Conversion rate
# May differ