class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let freqMap = new Map();

        // Step 1: Count frequency of each number
        for (let i = 0; i < nums.length; i++) {
            if (freqMap.has(nums[i])) {
                freqMap.set(nums[i], freqMap.get(nums[i]) + 1); // ✅ fix here
            } else {
                freqMap.set(nums[i], 1);
            }
        }

        // Step 2: Create buckets
        const bucket = Array(nums.length + 1).fill().map(() => []);

        // Step 3: Fill buckets
        for (let [num, freq] of freqMap.entries()) {
            bucket[freq].push(num);
        }

        // Step 4: Collect top k frequent elements
        const result = [];
        for (let i = bucket.length - 1; i >= 0 && result.length < k; i--) {
            if (bucket[i].length > 0) {
                result.push(...bucket[i]);
            }
        }

        // ✅ fix: return the final result
        return result.slice(0, k);
    }
}
