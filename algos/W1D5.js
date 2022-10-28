/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation or capitalization
*/
// RIOT Read Input Output Talk
const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

const str5 = "abba"
const expected5 = true;


function isPalindrome(str) {
    //Your code here
}

console.log(isPalindrome(str1)) //expected: true
console.log(isPalindrome(str2)) //expected: true
console.log(isPalindrome(str3)) //expected: false
console.log(isPalindrome(str4)) //expected: false
console.log(isPalindrome(str5)) //expected: true

/* 
  Zip Arrays into Map/Object
  
  
  Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
  Associative arrays are sometimes called maps because a key (string) maps to a value 

  If length of arrays are not equal, return false
*/

const keys1 = ["flavor", "size", "is_delicious"];
const vals1 = ["chocolate", 10, true];
const expectedA = {
    flavor: 'chocolate',
    size: 10,
    is_delicious: true,
};

const keys2 = [];
const vals2 = [];
const expectedB = {};

const keys3 = ['name', 'number', 'type', 'evolves_from']
const vals3 = ['Gyarados', 130, 'water/flying', 'Magikarp']
const expectedC = {
    name: 'Gyarados',
    number: 130,
    type: 'water/flying',
    evolves_from: 'Magikarp'
}

function zipArraysIntoMap(keys, values) {
    //Your code here
}
console.log(zipArraysIntoMap(keys1, vals1)) // expected: { flavor: 'chocolate', size: 10, is_delicious: true } (order may vary)
console.log(zipArraysIntoMap(keys2, vals2)) // expected: {} 
console.log(zipArraysIntoMap(keys3, vals3)) // expected: { name: 'Gyarados', number: 130, type: 'water/flying', evolves_from: 'Magikarp' } (order may vary)
