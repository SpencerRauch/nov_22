/* 
  Recursive Factorial
  Input: integer
  Output: integer, product of ints from 1 up to given integer
  
  If less than zero, treat as zero.
  Bonus: If not integer, truncate (remove decimals).
  
  Experts tell us 0! is 1.
  
  rFact(3) = 6 (1*2*3)
  rFact(6.8) = 720 (1*2*3*4*5*6)
*/

const num1 = 3;
const expected1 = 6;
// Explanation: 1*2*3 = 6

const num2 = 6.8;
const expected2 = 720;
// Explanation: 1*2*3*4*5*6 = 720

const num3 = 0;
const expected3 = 1;

function factorial(n) {
    //Your code here
    //Santize value?
    //Base case?
    //Recursive return / call

}

/*****************************************************************************/
console.log(factorial(num1)) // 6
console.log(factorial(num2)) // 720
console.log(factorial(num3)) // 1

/*
  Sum To One Digit
  Implement a function sumToOne(num)​ that,
  given a number, sums that number’s digits
  repeatedly until the sum is only one digit. Return
  that final one digit result.
  Tips:
    to access digits from a number, need to convert it .toString() to access each digit via index
    parseInt(arg) returns arg parsed as an integer, or NaN if it couldn't be converted to an int
    isNaN(arg) used to check if something is NaN
*/

const numA = 5;
const expectedA = 5;

const numB = 10;
const expectedB = 1;

const numC = 25;
const expectedC = 7;

const numD = 999;// 9+9+9 = 27, 2 + 7 = 9
const expectedD = 9;
/**
 * Sums the given number's digits until the number becomes one digit.
 * @param {number} num The number to sum to one digit.
 * @returns {number} One digit.
 */
 function sumToOneDigit(num){
  //Your code here
  //base case
  //logic
  //recursive call/return

}

console.log(sumToOneDigit(numA)) // 5
console.log(sumToOneDigit(numB)) // 1
console.log(sumToOneDigit(numC)) // 7
console.log(sumToOneDigit(numD)) // 9
/*****************************************************************************/
