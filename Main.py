import tkinter as tk
from tkinter import messagebox


# Function to get exchange rate for different currencies
def get_exchange_rate(from_currency, to_currency):
    # Sample exchange rates between currencies (you can add more as needed)
    exchange_rates = {
        'USD': {'EUR': 0.94, 'GBP': 0.82, 'INR': 83.21},
        'EUR': {'USD': 1.06, 'GBP': 0.87, 'INR': 88.54},
        'GBP': {'USD': 1.22, 'EUR': 1.15, 'INR': 101.47},
        'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0098},
    }

    # Return the exchange rate if available, else return None
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        return exchange_rates[from_currency][to_currency]
    else:
        return None  # If the conversion is not available


# Function to perform currency conversion
def convert_currency():
    try:
        # Get the amount entered by the user and convert it to float
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numerical amount.")
        return

    from_currency = from_currency_var.get()  # Get the selected 'from' currency
    to_currency = to_currency_var.get()  # Get the selected 'to' currency

    # Get the exchange rate for the selected currencies
    rate = get_exchange_rate(from_currency, to_currency)

    # Check if the rate is valid, if not show an error
    if rate is None:
        messagebox.showerror("Conversion Error", f"Cannot convert from {from_currency} to {to_currency}.")
    else:
        # Calculate the converted amount
        converted_amount = amount * rate
        # Update the result label to show the result
        result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")


# Create the main window for the GUI
root = tk.Tk()
root.title("Currency Converter")

# Create and place labels, buttons, and input fields in the grid layout
amount_label = tk.Label(root, text="Enter amount:")
amount_label.grid(row=0, column=0, padx=10, pady=10)

amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

from_currency_label = tk.Label(root, text="From currency:")
from_currency_label.grid(row=1, column=0, padx=10, pady=10)

# Dropdown menu for selecting from currency
from_currency_var = tk.StringVar()
from_currency_menu = tk.OptionMenu(root, from_currency_var, "USD", "EUR", "GBP", "INR")
from_currency_menu.grid(row=1, column=1, padx=10, pady=10)

to_currency_label = tk.Label(root, text="To currency:")
to_currency_label.grid(row=2, column=0, padx=10, pady=10)

# Dropdown menu for selecting to currency
to_currency_var = tk.StringVar()
to_currency_menu = tk.OptionMenu(root, to_currency_var, "USD", "EUR", "GBP", "INR")
to_currency_menu.grid(row=2, column=1, padx=10, pady=10)

# Button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display the conversion result
result_label = tk.Label(root, text="Conversion result will appear here.", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Set default currency values for both dropdowns
from_currency_var.set("USD")
to_currency_var.set("EUR")

# Start the main event loop to display the window
root.mainloop()
