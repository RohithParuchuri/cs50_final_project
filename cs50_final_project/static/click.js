let i = 0 
// Initializes a variable to count seconds passed

function redirect()
{
    window.location = "/profile"
}
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

function clicks(x, y, c)
{
    document.body.style.cursor = c
    document.getElementById("reload").style.display = "block"

    // Takes the button that calls the route to the random location
    document.getElementById("reload").style.marginLeft = x
    document.getElementById("reload").style.marginTop = y
    // Changes the name of the button

    document.getElementById("reload").innerHTML = "click me!" 
}
function modeclick(i)
{
    if (i == 'dark')
    {
        document.getElementById("timer").style.color = "white"
        document.getElementById("timer").style.textShadow = "none"
        document.body.style.backgroundColor = "rgb(32, 33, 36)"
    }
    else if (i == 'light')
    {
        document.getElementById("timer").style.color = "black"
    }
}