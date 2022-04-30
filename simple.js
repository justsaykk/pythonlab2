// Example of a callback function

const function1 = (x) => {
  const string = "Hello " + x;
  console.log(string);
};

const function2 = (callback) => {
  const x = "Kitty";
  callback(x);
};

function2(function1);

// JS Data Structures
const names = ["John", "Jane", "Mary"];
const car = { type: "Fiat", model: "500", color: "white" };

console.log(car); // Generic log
const keys = Object.keys(car);
const values = Object.values(car);
const keyValuePair = Object.entries(car);
// OR
for (const el in car) {
  const value = car[el];
  console.log(el, value);
}
