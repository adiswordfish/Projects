// pages/api/todos.js
import { v4 as uuidv4 } from 'uuid';

let todos = [
  { id: uuidv4(), text: 'Example to-do 1' },
  { id: uuidv4(), text: 'Example to-do 2' },
];

export default function handler(req, res) {
  const { method } = req;

  switch (method) {
    case 'GET':
      res.status(200).json(todos);
      break;
  }}
