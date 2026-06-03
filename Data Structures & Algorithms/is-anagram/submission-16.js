class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let charCounts = new Map()

    if (s.length !== t.length){
        return false
    }
    for(let char of s){
        charCounts.set(char,(charCounts.get(char)|| 0)+ 1)

    }

     for(let char of t){
       if(!charCounts.has(char) || charCounts.get(char)=== 0){
        return false
       }
         charCounts.set(char, charCounts.get(char) - 1);
       


    }

return true
    }
}

