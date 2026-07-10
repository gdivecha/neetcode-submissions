class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # - We can use the concept learned in COE 428 where
        #   when learning hash tables, we can give each alphabet
        #   a unique prime value - e.g. a=2, b=3, c=5, ....
        # - 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
        #   53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101
        # - We multiply those values by the number of times the letter
        #   was repeated and we add them all together
        # - E.g. "act" -> 2 + 5 + 71 = 78
        #        "cat" -> 5 + 2 + 71 = 78
        #        "acct" -> 2 + 2(5) + 71 = 83
        #        "w" -> 83 = 83
        # - You may have noticed we have "acct" and "w" both resulting
        #   to 83
        # - The easiest way to solve this problem is that we check the
        #   total lengths of 2 strings directly and compare and if they
        #   are not the same, then those 2 strings cannot go together

        # Algorithm:
        # - Create an integer array named letterHashes
        # - Loop through the array strs and for each string:
        #   - Create an integer var named runningHash = 0
        #   - For each letter within the current string:
        #     - Add the current letter's corresponding prime value to 
        #       the runningHash
        #   - Append the following to letterHashes:
        #     - "runningHash" + x + "len(strs[Index of the current string])"
        # - Create a dictionary (hashLists) that holds the following:
        #   - Key = Integer in the form of a string representing a hash value
        #   - Value = Array of integers that represent an index
        # - Iterate through the letterHashes and for each hash:
        #   - If the current hash is not in the list of keys of hashLists:
        #     - Add the following:
        #       - Key = currentHash
        #       - Value = [currentIndex]
        #   - Otherwise:
        #     - Append the currentIndex to the value of key that represents currentHash
        # - Create a new array that holds arrays of strings called anagrams
        # - For each key within letterHashes dictionary:
        #   - Create a new array of strings called currentAnagrams = []
        #   - For each index in the array that correspnds to the currentKey
        #     - Append strs[currentIndex] to currentAnagrams
        #   - Append currentAnagrams to anagrams
        # - Return anagrams

        # --------CODE STARTS HERE--------

        # letterHashes = []
        # letterToPrime = {
        #     "a":2,
        #     "b":3, 
        #     "c":5, 
        #     "d":7, 
        #     "e":11, 
        #     "f":13, 
        #     "g":17, 
        #     "h":19, 
        #     "i":23, 
        #     "j":29, 
        #     "k":31, 
        #     "l":37, 
        #     "m":41, 
        #     "n":43, 
        #     "o":47, 
        #     "p":53, 
        #     "q":59, 
        #     "r":61, 
        #     "s":67, 
        #     "t":71, 
        #     "u":73, 
        #     "v":79, 
        #     "w":83, 
        #     "x":89, 
        #     "y":97, 
        #     "z":101
        # }
        # for currentIndex,currentString in enumerate(strs):
        #     runningHash = 0
        #     for currentLetter in currentString:
        #         runningHash+=(letterToPrime.get(currentLetter))
        #     letterHashes.append(f"{runningHash}x{len(strs[currentIndex])}")
        
        # hashLists = {}
        # for currentIndex,currentHash in enumerate(letterHashes):
        #     if currentHash not in hashLists:
        #         hashLists[currentHash] = [currentIndex]
        #     else:
        #         hashLists[currentHash].append(currentIndex)

        # anagrams = []
        # for currentHashKey in hashLists.keys():
        #     currentAnagrams = []
        #     for currentIndex in hashLists.get(currentHashKey):
        #         currentAnagrams.append(strs[currentIndex])
        #     anagrams.append(currentAnagrams)

        # return anagrams

        # --------CODE ENDS HERE--------

        # 25/27 test cases pass here and after using diff checker,
        # I saw that for example, vhbaa and skbaa are considered to
        # be anagrams which is completely false. The reason is
        # vh and sk both when adding their prime equivalents up result to 98.
        # This means that the algorithm works fine - We need some numbers
        # and values that help us set them apart even more without collision.

        # Solution:
        # - We cannot just rely on the simple addition of prime equivalents
        # - We need something that scatters the hashes more
        # - We can multiply the ASCII value of the letter alphabet with its
        #   corresponding prime value before adding it to the running hash
        # - This would separate the hashes farther

        # --------CODE STARTS HERE--------

        # letterHashes = []
        # letterToPrime = {
        #     "a":2,
        #     "b":3, 
        #     "c":5, 
        #     "d":7, 
        #     "e":11, 
        #     "f":13, 
        #     "g":17, 
        #     "h":19, 
        #     "i":23, 
        #     "j":29, 
        #     "k":31, 
        #     "l":37, 
        #     "m":41, 
        #     "n":43, 
        #     "o":47, 
        #     "p":53, 
        #     "q":59, 
        #     "r":61, 
        #     "s":67, 
        #     "t":71, 
        #     "u":73, 
        #     "v":79, 
        #     "w":83, 
        #     "x":89, 
        #     "y":97, 
        #     "z":101
        # }
        # for currentIndex,currentString in enumerate(strs):
        #     runningHash = 0
        #     for currentLetter in currentString:
        #         runningHash+=(ord(currentLetter)*letterToPrime.get(currentLetter))
        #     letterHashes.append(f"{runningHash}x{len(strs[currentIndex])}")
        
        # print(letterHashes)

        # hashLists = {}
        # for currentIndex,currentHash in enumerate(letterHashes):
        #     if currentHash not in hashLists:
        #         hashLists[currentHash] = [currentIndex]
        #     else:
        #         hashLists[currentHash].append(currentIndex)

        # anagrams = []
        # for currentHashKey in hashLists.keys():
        #     currentAnagrams = []
        #     for currentIndex in hashLists.get(currentHashKey):
        #         currentAnagrams.append(strs[currentIndex])
        #     anagrams.append(currentAnagrams)

        # return anagrams

        # --------CODE ENDS HERE--------

        # Seems like once this was solved, there were other collisions
        # seemingly that are not as serious as before.
        # Again, 25/27 test cases fail and for example, nx and ss are 
        # regarded as anagrams which they are not.
        # What if we do both ways and append it to the hash string
        # -> The multiplication and the addition

        letterHashes = []
        letterToPrime = {
            "a":2,
            "b":3, 
            "c":5, 
            "d":7, 
            "e":11, 
            "f":13, 
            "g":17, 
            "h":19, 
            "i":23, 
            "j":29, 
            "k":31, 
            "l":37, 
            "m":41, 
            "n":43, 
            "o":47, 
            "p":53, 
            "q":59, 
            "r":61, 
            "s":67, 
            "t":71, 
            "u":73, 
            "v":79, 
            "w":83, 
            "x":89, 
            "y":97, 
            "z":101
        }
        for currentIndex,currentString in enumerate(strs):
            runningHash = 0
            primeSum = 0
            for currentLetter in currentString:
                primeSum+=(letterToPrime.get(currentLetter))
                runningHash+=(ord(currentLetter)*letterToPrime.get(currentLetter))
            letterHashes.append(f"{runningHash}x{len(strs[currentIndex])}x{primeSum}")
        
        hashLists = {}
        for currentIndex,currentHash in enumerate(letterHashes):
            if currentHash not in hashLists:
                hashLists[currentHash] = [currentIndex]
            else:
                hashLists[currentHash].append(currentIndex)

        anagrams = []
        for currentHashKey in hashLists.keys():
            currentAnagrams = []
            for currentIndex in hashLists.get(currentHashKey):
                currentAnagrams.append(strs[currentIndex])
            anagrams.append(currentAnagrams)

        return anagrams



