function SearchByName() {
    // Declare variables
    let input, filter, ul, li, a, i, nargiz = 0;
    input = document.getElementById("searchText");
    filter = input.value.toUpperCase();
    ul = document.getElementById("search-by-name-result");
    li = ul.getElementsByTagName("li");


    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            nargiz += 1;
            ul.style.display = "block";
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";

        }
    }



    if (!filter && ul.style.display !== 'none') {
        console.log(ul.style.display)
        ul.style.display = 'none'
        console.log('bosh')
    }
}

function SearchByNameExit() {
    let ul
    ul = document.getElementById("search-by-name-result");
    ul.style.display = 'none'
}