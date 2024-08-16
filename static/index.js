const menuToggle=document.querySelector('.menuToggle');

    menuToggle.onclick = function() 
    {
        scrollToBottom()
        menuToggle.classList.toggle('active')
    }

    if (localStorage.getItem('isActive') === 'true') {
        menuToggle.classList.toggle('active');
        const input = document.getElementById('inputValue');
            input.focus();
      
    }
    
const closeContainer = document.querySelector('.closeContainer');
    closeContainer.onclick = function() {
        menuToggle.classList.remove('active')
    }

    function scrollToBottom() {
        const container = document.getElementById('secondary-div');
        container.scrollTop = container.scrollHeight;
    }

document.addEventListener('DOMContentLoaded', (event) => {

        scrollToBottom();
        menuToggle.classList.toggle('active')
        const form = document.getElementById('myForm');
        const input = document.getElementById('inputValue');
    
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent actual form submission
            // Perform form submission logic here
            // Refocus on the input field
            input.value = ''; // Clear the input field if needed
        });
        input.focus();
});


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
            taskList.appendChild(newTaskItem)
            // location.reload();
            // window.location.href = "/";
            setTimeout(() => {
                location.reload();
            }, 2000);
            
        }
    })
    .catch(error => console.error('Error:', error));
});


