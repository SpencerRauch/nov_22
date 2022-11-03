/* 
  String: Rotate String
  Create a standalone function that accepts a string and an integer,
  and rotates the characters in the string to the right by that given
  integer amount.
*/

const str = "Hello World";

const rotateAmnt1 = 0;
const expected1 = "Hello World";

const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const rotateAmnt4 = 4;
const expected4 = "orldHello W";

const rotateAmnt5 = 13; 
const expected5 = "ldHello Wor";
/* 
Explanation: this is 2 more than the length so it ends up being the same
as rotating it 2 characters because after rotating every letter it gets back
to the original position.
*/

/**
 * Rotates a given string's characters to the right by the given amount,
 * wrapping characters to the beginning.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @param {number} amnt The amount of characters in the given str to rotate to the
 *    right.
 * @returns {string} The string rotated by the given amount.
 */
function rotateStr(str, amnt) {
    //Your code here
}

console.log(rotateStr(str, rotateAmnt1)); // expected: "Hello World"
console.log(rotateStr(str, rotateAmnt2)); // expected: "dHello Worl"
console.log(rotateStr(str, rotateAmnt3)); // expected: "ldHello Wor"
console.log(rotateStr(str, rotateAmnt4)); // expected: "orldHello W"
console.log(rotateStr(str, rotateAmnt5)); // expected: "ldHello Wor"


/*****************************************************************************/

/* 
  Create the function isRotation(str1,str2) that
  returns whether the second string is a rotation of the first.
*/

const strA1 = "ABCD";
const strA2 = "CDAB";
// Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated
const expectedA = true;

const strB1 = "ABCD";
const strB2 = "CDBA";
// Explanation: all same letters in 2nd string, but out of order
const expectedB = false;

const strC1 = "ABCD";
const strC2 = "BCDAB";
// Explanation: same letters in correct order but there is an extra letter.
const expectedC = false;

/**
 * Determines whether the second string is a rotated version of the first.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether the second string is a rotated version of the 1st.
 */
function isRotation(s1, s2) {
//Your code here
}

console.log(isRotation(strA1, strA2)); // expected: true
console.log(isRotation(strB1, strB2)); // expected: false
console.log(isRotation(strC1, strC2)); // expected: false
