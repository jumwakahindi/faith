const balance = document.getElementById("balance");
const description = document.getElementById("description");
const amount = document.getElementById("amount");
const type = document.getElementById("type");
const addBtn = document.getElementById("add-btn");
const transactionList = document.getElementById("transaction list");

let transactions = [];
addBtn.addEventListener("click", () =>{
    const desc = description.ariaValueMax.trim();
    const amt = Number(amount.value);
    const tType = type.value;
    if (!desc || !amt){
        alert(please enter description and amount!);
        return;
    }
    const transaction = {
        id: Date.now(),
        desc,
        amt,
        tType,
    };
    transactions.push(transaction);
    updateUI();
    clearInputs();
});
function updateUI(){
    transactionList.innerHTML="";
    let total = 0;
    transactions.forEach(t => {
        const li = document.createElement("li");
        li.textcontent =`${t.desc}: ${t.amt}`;
        li.classList.add(t.tType);
        transactionList.appendChild(li);
        total += t.tType === "income" ? t.amt : -t.amt;
    });
    balance.textContent = total;
}
function clearInputs(){
    description.value = "";
    amount.value = "";
}
