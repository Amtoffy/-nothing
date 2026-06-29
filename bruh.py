import tkinter as tk
window = tk.Tk()
fg= tk.PhotoImage(file="heheeeee.jpg")
info= tk.Label(text="student information",
                 bg="light blue",
                 image=fg)
label= tk.Label(text="hello tkinter")
label.pack()
info.pack()

window.geometry("400x300")
window.mainloop()