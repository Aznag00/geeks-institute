const grid = document.getElementById("grid");
const colorsContainer = document.getElementById("colors");
const clearBtn = document.getElementById("clearBtn");

let mouseDown = false;
let selectedColor = "#000000";
document.body.onmousedown = () => (mouseDown = true);
document.body.onmouseup = () => (mouseDown = false);

const colors = [
  "#000000",
  "#FF0000",
  "#00FF00",
  "#0000FF",
  "#FFFF00",
  "#FF00FF",
  "#00FFFF",
  "#FFA500",
  "#800080",
  "#808000",
  "#008080",
  "#C0C0C0",
  "#800000",
  "#008000",
  "#000080",
  "#FFC0CB",
  "#FFD700",
  "#A52A2A",
  "#F5DEB3",
  "#808080",
  "#ADD8E6",
];

colors.forEach((color) => {
  const colorBox = document.createElement("div");
  colorBox.classList.add("color-box");
  colorBox.style.backgroundColor = color;

  colorBox.addEventListener("click", () => {
    selectedColor = color;
    document
      .querySelectorAll(".color-box")
      .forEach((box) => box.classList.remove("selected"));
    colorBox.classList.add("selected");
  });

  colorsContainer.appendChild(colorBox);
});

colorsContainer.firstChild.classList.add("selected");

const gridSize = 32;
for (let i = 0; i < gridSize * gridSize; i++) {
  const square = document.createElement("div");
  square.classList.add("square");
  square.addEventListener("mouseover", () => {
    if (mouseDown) square.style.backgroundColor = selectedColor;
  });
  square.addEventListener("mousedown", () => {
    square.style.backgroundColor = selectedColor;
  });

  grid.appendChild(square);
}
clearBtn.addEventListener("click", () => {
  document
    .querySelectorAll(".square")
    .forEach((sq) => (sq.style.backgroundColor = "white"));
});
