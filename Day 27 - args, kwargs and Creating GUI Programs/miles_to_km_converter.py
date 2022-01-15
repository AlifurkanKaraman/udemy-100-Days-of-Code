from tkinter import *


def miles_to_km():
    mile = miles_input.get()
    km = int(mile) * 1.609
    km_result_label.config(text=round(km))


FONT = ("Arial", 15, "italic")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Label 1
mile_label = Label(text="Miles", font=FONT)
mile_label.grid(column=2, row=0)

# Label 2
is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=0, row=1)

# Label 3
km_result_label = Label(text='0', font=FONT)
km_result_label.grid(column=1, row=1)

# Label 4
km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

# Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()

