// ===== Exercise 1
function displayNumbersDivisible(divisor) {
  for (let i = 0; i < 501; i++) {
    if (i % divisor === 0) {
      console.log(i);
    }
  }
}

displayNumbersDivisible(56);
// ===== Exercise 2

const stock = {
  banana: 6,
  apple: 0,
  pear: 12,
  orange: 32,
  blueberry: 1,
};

const prices = {
  banana: 4,
  apple: 2,
  pear: 1,
  orange: 1.5,
  blueberry: 10,
};
const shoppingList = ["banana", "orange", "apple"];
function myBill() {
  let total = 0;
  for (let i = 0; i < shoppingList.length; i++) {
    if (shoppingList[i] in stock) {
      total += prices[shoppingList[i]];
      stock[shoppingList[i]] -= 1;
    }
  }
  console.log(total);
}
myBill();

// ===== Exercise 3

function changeEnough(itemPrice, amountOfChange) {
  if (amountOfChange > itemPrice) {
    return true;
  } else {
    return false;
  }
}

function changeEnough(itemPrice, amountOfChange) {
  const coinValues = [0.25, 0.1, 0.05, 0.01];
  let totalChange = 0;
  for (let i = 0; i < amountOfChange.length; i++) {
    totalChange += amountOfChange[i] * coinValues[i];
  }

  return totalChange >= itemPrice;
}

console.log(changeEnough(4.25, [25, 20, 5, 0]));

// ===== Exercise 4

function hotelCost() {
  let nights;
  do {
    nights = prompt("How many nights would you like to stay at the hotel?");
  } while (!nights || isNaN(nights));

  return 140 * Number(nights);
}
function planeRideCost() {
  let destination;
  do {
    destination = prompt("What is your destination?");
  } while (!destination || typeof destination !== "string");

  switch (destination.toLowerCase()) {
    case "london":
      return 183;
    case "paris":
      return 220;
    default:
      return 300;
  }
}
function rentalCarCost() {
  let days;
  do {
    days = prompt("How many days would you like to rent the car?");
  } while (!days || isNaN(days));

  let cost = 40 * Number(days);
  if (days > 10) {
    cost *= 0.95;
  }
  return cost;
}

function totalVacationCost() {
  const hotel = hotelCost();
  const plane = planeRideCost();
  const car = rentalCarCost();
  const total = hotel + plane + car;

  console.log(`The car cost: $${car}`);
  console.log(`The hotel cost: $${hotel}`);
  console.log(`The plane tickets cost: $${plane}`);
  console.log(`Total vacation cost: $${total}`);

  return total;
}
totalVacationCost();
