import "./TodoList.css";
import React, { useState, useEffect, useMemo } from "react";
import { useTodoListsContext } from "./TodoListsContext";

export default function TodoList(props) {
  const [selected, setSelected] = useState(false);
  const todos = useTodoListsContext();
  const [tasks, setTasks] = useState([]);
  const [selectedListName, setSelectedListName] = useState('');

  const memoizedLists = useMemo(() => {
    return JSON.stringify(todos['todoListData']['lists']);
  }, [todos['todoListData']['lists']]);

  useEffect(() => {
    if (todos['todoListData']['lists'] === undefined) {
      return;
    } else if (todos['todoListData']['lists'].filter((list) => list['selected'] === true).length === 0) {
      setTasks([]);
      setSelectedListName('');
      return;
    }

    let selected_list = todos['todoListData']['lists'].filter((list) => {
      return list['selected'] === true;
    })[0];

    console.log(selected_list)
    
    let taskspush = [];
    if (selected_list === undefined) {
      return;
    } else {
      todos['todoListData']['tasks'].map((task) => {
        if (task['list_id'] === selected_list['id']) {
          taskspush.push(task);
        }
      });
    }
    setTasks(taskspush);
    setSelectedListName(selected_list['name']);
  }, [memoizedLists]);
  
  // Check if the tasks are loaded.
  if (todos['todoListData']['tasks'] === undefined) {
    return (
      <div id="todo-list-items-container">
        <h1 id="list-name"></h1>
        <p>Loading...</p>
      </div>
    )
  }

  return (
    <div id="todo-list-items-container">
      {/* <h1 id="list-name">{todos['selected_list'] ? todos['selected_list']['name'] : ''}</h1> */}
      <h1 id="list-name">{selectedListName}</h1>
      {
        tasks.map((task) => {
          return (
            <>
              <p>{task.task}</p>
            </>
          )
        })
      }
      <div id="input-task">
        <input type="text" />
        <button>Add Task</button>
      </div>
    </div>
  )
}