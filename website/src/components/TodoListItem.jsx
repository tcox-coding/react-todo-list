import React, { useState } from "react";

import './TodoListItem.css';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCircle } from '@fortawesome/free-solid-svg-icons';
import { faCircle as faCircleLight } from '@fortawesome/free-regular-svg-icons';

import { useTodoListsContext } from "./TodoListsContext";

export default function TodoListItem(props) {
  return (
    <div className="todo-list-item">
      <button onClick={props.onClickHandler}>
        <p>{props.name}</p>
        { props.selected ? <FontAwesomeIcon icon={faCircle} /> : <FontAwesomeIcon icon={faCircleLight} /> }
      </button>
    </div>
  )
}