let client = "John";

const groceries = {
  fruits: ["pear", "apple", "banana"],
  vegetables: ["tomatoes", "cucumber", "salad"],
  totalPrice: "20$",
  other: {
    paid: true,
    meansOfPayment: ["cash", "creditCard"],
  },
};

const displayGroceries = () => console.log(groceries.fruits);
displayGroceries();

const cloneGroceries = () => {
  const user = client;
  client = "Betty";
  console.log(user); // we will not see the modification in the user variable, because its value is primitive so when we asign it to new varibale; we copy the actual value that doesn't impact with changes of other variable

  const shopping = groceries;
  groceries.totalPrice = "35$";
  groceries.other.paid = false;
  console.log(shopping);
  // we will see the modification in the shopping variable, because its value is reference so when we asign it to new varibale; we copy the reference or the adress of the actual value.so any changes of any variable will occur on the other
};

cloneGroceries();
