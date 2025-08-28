import db

# Define a function save task and return true
def save_task(task):
    # Save task to database
    db.tasks.insert_one(task)
    # Return response
    return True

# A function to delete a task
def delete_task(id):
    # Delete task from database
    db.tasks.delete_one({"_id": id})
    # Return response
    return True

# Define a function find task and return true
def get_tasks():
    # Get all tasks from database
    all_tasks = db.tasks.find()
    # Return response
    return all_tasks

# A function to update a task
def update_task(id, update):
    # Update task in database
    db.tasks.update_one({"_id": id}, {"$set": update})
    # Return response
    return True