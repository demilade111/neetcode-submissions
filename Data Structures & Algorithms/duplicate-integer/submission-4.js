class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
    const newSet = new Set()
    for(let i = 0;i<nums.length;i++){
        if(newSet.has(nums[i])){
            return true;
        }else {
            newSet.add(nums[i])
        }
    }
return false;

    }
}

// 
nums = [1,2,3,4,4]

//if any element inside the array is duplicate say true otherwise say false:
// for each of the elelemt in the array compare each element with the next element in the array