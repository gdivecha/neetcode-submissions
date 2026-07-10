class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ##### Approach #1:
        # Pseudocode:
        # - Check if the lenghts of both strings are the same
        # - If not, then:
        #   - return False
        # - If yes, then:
        #   - Create 2 dictionaries:
        #     - For s = appearancesInS
        #     - For T = appearancesInT
        #   - Both dictionaries conatin the following information:
        #     - Key = letter found in the string
        #     - Value = number of appearances of that letter int he string
        #   - For each letter in string s:
        #     - If the letter doesn't exist in appearancesInS as a key:
        #       - Add new dictionary entry like so: appearancesInS[letter] = 1
        #     - Otherwise:
        #       - Increment value of the dict key like so -> appearancesInS[letter] = appearancesInS.get(letter) + 1
        #   - For each letter in string t:
        #     - If the letter doesn't exist in appearancesInT as a key:
        #       - Add new dictionary entry like so: appearancesInT[letter] = 1
        #     - Otherwise:
        #       - Increment value of the dict key like so -> appearancesInT[letter] = appearancesInT.get(letter) + 1
        #   - Check if both dictionaries are the same
        #   - If they are the same:
        #     - return True
        #   - Otherwise:
        #     - return False
        # Complexity:
        # - Time complexity = O(n+m) because looping through each string once
        # - Space complexity = O(n+m) because creating 2 dictionaries, each being of the length of the respective string
        # Code:
        # if(len(s)!=len(t)):
        #     return False
        # else:
        #     appearancesInS = {}
        #     appearancesInT = {}
        #     for char in s:
        #         appearances = appearancesInS.get(char)
        #         if(not appearances):
        #             appearancesInS[char] = 1
        #         else:
        #             appearancesInS[char]+=1
        #     for char in t:
        #         appearances = appearancesInT.get(char)
        #         if(not appearances):
        #             appearancesInT[char] = 1
        #         else:
        #             appearancesInT[char]+=1
        #     if(appearancesInS==appearancesInT):
        #         return True
        #     else:
        #         return False
        
        ##### Approach #2:
        # Pseudocode:
        # - We could sort both strings and then go one by one with each character and check whether they match 
        # Complexity:
        # - Time complexity = O(nlogn + mlogm) because python directly uses timsort (fastest sorting algo) for both strings
        # - Space complexity = O(n+m) because timsort uses O(n) space complexity and we do that for both strings
        # Code:
        # sortedS = ''.join(sorted(s))
        # sortedT = ''.join(sorted(t))
        # for index, char in enumerate(sortedS):
        #     if(char!=sortedT[index]):
        #         return False
        # return True

        ##### Approach #3:
        # Pseudocode:
        # - By the definition of anagram, we can rearrange the characters so order doesn't matter
        # - A very simple way to go through this is that we can use hashing methods
        # - If the strings are not equal in length, then:
        #   - Not an anagram
        # - Otherwise:
        #   - We first set a specific value for each character in the alphabet (all 26)
        #   - We do so by creating a dictionary called alphabetMultiplier which holds the following info:
        #     - Key = alphabet
        #     - Value = prime number multiplier for the character so no hashing issues
        #   - We create 2 variables called sSum, and tSum each of which holds a sum startong at 0
        #   - Then we iterate through s and for each character in s:
        #     - We find the value for the character in question from alphabetMultiplier, multiply it with its ASCII code and add it to sSum
        #   - Then we iterate through s and for each character in t:
        #     - We find the value for the character in question from alphabetMultiplier, multiply it with its ASCII code and add it to tSum
        #   - If sSum and tSum are equal, then both strings are anagrams
        #   - Otherwise, they are not
        # Complexity:
        # - Time complexity = O(n+m) becuase iterating through both strings once
        # - Space complexity = O(1) because fixed length dictionary and 2 integer variables
        # Code:
        if(len(s)==len(t)):
            alphabetMultiplier = {
                'a': 1,
                'b': 3,
                'c': 5,
                'd': 7,
                'e': 11,
                'f': 13,
                'g': 17,
                'h': 19,
                'i': 23,
                'j': 29,
                'k': 31,
                'l': 37,
                'm': 41,
                'n': 43,
                'o': 47,
                'p': 53,
                'q': 59,
                'r': 61,
                's': 71,
                't': 73,
                'u': 83,
                'v': 89,
                'w': 97,
                'x': 101,
                'y': 103,
                'z': 107,
            }
            sSum = 0
            tSum = 0
            for character in s:
                sSum += (ord(character) * alphabetMultiplier.get(character))
            for character in t:
                tSum += (ord(character) * alphabetMultiplier.get(character))
            if(tSum==sSum):
                return True
        return False

        ##### Approach #4:
        # Pseudocode:
        # - If the strings are not equal in length, then:
        #   - Not an anagram
        # - Otherwise:
        #   - We can create a alphabetVsAppearances dictionary that holds the following info:
        #     - Key = alphabet
        #     - Value = the number of appearances it has
        #   - For each character in string s:
        #     - If the character is not in the keys in the dictionary, then:
        #       - We can add the pair by doing alphabetVsAppearances[char] = 1
        #     - Otherwise:
        #       - Increment the appearances by 1
        #   - For each character in string t:
        #     - If the character exists in the dictionary, then:
        #       - Decrement the appearances by 1
        #     - Otherwise:
        #       - return False
        #   - If the dictionary is empty:
        #     - return True
        #   - Otherwise:
        #     - return False
        # Complexity:
        # - Time complexity = O(n+m) because goes through both strings once at most
        # - Space complexity = O(1) in best case (since dictionary could be reduced to empty) or O(n) in worse case (because the biggest it can stay is teh sizeof string s)
        # Code:
        # if(len(s)!=len(t)):
        #     return False
        # else:
        #     alphabetVsAppearances = {}
        #     for character in s:
        #         appearance = alphabetVsAppearances.get(character)
        #         if(not appearance):
        #             alphabetVsAppearances[character] = 1
        #         else:
        #             alphabetVsAppearances[character] += 1
        #     print(alphabetVsAppearances)
        #     for character in t:
        #         appearance = alphabetVsAppearances.get(character)
        #         if(not appearance):
        #             return False
        #         else:
        #             if(appearance==1):
        #                 alphabetVsAppearances.pop(character)
        #             else:
        #                 alphabetVsAppearances[character] -= 1
        #     if(len(alphabetVsAppearances)==0):
        #         return True
        #     else:
        #         return False