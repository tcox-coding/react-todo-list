
export interface TodoList {
  id: number;
  name: string;
  user_id: string;
}

export interface Task {
  id: number;
  list_id: number;
  task: string;
  todo_list_id: number;
  completed: boolean;
}


export interface TodoListsAndTasksInterface {
  list: TodoList[];
  tasks: Task[];
}