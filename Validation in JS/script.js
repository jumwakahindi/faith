const form = document.getElementById("loginform");
form.addEventListener('submit', function(event){
    event.preventDefault();
    if (form.checkValidity()){
        window.location.href ="dashboard.html";
    }
    else{
        form.classList.add('was-validated');
    }
});