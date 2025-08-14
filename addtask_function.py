import add
import show
import update
import delete

add_task_response = add.add_task("Sleep")       # creating a variable(add_task_response), calling the file(add), calling the function(add_task()) 
print(add_task_response)

show_task_response = show.show_tasks()
print(show_task_response)

update_task_response = update.update_task("Sleep", "Wake Up")
print(update_task_response)

delete_task_response = delete.delete_task("Wake Up")
print(delete_task_response)