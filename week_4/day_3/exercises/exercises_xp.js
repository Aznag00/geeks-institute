// ===== Exercise 1
const person = {
  name: "John Doe",
  age: 25,
  location: {
    country: "Canada",
    city: "Vancouver",
    coordinates: [49.2827, -123.1207],
  },
};

const {
  name,
  location: {
    country,
    city,
    coordinates: [lat, lng],
  },
} = person;

console.log(
  `I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`
);
// the output woould be like : I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)

// ===== Exercise 2

function displayStudentInfo(objUser) {
  const { first, last } = objUser;
  console.log(`Your full name is ${first} ${last}`);
}

displayStudentInfo({ first: "Elie", last: "Schoppik" });

// ===== Exercise 3
const users = { user1: 18273, user2: 92833, user3: 90315 };
const users_array = Object.entries(users);
console.log(users_array);

const multipling = users_array.map(([user, id]) => [user, id * 2]);
console.log(multipling);

// ===== Exercise 4
class Person {
  constructor(name) {
    this.name = name;
  }
}

const member = new Person("John");
console.log(typeof member);
// the output wouldbe like : object

// ===== Exercise 5
class Dog {
  constructor(name) {
    this.name = name;
  }
}

class Labrador extends Dog {
  constructor(name, size) {
    super(name);
    this.size = size;
  }
}

// ===== Exercise 6

const object1 = { number: 5 };
const object2 = object1;
const object3 = object2;
const object4 = { number: 5 };

object1.number = 4;
console.log(object2.number); // 4,  because the reference value of that variable is same as object1, so if we change the value of any of them , the changes will impact the other varibales
console.log(object3.number); // 4, because the reference value of that variable is same as object1 and object2
console.log(object4.number); // 5

class Animal {
  constructor(name, type, color) {
    this.name = name;
    this.type = type;
    this.color = color;
  }
}

class Mammal extends Animal {
  sound(noise) {
    return `${noise} i am a ${this.type}, named ${this.name} and i'm ${this.color}`;
  }
}

const farmerCow = new Mammal("Lily", "cow", "brown and white");

console.log(farmerCow.sound("Moooo"));
