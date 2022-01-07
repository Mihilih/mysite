//to edit a jounral entry
function editjournal(id) {
    document.querySelector(`#edit_journal${id}`).style.display ='';
    document.querySelector(`#journal${id}`).style.display = 'none';
}

//to edit a book entry
function editbook(id) {
    document.querySelector(`#edit_book${id}`).style.display ='';
    document.querySelector(`#book${id}`).style.display = 'none';
}

//to edit a patent entry
function editpatent(id) {
    document.querySelector(`#edit_patent${id}`).style.display ='';
    document.querySelector(`#patent${id}`).style.display = 'none';
}

//to edit a grant entry
function editgrant(id) {
    document.querySelector(`#edit_grant${id}`).style.display ='';
    document.querySelector(`#grant${id}`).style.display = 'none';
}

//to edit an award entry
function editaward(id) {
    document.querySelector(`#edit_award${id}`).style.display ='';
    document.querySelector(`#award${id}`).style.display = 'none';
}


//to delete an journal entry
function deletejournal(id) {
   if(confirm("This journal record will be deleted.")==true){
        location.href=`/deletejournal/${id}`
   }
    
}

//to delete an book entry
function deletebook(id) {
    if(confirm("This book record will be deleted.")==true){
        location.href=`/deletebook/${id}`
   }   
}
//to delete an patent entry
function deletepatent(id) {
    if(confirm("This patent record will be deleted.")==true){
        location.href=`/deletepatent/${id}`
    }   
}
//to delete an grant entry
function deletegrant(id) {
    if(confirm("This grant record will be deleted.")==true){
        location.href=`/deletegrant/${id}`
    }   
}
//to delete an award entry
function deleteaward(id) {
    if(confirm("This award record will be deleted.")==true){
        location.href=`/deleteaward/${id}`
    }    
}