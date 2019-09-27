window.onscroll = function() {scrollFunction()};
    
function scrollFunction() {
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
	document.getElementById("topBtn").style.opacity = "1";
  } else {
	document.getElementById("topBtn").style.opacity = "0";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  $('html, body').stop().animate( { scrollTop : 0 } ); 
}