class Solution {
    /**
     * Encodes a list of strings to a single string.
     * @param {string[]} strs
     * @return {string}
     */
    encode(strs) {
        let encodedString = "";

        for (let i = 0; i<strs.length;i++) {
            encodedString += strs[i].length + "#" + strs[i]; // Store length + '#' + word
        }

        return encodedString;
    }


    decode(str) {
        const decodedWord = []
        let i = 0
        while(i<str.length){
const delimiterIndex = str.indexOf('#',i) //1
const length = parseInt(str.slice(i,delimiterIndex)) //4
 i = delimiterIndex + 1;

const extractWords = str.slice(i,length + i)
decodedWord.push(extractWords)
i+= length
        }
return decodedWord
    }
}

