import tkinter as tk

FONT = ("Calibri", 15)
CONVERSION_TO_KM = 1.6
CONVERSION_TO_MI = 0.6

window = tk.Tk()
window.title("Mile-Km Converter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)


def convert():
    conversion_factor = CONVERSION_TO_KM if radio_state.get() == 1 else CONVERSION_TO_MI
    result = float(user_input.get()) * conversion_factor
    result_label.config(text=f"{round(result, 2)}")


labels = {
    1: ("Mi", "km"),
    2: ("km", "Mi")
}


def radio_used():
    selection = radio_state.get()
    from_label.config(text=labels[selection][0])
    to_label.config(text=labels[selection][1])


radio_state = tk.IntVar()
radio_to_km = tk.Radiobutton(text="Miles to km", value=1, variable=radio_state, command=radio_used)
radio_to_mi = tk.Radiobutton(text="Km to miles", value=2, variable=radio_state, command=radio_used)
radio_to_km.select()
radio_to_km.grid(column=0, row=0)
radio_to_mi.grid(column=1, row=0)

user_input = tk.Entry(width=10)
user_input.focus()
user_input.grid(column=1, row=1)

from_label = tk.Label(text="Mi", font=FONT)
from_label.grid(column=2, row=1)

equal_label = tk.Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=2, padx=10, pady=10)

result_label = tk.Label(text="0", font=FONT)
result_label.grid(column=1, row=2)

to_label = tk.Label(text="km", font=FONT)
to_label.grid(column=2, row=2)

calculate_button = tk.Button(text="CALCULATE", command=lambda: convert(), padx=5, pady=5)
calculate_button.grid(column=1, row=3, padx=10, pady=10)

window.mainloop()


