/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */
function join(arr, separator) {
    //Your code here
}

console.log(join(arr1, separator1)) // Expected: "1, 2, 3"
console.log(join(arr2, separator2)) // Expected: "1-2-3"
console.log(join(arr3, separator3)) // Expected: "1 - 2 - 3"
console.log(join(arr4, separator4)) // Expected: "1"

/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

const str1 = "object oriented programming";
const expectedA = "OOP";

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expectedB = "APIE";

const str3 = "software development life cycle";
const expectedC = "SDLC";

// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expectedD = "GIT";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
 function acronymize(str) {
    //Your code here
}



console.log(acronymize(str1)); // Expected: "OOP"
console.log(acronymize(str2)); // Expected: "APIE"
console.log(acronymize(str3)); // Expected: "SDLC"
console.log(acronymize(str4)); // Expected: "GIT"





















function join(arr, separator) {
  //Your code here
  let joined = "";
  for (let i = 0; i < arr.length; i++) {
      joined += arr[i];
      if (i < arr.length - 1) {
          joined += separator;
      }
  }
  return joined;
}

function acronymize(str) {
  let acronym = "";
  let words = str.split(" ");
  for (let i = 0; i < words.length; i++) {
      if (words[i] !== "") {
          acronym += words[i][0].toUpperCase();
      }
  }
  return acronym;
}

function acronymize2(str) {
  let acronym = "";
  let currentWord = "";
  for (let i = 0; i < str.length; i++) {
      if (str[i] !== " ") {
          currentWord += str[i];
      } else if (currentWord.length > 0) {
          acronym += currentWord[0];
          currentWord = "";
      }
  }
  if (currentWord.length > 0) {
      acronym += currentWord[0];
  }
  return acronym.toUpperCase();
}

//credit Jason Yang
function acronymize(str) {
  //Your code here
  var result = "";
  var space = true;

  for (var i = 0; i < str.length; i++){
      if (space && str[i] != " "){
          space = false;
          result += str[i];
      } else if (str[i] == " ") {
          space = true;
      }
  }
  return result.toUpperCase();
}
//credit Marcus Seaman
function join(arr, separator) {
    //Your code here
    var newArr = "";
    for(var x=0; x < arr.length; x++) 
        if(newArr.length>0){
            newArr += separator;
            newArr += arr[x]
        }
        else{
            newArr += arr[x] 
        }
        return newArr
}