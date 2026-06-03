class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let map = new Map ()

        for(let i = 0;i<nums.length;i++){
            const currentNumber = nums[i]
            const diff = target - currentNumber

            if(map.has(diff)){
                return [map.get(diff),i]
            }else{
                map.set(nums[i],i)
            }


        }



    }
}
