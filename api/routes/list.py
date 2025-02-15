from fastapi import APIRouter
import psycopg2

list_router = APIRouter()

@list_router.get("/list", tags=["list"])
async def read_todo(user_id: int):
    '''
    This function will return all the lists and tasks of a given user.
    '''
    conn = psycopg2.connect(dbname="todo_application", user="postgres", password="postgres", host="0.0.0.0", port="5432")
    cur = conn.cursor()

    cur.execute(f"SELECT id FROM todo.users WHERE id = %s", (user_id,))
    row = cur.fetchone()
    if row is None:
        return {"msg": "User not found"}
    
    cur.execute(f"SELECT * FROM todo.lists WHERE user_id = %s", (row[0],))
    todos = cur.fetchall()
    lists_to_return = []
    for todo in todos:
        lists_to_return.append({
            "id": todo[0],
            "name": todo[1],
            "user_id": todo[2]
        })
    
    cur.execute(f"SELECT * FROM todo.tasks WHERE user_id = %s", (row[0],))
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
        
    return {"lists": lists_to_return, "tasks": tasks_to_return}

@list_router.post("/list", tags=["list"])
async def create_todo(user_id: int, list_name: str):
    '''
    This function will create a new list for a given user.
    '''
    conn = psycopg2.connect(dbname="todo_application", user="postgres", password="postgres", host="0.0.0.0", port="5432")
    cur = conn.cursor()

    cur.execute(f"SELECT id FROM todo.users WHERE user_id = %s", (user_id,))
    row = cur.fetchone()
    if row is None:
        return {"msg": "User not found"}
    
    cur.execute(f"INSERT INTO todo.lists (name, user_id) VALUES (%s, %s) RETURNING id", (list_name, row[0]))
    list_id = cur.fetchone()[0]
    conn.commit()

    return {"msg": "List created", "list_id": list_id}  

@list_router.patch("/list", tags=["list"])
async def update_todo(user_id: int, list_id: int, list_name: str):
    '''
    This function will update the name of a list for a given user.
    '''
    conn = psycopg2.connect(dbname="todo_application", user="postgres", password="postgres", host="0.0.0.0", port="5432")
    cur = conn.cursor()

    cur.execute(f"UPDATE todo.lists SET name = %s WHERE id = %s AND user_id = %s", (list_name, list_id, user_id))
    conn.commit()

    return {"msg": "List updated"}

@list_router.delete("/list", tags=["list"])
async def delete_todo(user_id: int, list_id: int):
    '''
    This function will delete a list for a given user.
    '''
    conn = psycopg2.connect(dbname="todo_application", user="postgres", password="postgres", host="0.0.0.0", port="5432")
    cur = conn.cursor()

    cur.execute(f"DELETE FROM todo.lists WHERE id = %s AND user_id = %s", (list_id, user_id))
    conn.commit()

    return {"msg": "List deleted"}