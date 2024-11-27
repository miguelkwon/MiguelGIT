import requests
import json
import tkinter as tk
from tkinter import Listbox, Button, messagebox

def get_vnd_exchange_rates(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/VND"
    response = requests.get(url)
    
    if response.status_code != 200:
        messagebox.showerror("Error", "Failed to retrieve data from ExchangeRate-API.")
        return []
    
    data = response.json()
    if data['result'] != 'success':
        messagebox.showerror("Error", "Error in fetching exchange rates.")
        return []
    
    rates = data['conversion_rates']
    exchange_rates = [(currency, rate) for currency, rate in rates.items()]
    return exchange_rates

# GUI setup
root = tk.Tk()
root.title("베트남환율 정보")

# Create listbox
listbox = Listbox(root, width=50)
listbox.pack(padx=10, pady=10)

# API key for ExchangeRate-API
API_KEY = "YOUR_API_KEY"  # Replace with your API key

# Fetch exchange rates and update the listbox
def fetch_exchange_rates():
    exchange_rates = get_vnd_exchange_rates(API_KEY)
    if exchange_rates:
        listbox.delete(0, tk.END)
        for currency, rate in exchange_rates:
            listbox.insert(tk.END, f"{currency}: {rate}")

# Create button
button = Button(root, text="환율정보 가져오기", command=fetch_exchange_rates)
button.pack(pady=10)

# Run GUI loop
root.mainloop()
