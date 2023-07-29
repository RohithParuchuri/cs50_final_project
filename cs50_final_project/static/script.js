function mode(i){
    if (i == 'dark'){
        document.body.style.backgroundColor = 'rgb(32, 33, 36)'
        document.getElementById("navbar").style.backgroundColor = 'rgb(48, 48, 48)'
        document.getElementById("navbar").style.boxShadow = 'none'
        document.getElementById("clickmetext").style.color = 'white'  
        document.getElementById("homeicon").src = '../static/home_white_24dp.svg'
        document.getElementById("themeicon").src = '../static/light_mode_white_24dp.svg'
    }
    else if (i == 'light'){
        document.body.style.backgroundColor = 'white'
        document.getElementById("navbar").style.backgroundColor = 'white'
        document.getElementById("navbar").style.boxShadow = '0.2px 0.2px 10px dimgray'
        document.getElementById("clickmetext").style.color = 'black'
        document.getElementById("homeicon").src = '../static/home_black_24dp.svg'
        document.getElementById("themeicon").src = '../static/dark_mode_black_24dp.svg'
    }
}

function route()
{
    setTimeout(() => {
        window.location = "/"
    }, 200);
}