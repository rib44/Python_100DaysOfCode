from tkinter import *


window = Tk()
window.title("GUI Application")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)
# my_label["text"] = "New Text"
# my_label.config(text="aloha")


# button
def button_function():
    print("Pressed")


button = Button(text="Click me", command=button_function)
button.grid(row=1, column=1)

btn = Button(text="New Button")
btn.grid(row=0, column=2)


# Entry
input1 = Entry(width=10)
input1.grid(row=2, column=3)


window.mainloop()
