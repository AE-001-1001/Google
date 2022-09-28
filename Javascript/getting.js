
function Getter(x){
    a = new Request(x)
    for (var i=0;i<10;i++)
        console.log(i,a)
    return a
}
Getter('https://www.google.com/')