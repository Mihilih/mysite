//to edit a jounral entry
function editjournal(id) {
    document.querySelector(`#edit_journal${id}`).style.display ='';
    document.querySelector(`#journal${id}`).style.display = 'none';

    document.querySelector(`#edit_journal_${id}`).addEventListener('click', () => {
        fetch('/editjournal/' + id, {
            method: 'PUT',
            body: JSON.stringify({
                name: document.querySelector(`#edit_journal_name_${id}`).value,
                title: document.querySelector(`#edit_journal_title_${id}`).value,
                authors:document.querySelector(`#edit_journal_author_${id}`).value,
                volume:document.querySelector(`#edit_journal_volume_${id}`).value,
                issue:document.querySelector(`#edit_journal_issue_${id}`).value,
                pages:document.querySelector(`#edit_journal_pages_${id}`).value
            })
          })
          
          setTimeout(function() {
          reload(); 
          }, 1000);
          function reload(){
            window.location ="view";
          }
    });
}

//to edit a book entry
function editbook(id) {
    document.querySelector(`#edit_book${id}`).style.display ='';
    document.querySelector(`#book${id}`).style.display = 'none';

    document.querySelector(`#edit_book_${id}`).addEventListener('click', () => {
        fetch('/editbook/' + id, {
            method: 'PUT',
            body: JSON.stringify({
                bool: document.querySelector(`#edit_book_bool_${id}`).value,
                book_title: document.querySelector(`#edit_book_title_${id}`).value,
                chapter_title: document.querySelector(`#edit_book_chapter_title_${id}`).value,
                authors:document.querySelector(`#edit_book_author_${id}`).value,
                year:document.querySelector(`#edit_book_year_${id}`).value,
                publisher:document.querySelector(`#edit_book_publisher_${id}`).value,
                isbn:document.querySelector(`#edit_book_isbn_${id}`).value
            })
          })
          
          setTimeout(function() {
          reload(); 
          }, 1000);
          function reload(){
            window.location ="view";
          }
    });
}

//to edit a patent entry
function editpatent(id) {
    document.querySelector(`#edit_patent${id}`).style.display ='';
    document.querySelector(`#patent${id}`).style.display = 'none';

    document.querySelector(`#edit_patent_${id}`).addEventListener('click', () => {
        fetch('/editpatent/' + id, {
            method: 'PUT',
            body: JSON.stringify({
                agency: document.querySelector(`#edit_patent_agency_${id}`).value,
                title: document.querySelector(`#edit_patent_title_${id}`).value,
                authors:document.querySelector(`#edit_patent_author_${id}`).value,
                year:document.querySelector(`#edit_patent_year_${id}`).value,
                number:document.querySelector(`#edit_patent_number_${id}`).value,
                isbn:document.querySelector(`#edit_patent_isbn_${id}`).value
            })
          })
          
          setTimeout(function() {
          reload(); 
          }, 1000);
          function reload(){
            window.location ="view";
          }
    });
}

//to edit a grant entry
function editgrant(id) {
    document.querySelector(`#edit_grant${id}`).style.display ='';
    document.querySelector(`#grant${id}`).style.display = 'none';

    document.querySelector(`#edit_grant_${id}`).addEventListener('click', () => {
        fetch('/editgrant/' + id, {
            method: 'PUT',
            body: JSON.stringify({
                agency: document.querySelector(`#edit_grant_agency_${id}`).value,
                title: document.querySelector(`#edit_grant_title_${id}`).value,
                investigators:document.querySelector(`#edit_grant_investigator_${id}`).value,
                pi:document.querySelector(`#edit_grant_pi_${id}`).value,
                budget:document.querySelector(`#edit_grant_budget_${id}`).value,
                from:document.querySelector(`#edit_grant_from_${id}`).value,
                to:document.querySelector(`#edit_grant_to_${id}`).value
            })
          })
          
          setTimeout(function() {
          reload(); 
          }, 1000);
          function reload(){
            window.location ="view";
          }
    });
}

//to edit an award entry
function editaward(id) {
    document.querySelector(`#edit_award${id}`).style.display ='';
    document.querySelector(`#award${id}`).style.display = 'none';

    document.querySelector(`#edit_award_${id}`).addEventListener('click', () => {
        fetch('/editaward/' + id, {
            method: 'PUT',
            body: JSON.stringify({
                name: document.querySelector(`#edit_award_name_${id}`).value,
                award: document.querySelector(`#edit_award_award_${id}`).value,
                year:document.querySelector(`#edit_award_year_${id}`).value,
                agency:document.querySelector(`#edit_award_agency_${id}`).value,
            })
          })
          
          setTimeout(function() {
          reload(); 
          }, 1000);
          function reload(){
            window.location ="view";
          }
    });
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