const message = (x) => 
{
    const Pie = Math.PI/100;
    const Random = Math.random();
    const both = Pie+Random;
        console.debug(`${Random}\n${Pie}`)
    return (both/x);
}

async function generateMessage(x)
{
    const msg = [message(x)];
    for (let m of msg)
    {
        msg.slice(m.toString().length, m.toString().length);
    }
    return console.log(msg);
}

function Main(t,y)
{
    const data = {generatedMessage: generateMessage(t),generateMessage: generateMessage(y)}
    return console.log(data.generatedMessage.finally());
}

Main(1,1);