class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {

let map = new Map()

for(let char of strs){
const sortedStrings = char.split('').sort().join('')
if(map.has(sortedStrings)){
    map.get(sortedStrings).push(char)
}else{
    map.set(sortedStrings,[char])
}
}
return Array.from(map.values())
    }
}

