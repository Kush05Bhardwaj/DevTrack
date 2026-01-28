const form = document.getElementById('task-form');
const taskList = document.getElementById('task-list');

//  Temporary backend URL for development

let tasks = [];

from.addEventListener('submit', async (e) => {
    e.preventDefault();
    const title = form.elements['title'].value;
    const description = form.elements['description'].value;

    const task = { 
        id: Date.now(),
        title: title,
        description: description,
        status: 'pending'
    };
    tasks.push(task);
    renderTasks();
    form.reset();
});

function renderTasks() {
    taskList.innerHTML = '';
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.textContent = `${task.title} - ${task.description} [${task.status}]`;
        taskList.appendChild(li);
    });
}