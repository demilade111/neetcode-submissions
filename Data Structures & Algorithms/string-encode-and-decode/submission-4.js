class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
    let result = ''
    for(let char of strs){
        result+= char.length +'#'+char
      
    }
  return result
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let result = []
        let i =0

        while (i<str.length){
            let j = i

            while (str[j] !== '#'){
         j++

            }
            const getWordCount = parseInt(str.slice(i,j))

            const text = str.slice(j+1,j+1+getWordCount)
            result.push(text)


  i = j + 1 +getWordCount

        
        }

  

    return result


    }
}
