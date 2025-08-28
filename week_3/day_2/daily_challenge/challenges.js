// ====== Daily Challenge 1

const sentence = "this exercise is not bad";

const wordNot = sentence.indexOf("not");
const wordBad = sentence.indexOf("bad");

if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
  const newSentence =
    sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
  console.log(newSentence);
} else {
  console.log(sentence);
}
// ====== Daily Challenge 2

// ====== Daily Challenge 3
