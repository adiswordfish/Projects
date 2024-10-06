import { useState, useEffect } from 'react';
import axios from 'axios';
import styled from '@emotion/styled';

const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const Input = styled.input`
  margin-bottom: 10px;
`;

const ListItem = styled.div`
  display: flex;
  align-items: center;
`;

const EditInput = styled.input`
  margin-left: 10px;
`;

function App() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');
  const [editing, setEditing] = useState(null);

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    const response = await axios.get('/api/todos');
    setTodos(response.data);
  };

  const addTodo = async () => {
    await axios.post('/api/todos', { text: newTodo });
    setNewTodo('');
    fetchTodos();
  };

  const updateTodo = async (id, newText) => {
    await axios.put(`/api/todos/${id}`, { text: newText });
    fetchTodos();
  };

  const deleteTodo = async (id) => {
    await axios.delete(`/api/todos/${id}`);
    fetchTodos();
  };

  return (
    <Container>
      <h1>To-Do App</h1>
      <Input
        value={newTodo}
        onChange={(e) => setNewTodo(e.target.value)}
        placeholder="New to-do"
      />
      <button onClick={addTodo}>Add</button>
      {todos.map((todo) => (
        <ListItem key={todo.id}>
          {editing === todo.id ? (
            <EditInput
              defaultValue={todo.text}
              onBlur={(e) => {
                updateTodo(todo.id, e.target.value);
                setEditing(null);
              }}
            />
          ) : (
            <span onDoubleClick={() => setEditing(todo.id)}>{todo.text}</span>
          )}
          <button onClick={() => deleteTodo(todo.id)}>Delete</button>
        </ListItem>
      ))}
    </Container>
  );
}

export default App;
