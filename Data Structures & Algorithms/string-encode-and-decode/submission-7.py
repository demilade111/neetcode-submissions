class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the '#'
            while s[j] != "#":
                j += 1

            # Length of the word
            wordLength = int(s[i:j])

            # Extract the word
            word = s[j + 1 : j + 1 + wordLength]
            result.append(word)

            # Move i to the beginning of the next encoded word
            i = j + 1 + wordLength

        return result