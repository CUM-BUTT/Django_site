

window.onload = init;

function init(){
    var button = document.getElementById("send_button");
    button.onclick = handleButtonClick;
}


function PasswordCorrect(password)
{
  var digits = /[0-9]+/g.test(password); 
  var simbol = /[a-z]+/g.test(password);
  var big_simbol = /[A-Z]+/g.test(password);
  var something = /[()*+.<>?[\]^{|}]+/g.test(password);
  var lenght = /.{8,}/g.test(password);
  var pass_valid = (lenght & something & big_simbol & simbol & digits);
  alert(digits+ '\n' +
  simbol+ '\n'+
  big_simbol + '\n'+
  something+ '\n'+
  lenght + '\n'+
  pass_valid+ '\n');
  return pass_valid;
}

function handleButtonClick()
{
    var reg_name = new RegExp("[А-Я][а-я]{1,15}\s[А-Я][а-я]{1,15}\s[А-Я][а-я]{1,15}");
    var reg_password = new RegExp("[0-9]{5,15}");

    var login = document.getElementById("login").value;
    var password = document.getElementById("password").value;
    var age = document.getElementById("age").value;

    var age_valid = (age>=0 && age <= 150);
    var name_valid = reg_name.test(login);
    var pass_valid = PasswordCorrect(password);
    
    alert(PasswordCorrect(password));
}


/*window.onload = function()
{
  var send_button = document.getElementById("send_button")
  var password = document.password;
  console.log(send_button);
}*/