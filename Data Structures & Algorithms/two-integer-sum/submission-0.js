class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {

const map = new Map() //{}
        for (let i = 0;i<nums.length;i++){

            const compliement = target - nums[i]    //10-2= 8

            if(map.has(compliement)){
                return [i,map.get(compliement)]
            }
            map.set(nums[i],i)
            
        }



    }
}




