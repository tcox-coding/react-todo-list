import { TodoListsContext, useTodoListsContext } from "./components/TodoListsContext";

import React, { useState, useEffect } from 'react'

import Header from './components/Header'
import TodoLists from './components/TodoLists'
import TodoList from './components/TodoList'

import './App.css'

function App() {
  // TODO: Get data from the server.
    const [todoListData, setTodoListData] = useState({});

    useEffect(() => {
      fetch("http://localhost:5000/list?user_id=1")
        .then(response => response.json())
        .then(data => {
          setTodoListData(data);  
      });
    }, []);

  return (
    <>
      <Header></Header>
      <div id="container">
        <TodoListsContext.Provider value={{todoListData, setTodoListData}}>
          <TodoLists></TodoLists>
          <TodoList></TodoList>
        </TodoListsContext.Provider>
      </div>
    </>
  )
}

export default App
