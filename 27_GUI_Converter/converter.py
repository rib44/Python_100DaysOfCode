import tkinter


window = tkinter.Tk()
window.title("Mile to KM converter")

window.config(padx=20, pady=20)

user_in = tkinter.Entry(width=10)
user_in.insert(tkinter.END, string="0")
user_in.grid(row=0, column=1, ipady=6)

label_miles = tkinter.Label(text="Miles", font=("Arial", 12, "normal"))
label_miles.grid(row=0, column=2)

label_is_equal_to = tkinter.Label(text="is equal to", font=("Arial", 12, "normal"))
label_is_equal_to.grid(row=1, column=0)

label_ans = tkinter.Label(text="0.0", font=("Arial", 12, "normal"))
label_ans.grid(row=1, column=1)

label_km = tkinter.Label(text="Km", font=("Arial", 12, "normal"))
label_km.grid(row=1, column=2)


def solve():
    user_input = int(user_in.get())
    ans = round(user_input * 1.60934, 2)
    label_ans.config(text=ans)


button_submit = tkinter.Button(text="Calculate", command=solve)
button_submit.grid(row=2, column=1)


window.mainloop()
