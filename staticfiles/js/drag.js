document.getElementById("dragLink").addEventListener("click", function(event) {
  event.preventDefault(); // Prevent default link behavior
  document.querySelector(".content").classList.add("dragged");
});
