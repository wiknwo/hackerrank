/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    var max = Math.max.apply(null, nums); // get the max of the array
    while (nums.indexOf(max) != -1) {
        nums.splice(nums.indexOf(max), 1); // remove max from the array
    }
    
    
    return Math.max.apply(null, nums); // get the 2nd max
}