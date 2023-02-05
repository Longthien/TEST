import tkinter as tk

def do_nothing():
    pass

root = tk.Tk()
root.title("Key press event")

root.protocol("WM_DELETE_WINDOW", do_nothing)
label = tk.Label(root, text="CON CAC THANG LON THIEN",font=("Helvetica",20))
label.pack()


root.mainloop()