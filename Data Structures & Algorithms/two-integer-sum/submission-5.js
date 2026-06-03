class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const mapCount = new Map()

        for(let i = 0 ; i<nums.length;i++){
            let diff =  target - nums[i]
            if(mapCount.has(diff)){
                return[mapCount.get(diff),i]
            }else{
                mapCount.set(nums[i], i)
            }

    
        }


    }
}


