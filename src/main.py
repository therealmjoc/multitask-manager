import tkinter as tk
window = tk.Tk()
window.title("Multitask Manager")

text = tk.Label(window, text="Hello Matthew, you have 5 assignments due today.")
text.pack()

button = tk.Button(window, text='Stop', width=25, command=window.destroy)
button.pack()

window.mainloop()