function IfUserLoaded()
{
        if (document.readyState != "complete")
        {
            setTimeout(IfUserLoaded, 100);
        }
        if (document.readyState == "Completed Content")
        {
            document.addEventListener("DOMContentLoaded: " + document.getElementById("domContentLoaded").innerHTML);
        }
        else
        {
            document.addEventListener("DOMContentLoaded", IfUserLoaded);
            console.log("DOMContentLoaded: " + document.readyState);
        }
}

IfUserLoaded();