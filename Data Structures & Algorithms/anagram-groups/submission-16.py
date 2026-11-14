class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Brute Force Approach:
        # - Create a dict taht holds:
        #   - Key = sorted words
        #   - Value = List of indices that are associated to that sorted
        #             word
        # - Iterate through each word within strs and for each word:
        #   - Sort the word according to their letters e.g. "act" and
        #     "cat" would both be "act"
        #     - e.g. [act, opst, opst, act, opst, aht]
        #   - Check whether that sorted word exists in the dict
        #     - If not, then we add it as (sortedWord:[that word])
        #     - If yes, then we append that word to list for that sorted
        #       word
        # - Print out the values
        #
        # Complexity:
        # - Time = O(n x (mlogm)) where n = # of words and m = length of 
        #   the longest word
        # - Space = O(n x m) in the worse, each word is unique because
        #   a string which is almost like a list meaning we have m chars
        #   and n words

        # Optimize this:
        # - 26 alphabets in total
        # - act -> [1,0,1,0,....,0,1,0,...]
        # - cat -> [1,0,1,0,....,0,1,0,...]
        # ..
        # - Lists cannot be assigned as keys because they are mutable
        #   which makes them not hashable
        # - Tuple is what lists are but they are immutable meaning they
        #   cannot be changed after setting their values
        # - Iterate through each word within strs:
        #   - We create the list that holds [0] * 26
        #   - Iterate through the word and for each character:
        #     - indexOfAlphabet = ASCII(that char) - ASCII('a') 
        #       and that is the index in the tuple we'll name count
        #     - Retrive the value of that index and we add a 1 to it
        #       for that character
        #   - Add this count to the dictionary as a key if it doesn't
        #     exist and assign it a value of [that word]
        #   - Append that word to the key's list if it does exist

        anagrams = {}

        for word in strs:
            count = [0] * 26
            for alphabet in word:
                indexOfAlphabet = ord(alphabet) - ord('a') 
                count[indexOfAlphabet] += 1
            if tuple(count) not in anagrams:
                anagrams[tuple(count)] = [word]
            else:
                anagrams[tuple(count)].append(word)
        return list(anagrams.values())
        
