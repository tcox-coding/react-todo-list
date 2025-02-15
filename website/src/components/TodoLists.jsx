import TodoListItem from "./TodoListItem";

import { useTodoListsContext } from "./TodoListsContext";

import "./TodoLists.css";
import { useContext, useState } from "react";

export default function TodoLists() {
  const todos = useTodoListsContext();
  const [selected, setSelected] = useState(false);

  const onClickHandler = (e) => {
    e.preventDefault();
    let new_lists = [];
    for (let i = 0; i < todos['todoListData']['lists'].length; i++) {
      let list = todos['todoListData']['lists'][i];
      list['selected'] = (list.name === e.target.textContent && (list['selected'] === false || list['selected'] === undefined));
      new_lists.push(list);
    }
    setSelected(!selected);
    todos['setTodoListData']({
      lists: new_lists,
      tasks: todos['todoListData']['tasks']
    });
  }

  if (todos['todoListData']['lists'] === undefined) {
    return (
      <div id="todo-lists-container">
        <h1 className="inter-font">Lists</h1>
        <div id="todo-lists">
          <p>Loading...</p>
        </div>
      </div>
    )
  } else {
    return (
      <div id="todo-lists-container">
        <h1 className="inter-font">Lists</h1>
        <div id="todo-lists">
          {
            todos['todoListData']['lists'].map((list) => {
              return <TodoListItem name={list.name} onClickHandler={onClickHandler} selected={list.selected}></TodoListItem>
            })
          }
        </div>
      </div>
    )
  }
}