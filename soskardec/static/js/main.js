// const date = new Date();
// document.querySelector('.year').innerHTML = date.getFullYear();

window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function(){
        $(this).remove(); 
    });
}, 5000);