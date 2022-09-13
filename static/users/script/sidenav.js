/* Set the width of the side navigation to 250px and the left margin of the page content to 250px */
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

function toggleNav() {
  if (document.getElementById("mySidenav").style.width === "250px") {
    document.getElementById("mySidenav").style.width = "0px";
  }
  else {
    document.getElementById("mySidenav").style.width = "250px";
  }
}