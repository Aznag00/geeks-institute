// ===== Exercise 1
function funcOne() {
  let a = 5;
  if (a > 1) {
    a = 3;
  }
  console.log(`inside the funcOne function ${a}`);
}

// #1.1 - run in the console:
funcOne();
// output: a = 3

// #1.2 What if const instead of let?
// If we declare a with const, it cannot be reassigned.
// So `a = 3;` will throw an error

//#2
let a = 0;
function funcTwo() {
  a = 5;
}

function funcThree() {
  console.log(`inside the funcThree function ${a}`);
}

// #2.1 - run in the console:
funcThree(); // a = 0
funcTwo();
funcThree(); // a = 5
// Explanation:
// - a is a global variable. funcThree reads its value, initially 0
// - funcTwo modifies the global a to 5
// - next call to funcThree prints 5

// #2.2 What if const instead of let?
// If a is declared as const funcTwo cannot reassign it
// It will throw an error

//#3
function funcFour() {
  window.a = "hello";
}

function funcFive() {
  console.log(`inside the funcFive function ${a}`);
}

// #3.1 - run in the console (browser only):
funcFour();
funcFive();
// output : a = "hello"
// Explanation: funcFour adds 'a' as a property of the window object (global scope in browser)
// funcFive accesses global 'a', prints "hello".

//#4
let a = 1;
function funcSix() {
  let a = "test";
  console.log(`inside the funcSix function ${a}`);
}

// #4.1 - run in the console:
funcSix();
// output: a = "test"
// Explanation: funcSix has a local variable a, which shadows the outer a. So "test" is printed

// #4.2 What if const instead of let?
// Same behavior: a local constant a = "test" works fine, prints "test"
// The outer a = 1 remains unchanged

//#5
let a = 2;
if (true) {
  let a = 5;
  console.log(`in the if block ${a}`);
}
console.log(`outside of the if block ${a}`);

// #5.1 - run the code in the console
// output:
// in the if block: 5
// outside of the if block: 2
// Explanation:
// - The a inside the if block is block-scoped, it does not affect the outer a

// #5.2 What if const instead of let?
// Same behavior: const inside the if block is block-scoped, prints the same values

// ===== Exercise 2

const winBattle = () => true;
const experiencePoints = winBattle() ? 10 : 1;
console.log(experiencePoints);

// ===== Exercise 3
const isString = (value) => typeof value === "string";

console.log(isString("hello"));
console.log(isString([1, 2, 4, 0]));

// ===== Exercise 4
const sum = (x, y) => x + y;

// ===== Exercise 5
function toGrams1(x) {
  return x * 1000;
}
console.log(toGrams1(5));
const toGrams2 = function (kg) {
  return kg * 1000;
};
console.log(toGrams2(7));
const kgToGrams3 = (kg) => kg * 1000;
console.log(kgToGrams3(3));

// ===== Exercise 6
(function (children, partner, location, job) {
  const message = `You will be a ${job} in ${location}, and married to ${partner} with ${children} kids.`;
  document.body.innerHTML += `<p>${message}</p>`;
})(3, "imane", "casablanca", "engineer");

// ===== Exercise 7
(function (username) {
  const navbar = document.getElementById("navbar");
  const userDiv = document.createElement("div");
  userDiv.innerHTML = `
    <img src="https://via.placeholder.com/40" alt="profile" style="border-radius:50%">
    <span>Welcome, ${username}</span>
  `;
  navbar.appendChild(userDiv);
})("John");

// ===== Exercise 8

function makeJuice(size) {
  function addIngredients(ing1, ing2, ing3) {
    const sentence = `The client wants a ${size} juice, containing ${ing1}, ${ing2}, ${ing3}.`;
    document.body.innerHTML += `<p>${sentence}</p>`;
  }

  addIngredients("apple", "banana", "mango");
}
makeJuice("Large");
