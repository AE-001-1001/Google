
function Greeting(){
    console.log('Hello world');
    return Greeting;
}

function numbers()
{
    numbers = [
        1,2,
        2,3,
        3,4,
        4,5,
        5,6,
        6,7,
        7,8,
        8,9,
        9,10,
        10,11,
        11,12,
        12,13,
        13,14
    ]
    return numbers;
}

function USERDATA() {
    userdata = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@gmail.com",
        "password": "123456"
    },
    {
        "id": 2,
        "name": "Jane Doe",
        "email": "jane.doe@gmail.com",
        "password": "123456"
    }
    ];
    return userdata;
}

console.log(USERDATA(),numbers(),Greeting());