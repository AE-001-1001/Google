const docgettter = document.createElement('Images');
const docgettter1 = document.createElement('h1');
const docgettter2 = document.createElement('div');

docgettter.appendChild(docgettter1);
docgettter.appendChild(docgettter2);
docgettter.src = 'Javascript project/life.js';
docgettter.type = 'text/javascript';
docgettter.onload = function() {
    head = (document.getElementsByTagName('head')[0] || document.documentElement);
    body = (document.getElementsByTagName('body')[0]);
    return console.log(head,body)
};

docgettter.onload();

