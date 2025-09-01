// ===== Exercise 1

const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
colors.forEach((value, index) =>
  console.log(`${index + 1}# choice is ${value}`)
);

colors.some((value) => {
  value == "Violet" ? console.log("yeah") : console.log("no");
});

// ===== Exercise 2
const color = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th", "st", "nd", "rd"];

color.forEach((value, index) => {
  let position = index + 1;

  let suffix =
    position % 10 === 1 && position !== 11
      ? ordinal[1]
      : position % 10 === 2 && position !== 12
      ? ordinal[2]
      : position % 10 === 3 && position !== 13
      ? ordinal[3]
      : ordinal[0];

  console.log(`${position}${suffix} choice is ${value}`);
});

// ===== Exercise 3

const fruits = ["apple", "orange"];
const vegetables = ["carrot", "potato"];

const result = ["bread", ...vegetables, "chicken", ...fruits];
console.log(result);
// the output would be like [ 'bread', 'carrot', 'potato', 'chicken', 'apple', 'orange' ]
const country = "USA";
console.log([...country]);
// the output would be like [ 'U', 'S', 'A' ]

let newArray = [...[, ,]];
console.log(newArray);
// the output would be like [ undefined, undefined ]

// ===== Exercise 4
const users = [
  { firstName: "Bradley", lastName: "Bouley", role: "Full Stack Resident" },
  { firstName: "Chloe", lastName: "Alnaji", role: "Full Stack Resident" },
  { firstName: "Jonathan", lastName: "Baughn", role: "Enterprise Instructor" },
  { firstName: "Michael", lastName: "Herman", role: "Lead Instructor" },
  { firstName: "Robert", lastName: "Hajek", role: "Full Stack Resident" },
  { firstName: "Wes", lastName: "Reid", role: "Instructor" },
  { firstName: "Zach", lastName: "Klabunde", role: "Instructor" },
];

const welcomeStudents = users.map((value) => `hello ${value.firstName}`);
console.log(welcomeStudents);

const filtredUsers = users.filter(
  (user) => user.role === "Full Stack Resident"
);
console.log(filtredUsers);

const fullStackLastNames = users
  .filter((user) => user.role === "Full Stack Resident")
  .map((user) => user.lastName);

console.log(fullStackLastNames);

// ===== Exercise 5
const epic = ["a", "long", "time", "ago", "in a", "galaxy", "far far", "away"];
const fullEpic = epic.reduce((acc, val) => acc + " " + val);
console.log(fullEpic);

// ===== Exercise 6
const students = [
  { name: "Ray", course: "Computer Science", isPassed: true },
  { name: "Liam", course: "Computer Science", isPassed: false },
  { name: "Jenner", course: "Information Technology", isPassed: true },
  { name: "Marco", course: "Robotics", isPassed: true },
  { name: "Kimberly", course: "Artificial Intelligence", isPassed: false },
  { name: "Jamie", course: "Big Data", isPassed: false },
];
const passedStudents = students.filter((value) => value.isPassed == true);
console.log(passedStudents);

const congratulations = passedStudents.forEach((e) =>
  console.log(`Good job ${e.name}, you passed the course in ${e.course}`)
);
