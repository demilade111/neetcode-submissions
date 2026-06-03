class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map()
        for(let i= 0;i<nums.length;i++){
            const compliement = target - nums[i] //if this in the map we get the value which is the array index
if(map.has(compliement )){
    return [i,map.get(compliement)]
}else {
    map.set(nums[i],i)
}
        }
    }
}
