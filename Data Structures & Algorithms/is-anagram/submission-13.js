class Solution {
		
	isAnagram(s, t) {

const newMap = new Map()


if(s.length !== t.length) return false

for (let char of s){
     newMap.set(char,(newMap.get(char) || 0)+1 )

}

for (let char of t){
    if(!newMap.has(char)|| newMap.get(char) === 0){
        return false
    }else{
        newMap.set(char, newMap.get(char )- 1)
    }



}


return true 

		}


		
}




const solution = new Solution()

console.log(solution.isAnagram('anagram', 'nagaram'))


