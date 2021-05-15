//Get the button:
mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
} 

function hover(element, link) {
  const country_code = link.split("/")[3];
  element.children('.logo').setAttribute('src', `https://www.countryflags.io/${country_code}/shiny/16.png`);
}

function unhover(element, link) {
  const country_code = link.split("/")[3];
  element.children('.logo').setAttribute('src', `https://www.countryflags.io/${country_code}/flat/16.png`);
}