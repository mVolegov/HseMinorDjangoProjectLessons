function verify() {
    let car_price = parseInt(document.getElementsByTagName("input")[1].value);
    let period = parseInt(document.getElementsByTagName("input")[2].value);
    let interest_rate = parseFloat(document.getElementsByTagName("input")[3].value);

    const month_interest_rate = interest_rate / 100 / 12
    console.log(month_interest_rate)
    result =
        ((month_interest_rate * (1 + month_interest_rate) ** period)
            / ((month_interest_rate + 1) ** period - 1)) * car_price

    document.getElementById("result").innerText = messageText + " " + result + ".руб"
    console.log(car_price, period, interest_rate, result)
    check = true
}

function send() {
    if (check) {
        let textCondition = document.getElementsByTagName('p')[0].innerText
        document.getElementsByName('q')[0].value = textCondition;
        document.getElementsByName('result')[0].value = result;
        document.getElementById("UserEnter").submit();
    } else {
        alert("Есть недостатки. Повторите ввод")
    }
}

function verify_send() {
    verify();
    send();
}


let messageText = document.getElementById("result").innerText
let result;
let check = false;


const elementA = document.getElementById("car_price");
elementA.addEventListener('keyup', verify);
const elementB = document.getElementById("period");
elementB.addEventListener('keyup', verify);
const elementC = document.getElementById("interest_rate");
elementC.addEventListener('keyup', verify);

const verifyAll = document.getElementById("verify");
verifyAll.addEventListener('click', verify)

const elementSend = document.getElementById("send");
elementSend.addEventListener('click', send)