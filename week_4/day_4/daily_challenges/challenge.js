const form = document.querySelector("form");
const output = document.getElementById("output");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = form.elements["name"].value;
  const lastname = form.elements["lastname"].value;

  const jsonData = { name: name, lastName: lastname };

  output.textContent = JSON.stringify(jsonData, null, 2);
  console.log(jsonData);
});
