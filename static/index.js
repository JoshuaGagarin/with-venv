const menuToggle=document.querySelector('.menuToggle');

    menuToggle.onclick = function() 
    {
        scrollToBottom()
        menuToggle.classList.toggle('active')
    }

    

    if (localStorage.getItem('isActive') === 'true') {
        menuToggle.classList.toggle('active');
        
    }
    
const closeContainer = document.querySelector('.closeContainer');
    closeContainer.onclick = function() {
        menuToggle.classList.remove('active')
    }

    function scrollToBottom() {
        console.log("hello");
        const container = document.getElementById('bayot');
        container.scrollTop = container.scrollHeight;
    }


document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    var taskInput = document.getElementById('inputValue').value;
    if (taskInput.trim() === '') return; // Don't add empty tasks

    fetch('/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'task=' + encodeURIComponent(taskInput)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            var taskList = document.getElementById('taskList');
            var newTaskItem = document.createElement('p');
            newTaskItem.classList.add('task');
            newTaskItem.textContent = taskInput;
            taskList.appendChild(newTaskItem);
            // document.getElementById('taskInput').value = ''; // Clear input field
            location.reload();
            // scrollToBottom();

            // localStorage.setItem('isActive', 'true');
        }
    })
    .catch(error => console.error('Error:', error));
});

document.addEventListener('DOMContentLoaded', (event) => {
    scrollToBottom();
});