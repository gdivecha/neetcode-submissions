class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedString = []
        for word in strs:
            encodedString.append(str(len(word)) + '#' + word)
        print("".join(encodedString))
        return "".join(encodedString)
    
    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        i = 0
        while i < len(s):
            j = s.find("#", i)          # end of the length number
            length = int(s[i:j])
            decodedStrings.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length          # jump past the word
        return decodedStrings


            



