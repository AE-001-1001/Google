const message = (x) => 
{
    const Pie = Math.PI/100;
    const Random = Math.random()*10;
    const both = Pie+Random;
    if (Random <= 5)
    {
        return both
    }
        console.debug(`${Random}`)
    return (both/x);
}

async function generateMessage(x)
{
    const msg = [message(x)];
    for (let m of msg)
    {
        msg.slice(m.toString().length, m.toString().length);
    }
    return (msg);
}

function MainApp(t,y)
{
    const data = {
        generatedMessage: generateMessage(t),
        generateMessage: generateMessage(y)
    }
    return (data.generatedMessage);
}

function RunApp(t,y,r,o)
    {
    const TimeHeader = (r) =>
    {
        const date = new Date(Date.now());
        {
            console.log("Time(s) Ran:" + r);
        }
        return console.log(date);
    }
    const data = (o) => 
    {
    for (var m = 0; m < r ; m++)
        {
        MainApp(t,y)
        }
    if (o >= 'Hello')
        {
        console.log("Confirmed",o)
        }
        return data;
    } 
    return (data(o), TimeHeader(r));
}

RunApp(1,2,25,'Hello')