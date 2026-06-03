class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
let left = 0
let right = numbers.length - 1
while(left<right){
    let sum = numbers[left] + numbers[right]

    if(sum===target){
        return [left+1,right+1]
    }else if(sum<target){
        left++

    }else{
        right --
    }

}



   return []
    }
}
//   input : array of integers which must be non-decreasing order. .. from small to highest
// target; integers
//output : index of two numbers , return array of 2 numbers
// goals ; we need to return the two index of different elenent that sum up to the target

