/* 
Given an array of ints representing a line of people where the space between
indexes is 1 foot, with 0 meaning no one is there and 1 meaning someone is in
that space,
return whether or not there is at least 6 feet separating every person.
Bonus: O(n) linear time (avoid nested loops that cause re-visiting indexes).
*/

const queue1 = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1];
const expected1 = false;

const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected2 = true;

const queue3 = [1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected3 = true;

const queue4 = [];
const expected4 = true;

/**
 * Determines whether each occupied space in the line of people is separated by
 * 6 empty spaces.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<0|1>} queue
 * @returns {Boolean}
 */
function socialDistancingEnforcer(queue) {
    //Your code here
}

console.log(socialDistancingEnforcer(queue1)) // false
console.log(socialDistancingEnforcer(queue2)) // true
console.log(socialDistancingEnforcer(queue3)) // true
console.log(socialDistancingEnforcer(queue4)) // true

/* 
  Balance Index
  Here, a balance point is ON an index, not between indices.
  Return the balance index where sums are equal on either side
  (exclude its own value).
  
  Return -1 if none exist.
  
*/
            // 0   1  2  3  4
const numsA = [-2, 5, 7, 0, 3];
const expectedA = 2;

const numsB = [9, 9];
const expectedB = -1;

const numsC = [1,1,1,1,1,9,1,1,1,1,1]
const expectedC = 5



/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
function balanceIndex(nums) {
    //Your code here
}

console.log(balanceIndex(numsA)) // 2
console.log(balanceIndex(numsB)) // -1
console.log(balanceIndex(numsC)) // 5




function balanceIndex(nums) {
    if (nums.length < 3) {
        return -1;
    }
  
    let left = nums[0];
    let right = 0;
  
    for (let i = 2; i < nums.length; i++) {
        right += nums[i];
    }
  
    for (let i = 1; i < nums.length - 1; i++) {
        if (left === right) {
            return i;
        }
        right -= nums[i + 1];
        left += nums[i];
    }
    return -1;
  }
  







  function balanceIndex(nums) {
    if(nums.length >= 3){
        for(var i =1; i< nums.length -1; i++){
            var suml=0
            var sumr = 0
            for(var j = 0; j < i; j++){
                suml += nums[j]
            }
            for(var k = i+1; k < nums.length; k++){
                sumr += nums[k]
            }
            if(suml == sumr){
                return i
            }
        }
    }
    return -1
  }
  
  
  
  function socialDistancingEnforcer(queue) {
    var position = [];
    var flag =true;
    for (i=0;i<queue.length;i++) {
        if (queue[i] == 1) {
            position.push(i)
        }
    }
    for (i=1;i<position.length;i++){
        if (position[i] - position[i-1] < 6){
            flag = false
            return flag
        }
    }
    return flag 
  }
  
  function socialDistancingEnforcer(queue) {
    var count = 0
    var people = false
    if (queue.length === 0){
        return true
    }
    for (var i = 0; i < queue.length; i++) {
        if (queue[i] === 1 && people === false) {
            people = true
            count = 0
        }
        else if (queue[i] === 1 && people === true){
            people = false
            if (count < 6) {
                return false
            } else if (count >= 6){
                people = true
            }
            count = 0
        }
        if (people === true) {
            if(queue[i] === 0){
                count++
            }
        }
    }
    return people
}
  
  
  function socialDistancingEnforcer(queue) {
    let distance = 0;
    let firstPersonSeen = false;
    for (let i = 0; i < queue.length; i++) {
        if (queue[i] === 0) {
            distance += 1;
        } else {
            if (firstPersonSeen && distance < 6) {
                return false;
            }
            firstPersonSeen = true;
            distance = 0;
        }
    }
    return true;
  }
  