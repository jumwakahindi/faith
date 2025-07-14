const display=document.getElementById("display");
const buttons=document.querySelectorAll("button");
buttons.forEach(button=>{
    button.addEventListener("click" ,()=>{
        const value=button.textContent;
        if(value=="C"){
            display.value="";
        }
        else if(value=="="){
            try{
                display.value=eval(display.value.replace(/÷/g,"/"));
            }catch{
                display.value="Error";
            }
        }else if (value=="⌫"){
            display.value=display.value.slice(0,-1);
        }else{
            display.value+=value;
         }
    });
});