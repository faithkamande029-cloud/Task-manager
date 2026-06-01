from datetime import datetime

# Import validation functions
from validation import  validate_task_title, validate_task_description, validate_due_date


# Define tasks list
tasks =[ {
    "title": "Groceries",
    "description": "Shop at Market Basket for food", 
    "due_date": "2024-06-26",
    "completed": True
}]

next_id = 2


# Implement add_task function
def add_task(title, due_date,  description=""):
    global next_id

    errors = []

    title_check = validate_task_title(title)
    description_check = validate_task_description(description)
    date_check = validate_due_date(due_date)

    if not title_check["is_valid"]:
        errors.extend(title_check["errors"])

    if not description_check["is_valid"]:
        errors.extend(description_check["errors"])  # add description errors
 
    if not date_check["is_valid"]:
        errors.extend(date_check["errors"])  # add date errors

    if errors:
        return {"success": False, "task": None, "errors": errors}
    
    new_task = {
        "id"         : next_id,
        "title"      : title_check["value"],
        "description": description_check["value"],
        "due_date"   : date_check["value"],
        "completed"  : False,
        "created_at" : datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    }

    tasks.append(new_task)
    next_id += 1

    print("Task added successfully!")
    return {"success": True, "task": new_task, "errors": []}

    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("No task found at that position")
        return
    
    task = tasks[index]

    if task["completed"]:
        print(f"'{task['title']}' if already compelete!")
        return
    task["completed"] = True

    print(f"Task marked as complete! '{task['title']}'")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = []
    for task in tasks:
        if not task["completed"]:
            pending.append(task)

    # If no pending tasks, let the user know
    if not pending:
        print("No pending tasks!")
        return []
    
    print(f"You have {len(pending)} pending task(s):\n")
    for index, task in enumerate(pending):
        print(f"  {index}. {task['title']} — due {task['due_date']}")

    return pending

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    # Count total and completed tasks
    total = len(tasks)
    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    # Calculate the remaining and percentage
    pending = total - completed
    percentage = round((completed / total) * 100, 1) if total > 0 else 0.0

    # Build the progress dictionary
    progress = {
        "total"     : total,
        "completed" : completed,
        "pending"   : pending,
        "percentage": percentage
    }

    return progress