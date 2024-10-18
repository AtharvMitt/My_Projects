import tkinter


def Calc():
    Kms = float(Miles.get()) * 1.609
    my_label_km.config(text=int(Kms))


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="is equal to")
my_label.grid(column=0, row=1)

Miles = tkinter.Entry(width=7)
Miles.grid(column=1, row=0)

my_label_miles = tkinter.Label(text="Miles")
my_label_miles.grid(column=2, row=0)

my_label_km = tkinter.Label(text="0")
my_label_km.grid(column=1, row=1)

my_label_KiloMeters = tkinter.Label(text="Km")
my_label_KiloMeters.grid(column=2, row=1)

my_button = tkinter.Button(text="Calculate", command=Calc)
my_button.grid(column=1, row=2)
window.mainloop()
