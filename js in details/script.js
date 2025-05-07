const handleSubmit = e => {

    e.preventDefault();
    
    const name = document.getElementById("name").value;
    
    const age = document.getElementById("age").value;
    
    const message = document.getElementById("message");
    
    let error = !name ? "Please enter your name." :
    
    isNaN(age) ? "Age must be a number." :
    
    age <= 0 ? "Age must be greater than 0." : "";
    
    message.innerHTML = error
    
    ? `<div class="alert alert-danger">${error}</div>`
    
    : `<div class="alert alert-info">Hello ${name}, you are ${age} years old!</div>`;
    
    };
    
    document.getElementById("userform").addEventListener("submit", handleSubmit);
