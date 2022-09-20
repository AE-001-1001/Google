async function testCapabilities(Value)
{
    const WhatType = typeof String === "string" ? "float" : "number" ? "boolean" : "number";
    const Capabilities = typeof String === "string" ? ["string", "number","float","boolean"] : ["string", "number","float", "boolean"];
    const returnValue = Boolean(Value);

    for (let i = 0 ; i < Capabilities.length; i++) 
    {
        const cap = [Capabilities[i].split("").join(" ")];
        console.debug(cap);
    for (let type of Capabilities)
    {
        const capa = [
                    type.replace("string","Changed").trim(),
                    type.replace("boolean", "Changed").trim(),
                    type.replace("Changed", "boolean").trim()
                    ];
        const capg = [Capabilities[i].split("").join(" "), " ",capa];
        console.log(capg.join(type));
    }
}
   await returnValue;
return returnValue;
}

function init(x)
{
    for( let i = 0 ; i < x.length ; i++ )
    {
        console.log(x[i]);
    }
    return x;
}

async function Main(x)
{
    init(x)
    testCapabilities(x);
    return 0;
}
Main(12)