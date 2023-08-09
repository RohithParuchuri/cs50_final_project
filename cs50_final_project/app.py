from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from random import randint
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "afknfkghjnasdjh"
Session(app)


# Initialize the variables
click = 0
level = 0
mode = 0


# It will be loaded
time = []
time.append(0)

# Initialize the variables
timesum = 0
time_least = 404
timegiven = [0, 30]

i = randint(0, 90)
j = randint(0, 80)


@app.route("/")
def sessonroute():
    # Checks if there were any cookies

    if not session.get("mode"):
        session["mode"] = "light"
    if not session.get("best"):
        session["best"] = "0"
    return redirect("/index")


@app.route("/index", methods=["POST", "GET"])
def home():
    # If device are in following it rejects the device
    # I can't use or as I want device name too
    global mode

    agent = request.headers.get("User-Agent")
    print(agent)
    if "iphone" in agent.lower():
        device = "iPhones"
        return render_template("sorry.html", device=device)
    elif "android" in agent.lower():
        device = "Android Devices"
        return render_template("sorry.html", device=device)
    elif "blackberry" in agent.lower():
        device = "Blackberries"
        return render_template("sorry.html", device=device)
    elif "ipad" in agent.lower():
        device = "iPads"
        return render_template("sorry.html", device=device)
    else:
        print(str(session["mode"]) + "hello")
        return render_template("index.html", mode=session["mode"])


@app.route("/clicks", methods=["POST", "GET"])
def clicks():
    # Initializes variables as globa
    global i, j, click, time, timesum, level, time_least, timegiven, mode
    cursor = "none"
    name = ""
    name = request.form.get("click_button")
    # Sets the variable on the click of start button
    if name == "Starts":
        time[0] = datetime.now()
        level = 2
    elif name == "1":
        time[0] = datetime.now()
        level = 1
    elif name == "2":
        time[0] = datetime.now()
        level = 2
    elif name == "3":
        time[0] = datetime.now()
        level = 3

    # Changes the variables everytime we click the click me! buttom
    elif request.method == "POST":
        click += 1
        if len(time) < 2:
            time.append(datetime.now())
        else:
            time[0] = time[1]
            time[1] = datetime.now()
        timetaken = time[1] - time[0]

        # Dynamic change of hardness, timelimit of the game
        if timegiven[0] < 3 - level:
            timegiven[0] += 1
        else:
            timegiven[1] = timegiven[1] / (1 + level / 10)
            timegiven[0] = 0

        # Summation of the timetaken
        timesec = float(timetaken.total_seconds())
        timesum += timesec

        # Gets the least time taken
        if float(timesec) < float(time_least):
            time_least = timesec
        timesec = 0

        # gets random values for X and Y coordinates
        i = randint(1, 90)
        j = randint(1, 90)
        return redirect("/clicks")

    return render_template(
        "clicks.html",
        i=i,
        j=j,
        cursor=cursor,
        clicks=click,
        timegiven=timegiven[1],
        mode=session["mode"],
    )


@app.route("/profile", methods=["POST", "GET"])
def profile():
    # Initializes variables as global
    global click, time_least, timegiven, timesum, time, level

    # Normalizes the hardness
    if level == 1:
        factor = 4
    if level == 2:
        factor = 2
    if level == 3:
        factor = 1

    # Checks and GIVES review
    if click in range(3, (6 * factor) // 2):
        reaction = "Ok!"
    elif click in range((6 * factor) // 2, (15 * factor) // 2):
        reaction = "Very good!"
    elif click in range((15 * factor) // 2, (25 * factor) // 2):
        reaction = "Excellent!!!!!"
    elif click > (25 * factor) // 2:
        reaction = "OutStanding!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    else:
        reaction = "needs improvement"

    # Initalizes variables to new
    # And deletes old variables
    count = click
    click = 0
    mintime = time_least
    time_least = 404
    timesum2 = timesum
    timesum = 0

    if mintime != 0 and session["best"] != "0" and mintime < float(session["best"]):
        session["best"] = str(round(mintime, 2))
    elif session["best"] == "0":
        session["best"] = str(mintime)

    # Resets the list to Initial state
    timegiven[1] = 30
    timegiven[0] = 0

    # Removes old variable list
    time.clear()

    # Adds New element for /clicks to edit
    time.append(datetime.now())

    # Generates the average to be displayed
    if count != 0:
        timeave = timesum2 / count
    else:
        timeave = 0.00

    return render_template(
        "profile.html",
        click=count,
        timesum=timesum,
        reaction=reaction,
        timesec=round(timeave, 2),
        least_time=round(mintime, 2),
        best=session["best"],
    )


@app.route("/theme")
def changer():
    global mode
    if mode == 0 and session["mode"] == "light":
        mode = 1
        session["mode"] = "dark"
    else:
        mode = 0
        session["mode"] = "light"
    return redirect("/")


@app.route("/best")
def top():
    if session["best"] != "0":
        best = session["best"]
    else:
        best = "Play a Game"
    return render_template("best.html", best=best)


@app.route("/TypeFury")
def typefury():
    # TODO: type fury
    return redirect("/")
