	class Solution {
		isAnagram(s, t) {
				if(s.length !== t.length){
						return false
				}
				let charCount = {} 

				for (let char of s){
						charCount[char] = (charCount[char] || 0)+ 1
				}
				console.log(charCount)

			for (let char of t){
				if(!charCount[char]) return false 

				charCount[char]--

				
			}





			return true
		}
	}


	const newSolution = new Solution()
	console.log(newSolution.isAnagram('race','acre'))









