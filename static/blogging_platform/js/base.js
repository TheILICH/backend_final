let user = "";

let front = document.getElementById("front"), back = document.getElementById("back");

let rotate =
    {
        'transform': 'rotateY(180deg)'
    }

let reset =
    {
        'transform': 'rotateY(0deg)'
    }


const Rotate = () =>
{
    Object.assign(front.style, rotate);
    Object.assign(back.style, reset);
}

const Reset = () =>
{
    Object.assign(front.style, reset);
    Object.assign(back.style, rotate);
}

const backSubmit = () =>
{
    let name = document.getElementById("backName").value, surname = document.getElementById("backSurname").value, email = document.getElementById("backEmail").value, password = document.getElementById("backPassword").value, confirm = document.getElementById("backConfirm").value;

    let mails = ['@gmail.com', '@mail.ru', '@stu.sdu.edu.kz'];
    let e = false;
    for (let x of mails) e |= email.endsWith(x);

    let p = password === confirm;

    if (!e)
    {
        alert(`Your email is wrong. It should end with one of the ${mails.join(' ')} Please write your email.`);
    }

    if (!p)
    {
        alert("Your confirmation password doesn't match. Please try again.");
    }

    if (e && p) start();
}

const start = (name) =>
{
    let arr = document.getElementsByClassName("in");
    for (let x of arr) x.value = '';

    alert(`${name}, you're logged in!`);
}


function log_php(uname, pass)
{
    $.ajax(
        {
            url: 'login.php',
            type: 'POST',
            data: {username: uname, password: pass},
            success: function(result)
            {
                console.log(result);
                if (result === "Login!")
                {
                    start(uname);
                    user = uname;
                }
            },
            error: function()
            {
                console.log('login error!');
            }
        }
    )
}


function reg_php(uname, pass, pass_again)
{
    if (pass !== pass_again)
    {
        alert("different password inputs!");
        return;
    }

    $.ajax(
        {
            url: 'register.php',
            type: 'POST',
            data: {username: uname, password: pass},
            success : function (result)
            {
                console.log(result);
                if (result === 'Success!') {alert(`${uname}, you're registered!`)}
                else alert(`Wrong input`);
            },
            error: function()
            {
                console.log('error');
            }
        }
    )
}