# CLICKFURY
#### Video Demo:  <https://youtu.be/1fUrZfC1nuw>
#### Description: This is the discription of my small project

## Introduction

I am Rohith a student of CS50 from Hyderabad, India. I made my project 
`ClickFury` in `flask` in which we I have to click the click me button in the least time and consistency is the most important thing in the game.

You can select your game levels too which will help you if you feel the game hard to play.

You see Dark mode is necessity in the modren time I have got you covered, there is dark mode too and it will be saved to cookies but beware you can't change theme in between the game.

What about score it is shown automatically once you lose the game or you click on SCORE once the game starts.

And finally, you can see your best time in seconds.

Ok and let's go to game and play it . . .

## Why I made it

When I learned typing my teacher used to say computer should be a part of you, I thought it was funny until I learnt to touch type I felt like keyboard is a part of me and then thought, why can't one make mouse their own part? So, I went to research I found none so I made this project.

I know many of you will be like why would we ever learn using a mouse? David sir said that programmers use keyboard shortcuts  instead of mouse? In a way you are right but learning another skill is very much productive especially if you're a gamer or designer. 

Ok let's get into details of the project Thank you.

## How it Works

- ***Languages used:*** It uses Python (flask), JavaScript, HTML, CSS etc.

- ***Front-end:*** My project's frontend consists only of design in HTML, style in CSS and timer in JS along with some dynamic js. I also used [Bootstrap 5](https://getbootstrap.com/) and some fonts and icons from [Google fonts](https://fonts.google.com/)

- ***Back-end:*** My backend is made totally on FLASK it is the one responsible for showing best score average score comments in analysis etc. it is mostly used as it is practically very hard to hack, I don't want my web-site to have large number of vulnerabilities and breaches hence I didn't used traditional methods

Counter works by the following method in front-end using recursion:
```js
function upd_timer(time)
{
    time = parseFloat(time)
    document.getElementById("timer").innerHTML = (time - i).toFixed(1)
    if (i <= time)
    {
        setTimeout(upd_timer, 100, time)
        // Calls itself if the input time is more than the time passed
    }
    else
    {
        document.getElementById("timer").innerHTML = "Time out"
        document.getElementById("timerdiv").style.scale = "500%"
        document.getElementById("timerdiv").style.opacity = "0.9"
        document.body.style.backgroundColor = "red"
        document.getElementById("reload").disabled = true
        document.body.style.cursor = "pointer"
        setTimeout(redirect,500)
        // Else it shows time out
    }
    i += 0.1
}
``` 
In back-end it is with the ```datetime.datetime.now()``` function.

And data is stored into cookies by the same manner as CS50 last project like this 
```python
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'afknfkghjnasdjh'
Session(app)
```

then there is an issue I can only initialize it inside app so I have to add another route and rest is in the comments.

finnally I felt login and db is too much for such a simple project 

# Thank You

Any issues or changes are welcomed