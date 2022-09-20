function loadDocElement(){
    var doc = document;
    for (let i = 0; i < doc.length; i++){
        doc = doc.elements[i];
    }
    return console.log(doc);
}

loadDocElement();