class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = new Map ()

        for(let char of strs){
            const sortedChar = char.split('').sort().join('');

            if(map.has(sortedChar)){
                map.get(sortedChar).push(char)
            }else{
                map.set(sortedChar,[char])
            }
        }
return Array.from(map.values())


    }
}
 