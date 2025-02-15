import { createContext, useContext } from "react";

import { TodoListsAndTasksInterface } from "../types";

export const TodoListsContext = createContext<TodoListsAndTasksInterface | undefined>(undefined);

export function useTodoListsContext() {
  const context = useContext(TodoListsContext);

  if (context === undefined) {
    throw new Error('useTodoListsContext must be used within a TodoListsContextProvider');
  }

  return context;
}