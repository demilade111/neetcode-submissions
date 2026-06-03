class Solution {
  topKFrequent(nums, k) {
    const map = new Map();

    // Step 1: Count frequencies.
    for (let i = 0; i < nums.length; i++) {
      const num = nums[i];
      const elementCount = (map.get(num) || 0) + 1; // Correctly handle undefined.
      map.set(num, elementCount); // Update the count in the Map.
    }

    // Step 2: Convert the Map to an array of [number, frequency] pairs.
    const frequencyArray = Array.from(map);

    // Step 3: Sort the array by frequency in descending order.
    frequencyArray.sort((a, b) => b[1] - a[1]);

    // Step 4: Extract the top k elements.
    const result = [];
    for (let i = 0; i < k; i++) {
      result.push(frequencyArray[i][0]);
    }

    return result;
  }
}

// Test Case
const solution = new Solution();
console.log(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)); // Output: [1, 2]