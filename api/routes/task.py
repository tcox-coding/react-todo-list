from fastapi import APIRouter
import psycopg2

task_router = APIRouter()

@task_router.get("/task/{list_id}", tags=["task"])
async def read_todo_items(user_id: int, list_id: int):
    '''
    This function will return all the tasks of a given list.
    '''
    conn = psycopg2.connect(dbname="todo_application", user="postgres", password="postgres", host="0.0.0.0", port="5432")
    cur = conn.cursor()

    cur.execute(f"SELECT id FROM todo.users WHERE user_id = %s", (user_id,))
    row = cur.fetchone()
    if row is None:
        return {"msg": "User not found"}
    
    cur.execute(f"SELECT * FROM todo.lists WHERE user_id = %s AND id = %s", (row[0], list_id))
    list_row = cur.fetchone()
    if list_row is None:
        return {"msg": "List not found"}
    
    cur.execute(f"SELECT * FROM todo.tasks WHERE user_id = %s AND list_id = %s", (row[0], list_id))
    tasks = cur.fetchall()
    tasks_to_return = []
    for task in tasks:
        tasks_to_return.append({
            "id": task[0],
            "user_id": task[1],
            "list_id": task[2],
            "task": task[3],
            "completed": task[4]
        })
    
    return {"tasks": tasks_to_return}

@task_router.post("/task/{list_id}", tags=["task"])
async def create_todo_item(user_id: int, list_id: int, task: str):
    '''
    This function will create a new task for a given list.
    '''
    conn = psycopg2.connect(dbname="todo_application", user="postgres", password="postgres", host="0.0.0.0", port="5432")
    cur = conn.cursor()

    cur.execute(f"SELECT id FROM todo.users WHERE user_id = %s", (user_id,))
    row = cur.fetchone()
    if row is None:
        return {"msg": "User not found"}
    
    cur.execute(f"SELECT * FROM todo.lists WHERE user_id = %s AND id = %s", (row[0], list_id))
    list_row = cur.fetchone()
    if list_row is None:
        return {"msg": "List not found"}
    
    cur.execute(f"INSERT INTO todo.tasks (user_id, list_id, task, completed) VALUES (%s, %s, %s, %s) RETURNING id", (row[0], list_id, task, False))
    task_id = cur.fetchone()[0]
    conn.commit()

    return {"msg": "Task created", "task_id": task_id}

@task_router.patch("/task/{list_id}/{task_id}", tags=["task"])
async def update_todo_item(user_id: int, list_id: int, task_id: int, completed: bool):
    '''
    This function will update the status of a task.
    '''
    conn = psycopg2.connect(dbname="todo_application", user="postgres", password="postgres", host="0.0.0.0", port="5432")
    cur = conn.cursor()

    cur.execute(f"SELECT id FROM todo.users WHERE user_id = %s", (user_id,))
    row = cur.fetchone()
    if row is None:
        return {"msg": "User not found"}
    
    cur.execute(f"SELECT * FROM todo.lists WHERE user_id = %s AND id = %s", (row[0], list_id))
    list_row = cur.fetchone()
    if list_row is None:
        return {"msg": "List not found"}
    
    cur.execute(f"SELECT * FROM todo.tasks WHERE user_id = %s AND list_id = %s AND id = %s", (row[0], list_id, task_id))
    task_row = cur.fetchone()
    if task_row is None:
        return {"msg": "Task not found"}
    
    cur.execute(f"UPDATE todo.tasks SET completed = %s WHERE user_id = %s AND list_id = %s AND id = %s", (completed, row[0], list_id, task_id))
    conn.commit()

    return {"msg": "Task updated"}

@task_router.delete("/task/{list_id}/{task_id}", tags=["task"])
async def delete_todo_item(user_id: int, list_id: int, task_id: int):
    '''
    This function will delete a task.
    '''
    conn = psycopg2.connect(dbname="todo_application", user="postgres", password="postgres", host="0.0.0.0", port="5432")
    cur = conn.cursor()

    cur.execute(f"SELECT id FROM todo.users WHERE user_id = %s", (user_id,))
    row = cur.fetchone()
    if row is None:
        return {"msg": "User not found"}
    
    cur.execute(f"SELECT * FROM todo.lists WHERE user_id = %s AND id = %s", (row[0], list_id))
    list_row = cur.fetchone()
    if list_row is None:
        return {"msg": "List not found"}
    
    cur.execute(f"SELECT * FROM todo.tasks WHERE user_id = %s AND list_id = %s AND id = %s", (row[0], list_id, task_id))
    task_row = cur.fetchone()
    if task_row is None:
        return {"msg": "Task not found"}
    
    cur.execute(f"DELETE FROM todo.tasks WHERE user_id = %s AND list_id = %s AND id = %s", (row[0], list_id, task_id))
    conn.commit()

    return {"msg": "Task deleted"}