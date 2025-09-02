function isAnagram(arg1, arg2) {
  const normalize = (str) =>
    str.replace(/\s+/g, "").toLowerCase().split("").sort().join("");

  return normalize(arg1) === normalize(arg2);
}

console.log(isAnagram("Astronomer", "Moon starer"));
console.log(isAnagram("School master", "The classroom"));
console.log(isAnagram("The Morse Code", "Here come dots"));
