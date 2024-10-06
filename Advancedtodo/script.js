document.getElementById("addTaskForm").addEventListener("submit", addTask);

loadTasksFromStorage();

function addTask(event) {
  event.preventDefault();

  const taskText = document.getElementById("inputTask").value.trim();
  const taskCategory = document.getElementById("inputCategory").value.trim();
  const taskDueDate = document.getElementById("inputDueDate").value;

  if (taskText === "") return;

  const taskList = document.getElementById("taskList");
  const task = document.createElement("li");

  const taskContent = document.createElement("div");
  taskContent.textContent = taskText;

  const category = document.createElement("span");
  category.classList.add("category");
  category.textContent = taskCategory ? `Category: ${taskCategory}` : "";

  const dueDate = document.createElement("span");
  dueDate.classList.add("due-date");
  dueDate.textContent = taskDueDate ? `Due: ${taskDueDate}` : "";

  const deleteButton = document.createElement("span");
  deleteButton.textContent = "Delete";
  deleteButton.classList.add("delete");
  deleteButton.addEventListener("click", () => {
    taskList.removeChild(task);
    saveTasksToStorage();
  });

  const editButton = document.createElement("span");
  editButton.textContent = "Edit";
  editButton.classList.add("edit");
  editButton.addEventListener("click", () => {
    const newText = prompt("Edit task:", taskText);
    if (newText) {
      taskContent.textContent = newText;
      saveTasksToStorage();
    }
  });

  const checkboxContainer = document.createElement("div");
  checkboxContainer.classList.add("checkbox-container");

  const completedCheckbox = document.createElement("input");
  completedCheckbox.type = "checkbox";
  completedCheckbox.addEventListener("change", () => {
    taskContent.classList.toggle("status");
    saveTasksToStorage();
  });

  const completedLabel = document.createElement("label");
  completedLabel.textContent = "Completed";

  checkboxContainer.appendChild(completedCheckbox);
  checkboxContainer.appendChild(completedLabel);

  task.appendChild(taskContent);
  task.appendChild(category);
  task.appendChild(dueDate);
  task.appendChild(checkboxContainer);
  task.appendChild(deleteButton);
  task.appendChild(editButton);

  taskList.appendChild(task);

  document.getElementById("inputTask").value = "";
  document.getElementById("inputCategory").value = "";
  document.getElementById("inputDueDate").value = "";

  saveTasksToStorage();
}

function saveTasksToStorage() {
  const taskList = document.getElementById("taskList");
  localStorage.setItem("taskList", taskList.innerHTML);
}

function loadTasksFromStorage() {
  const taskList = document.getElementById("taskList");
  const savedTasks = localStorage.getItem("taskList");
  if (savedTasks) {
    taskList.innerHTML = savedTasks;
    addListenersToExistingTasks();
  }
}

function addListenersToExistingTasks() {
  const taskList = document.getElementById("taskList");
  const deleteButtons = taskList.querySelectorAll(".delete");
  const editButtons = taskList.querySelectorAll(".edit");
  const checkboxes = taskList.querySelectorAll("input[type='checkbox']");
}

  deleteButtons.forEach((button) => {
    button.addEventListener("click", () => {
      taskList.removeChild(button.parentElement);
      saveTasksToStorage();
    });
  });

  editButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const newText = prompt("Edit task:", button.parentElement.firstChild.textContent);
      if (newText) {
        button.parentElement.firstChild.textContent = newText;
        saveTasksToStorage();
      }
    });
  });

  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", () => {
      checkbox.parentElement.previouscheckboxes.forEach((checkbox) => {
        checkbox.addEventListener("change", () => {
          checkbox.parentElement.previousElementSibling.previousElementSibling.previousElementSibling.classList.toggle("status");
          saveTasksToStorage();
        });
      });
    })}
  )
