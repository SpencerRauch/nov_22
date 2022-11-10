/* 
  Array: Binary Search (non recursive)
  Given a sorted array and a value, return whether the array contains that value.
  Do not sequentially iterate the array. Instead, ‘divide and conquer’,
  taking advantage of the fact that the array is sorted .
  Bonus (alumni interview): 
    first complete it without the bonus, because they ask for additions
    after the initial algo is complete
    return how many times the given number occurs
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true; //1 for bonus

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true; //1 for bonus

// bonus, how many times does the search num appear?
const nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const searchNum4 = 2;
const expected4 = 4;

/**
 * Efficiently determines if the given num exists in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 */
 function binarySearch(sortedNums, searchNum) {
  //Your code here

}


console.log(binarySearch(nums1, searchNum1)); // false
console.log(binarySearch(nums2, searchNum2)); // true (1 for bonus)
console.log(binarySearch(nums3, searchNum3)); // true (1 for bonus)

// bonus, how many times does the search num appear?
// console.log(binarySearch(nums4, searchNum4)); // 4











function binarySearch(sortedNums, searchNum) {
  //Your code here
  let left = 0;
  let right = sortedNums.length - 1;
  while (left <= right) {
      let mid = Math.floor((left + right) / 2);
      if (sortedNums[mid] === searchNum) {
          return countAdjacentDupes(sortedNums, mid)
          // return true;
      } else if (sortedNums[mid] < searchNum) {
          left = mid + 1;
      } else {
          right = mid - 1;
      }
  }
  return false;
}

function countAdjacentDupes(arr, idx) {
  let count = 1;
  let elem = arr[idx];
  let right = idx + 1;
  let left = idx - 1;
  while (arr[right] === elem) {
      count++;
      right++;
  }
  while (arr[left] === elem) {
      count++;
      left--;
  }
  return count;

}


let i = 1
for (;;){
  console.log(i)
  i++
}