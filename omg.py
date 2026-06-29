import tkinter as tk
window = tk.Tk()
info=tk.Entry(text=("name"))
info2=tk.Entry(text="age")
info3=tk.Entry(text="department")
def  check() :
    a=tk.Label(text=str(info.get()))
    X=tk.Label(text=2026-(int(info2.get())))
    y=tk.Label(text=str(info3.get()))
    a.pack()
    X.pack()
    y.pack()
b=tk.Button(text="click me",
            command=check)
b.pack()
info.pack()
info2.pack()
info3.pack()
window.mainloop()