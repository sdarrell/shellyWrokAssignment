//searchBarInput = document.getElementById("searchBar")
//searchBarInput.addEventListener("input",updateTable)
function updateTable() {
    let input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("searchBarInput");
    filter = input.value.toLowerCase();
    table = document.getElementById("workersTable")
    tr = table.getElementsByTagName("tr")

    for(i=0; i < tr.length; i++) {
        tdId = tr[i].getElementsByTagName("td")[0];
        tdName = tr[i].getElementsByTagName("td")[2];
        if(tdName || tdId){
            textValue = tdId.textContent || tdId.innerText || tdName.textContent || tdName.innerText;
            if(textValue.toLowerCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            }
            else {
                tr[i].style.display = "none";
             }
        }
    }
}