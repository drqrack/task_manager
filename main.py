import tkinter as tk
import ui

app = tk.Tk()
app.title("Task Manager")
app.geometry("")
app.resizable(True, True)

app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)

ui.show_all_tasks_frame(app)

app.mainloop()