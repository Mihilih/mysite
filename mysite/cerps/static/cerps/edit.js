//to edit a jounral entry
function editjournal(id) {
    
}

//to edit a book entry
function editbook(id) {
    
}

//to edit a patent entry
function editpatent(id) {
    
}

//to edit a grant entry
function editgrant(id) {
    
}

//to edit an award entry
function editaward(id) {
    
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