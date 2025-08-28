// ===== Exercise 1
const people = ["Greg", "Mary", "Devon", "James"];
people.shift();
people[people.indexOf("James")] = "Jason";
people.push("Mehdi");
console.log(people.indexOf("Mary"));
const people_copy = people.slice(1, 3);
console.log(people.indexOf("Foo"));
// it does return -1 because that value does not exist in people variable
const last = people[people.length - 1];
for (i = 0; i < people.length; i++) {
  console.log(people[i]);
}

for (i = 0; i < people.length; i++) {
  console.log(people[i]);
  if ((people[i] = "Devon")) break;
}

// ===== Exercise 2
const colors = ["black", "white", "gray", "red"];
for (i = 0; i < colors.length; i++) {
  console.log(`my ${i + 1} choice is ${colors[i]}`);
}
const suffixes = ["st", "nd", "rd", "th", "th"];
for (i = 0; i < colors.length; i++) {
  console.log(`my ${i + 1}${suffixes[i]} choice is ${colors[i]}`);
}
// ===== Exercise 3
let alter_input;
let user_input;

do {
  user_input = prompt("enter a number: ");
  alter_input = Number(user_input);
  if ((alter_input = NaN)) {
    console.log("please enter a valid number");
  } else if (alter_input < 10) {
    console.log("Number is smaller than 10. Please try again.");
  }
} while (isNaN(alter_input) || alter_input < 10);

// ===== Exercise 4
const building = {
  numberOfFloors: 4,
  numberOfAptByFloor: {
    firstFloor: 3,
    secondFloor: 4,
    thirdFloor: 9,
    fourthFloor: 2,
  },
  nameOfTenants: ["Sarah", "Dan", "David"],
  numberOfRoomsAndRent: {
    sarah: [3, 990],
    dan: [4, 1000],
    david: [1, 500],
  },
};

console.log(building.numberOfFloors);
console.log(
  building.numberOfAptByFloor.firstFloor +
    building.numberOfAptByFloor.thirdFloor
);

console.log(
  `the name is ${building.nameOfTenants[1]} and he has ${building.numberOfRoomsAndRent.dan[0]} rooms`
);

const rent_sum =
  building.numberOfRoomsAndRent.sarah[1] +
  building.numberOfRoomsAndRent.david[1];
if (building.numberOfRoomsAndRent.dan[1] < rent_sum) {
  building.numberOfRoomsAndRent.dan[1] = 1200;
}

console.log(building.numberOfRoomsAndRent.dan[1]);

// ===== Exercise 5

const family = {
  name: "geeks",
  members: 25,
  activity: "coding",
};

for (let key in family) {
  console.log(key);
}

for (let value in family) {
  console.log(family[value]);
}

// ===== Exercise 6

const details = {
  my: "name",
  is: "Rudolf",
  the: "reindeer",
};

let sentence = "";
for (let key in details) {
  sentence += key + " " + details[key] + " ";
}
console.log(sentence.trim());

// ===== Exercise 7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
console.log(
  names
    .map((name) => name[0])
    .sort()
    .join("")
);
