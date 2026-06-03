class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const newSet = new Set(nums)
        let maxLength = 0


        for(const  num of newSet){
            if(!newSet.has(num-1)){
                let count= 1
                let currentNumber = num

                while(newSet.has(currentNumber+1)){
                    count+=1
                    currentNumber+=1
                }

 maxLength = Math.max(maxLength, count);
            }

  
        }




  return maxLength;

    }
}


