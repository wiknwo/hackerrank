function modifyArray(nums) {
    return nums.map(n => n = (n%2==0) ? n*2: n*3); 
}