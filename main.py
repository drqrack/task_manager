import tkinter as tk
import ui

app = tk.Tk()
app.title("Task Manager")
app.geometry("720x480")

ui.show_all_tasks_frame(app)

app.mainloop()