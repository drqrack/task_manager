import tkinter as tk
import ui

app = tk.Tk()
app.title("Task Manager")
app.geometry("")
app.resizable(True, True)

ui.show_all_tasks_frame(app)

app.mainloop()