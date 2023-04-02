import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometers Converter")
window.minsize()
window.config(padx=30, pady=30)

is_equal_to = tkinter.Label(text="is equal to", font=("Arial", 18, "normal"))
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=10, pady=10)

entry_input = tkinter.Entry(width=10)
entry_input.grid(column=1, row=0)

result = tkinter.Label(text="0", font=("Arial", 18, "normal"))
result.grid(column=1, row=1)


def button_clicked():
    km_value = round(float(entry_input.get()) * 1.609, 3)
    result.config(text=km_value, font=("Arial", 18, "normal"))


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

miles = tkinter.Label(text="Miles", font=("Arial", 18, "normal"))
miles.grid(row=0, column=2)
miles.config(pady=10, padx=10)

km = tkinter.Label(text="Km", font=("Arial", 18, "normal"))
km.grid(row=1, column=2)
km.config(padx=10, pady=10)





window.mainloop()