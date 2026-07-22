class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # - Let's try to come up with a simple solution keeping in mind
        #   that we must use slideing window to solve it:
        # - Let's look at the desired behavior and see how
        #   the pattern aligns with sliding window:
        #   - e.g. s = "zxyzxyz"
        #     - characterFrequency = {}
        #     - longestSubStringLength = 0
        #     - currentSubstringLen = 0
        #     - @ i = 0 -> s[0] = z
        #       - Is z in characterFrequency? No
        #       - characterFrequency = {z:1}
        #       - currentSubstringLen = 1
        #       - Is currentSubstringLen > longestSubStringLength? Yes
        #       - longestSubStringLength = 1
        #     - @ i = 1 -> s[1] = x
        #       - Is x in characterFrequency? No
        #       - characterFrequency = {z:1,x:1}
        #       - currentSubstringLen = 2
        #       - Is currentSubstringLen > longestSubStringLength? Yes
        #       - longestSubStringLength = 2
        #     - @ i = 2 -> s[2] = y
        #       - Is y in characterFrequency? No
        #       - characterFrequency = {z:1,x:1,y:1}
        #       - currentSubstringLen = 3
        #       - Is currentSubstringLen > longestSubStringLength? Yes
        #       - longestSubStringLength = 3
        #     - @ i = 3 -> s[3] = z
        #       - Is z in characterFrequency? Yes
        #       - characterFrequency = {}
        #       - currentSubstringLen = 0
        #     - Repeat for the rest of the string
        # - Something I can do to optimize this whole algorithm is that
        #   I can use a hash set instead of a dictionary

        # Algorithm:
        # - longestSubStringLength = 0
        # - currentString = set()
        # - Iterate through the string s and for each character:
        #   - If character is not in currentString:
        #     - Add the character to the set currentString
        #     - longestSubStringLength = max(longestSubStringLength,len(currentString))
        #   - Otherwise:
        #     - currentString = set()
        #     - Add the character to the set currentString
        #     - longestSubStringLength = max(longestSubStringLength,len(currentString))
        # - Return longestSubStringLength

        # longestSubStringLength = 0
        # currentString = set()
        # for character in s:
        #     if character in currentString:
        #         currentString = set()
        #     currentString.add(character)
        #     longestSubStringLength = max(longestSubStringLength, len(currentString))
        #     print(currentString)        
        # return longestSubStringLength
        
        # - 22/32 test cases pass and I see why that is the case
        # - I realized earlier that this solution so far doesn't
        #   necessarily use the "sliding window" strategy and is
        #   just relying on normal iteration using the for loop
        # - I see why we need sliding window here so let's look at
        #   what happened in the test case that failed
        #   - e.g. s="dvdf"
        #   - We looked at d, then dv, and when we get to the second
        #     d, we restart the substring we are looking at to now just d
        #   - This leads to the next evaluation to be df and this
        #     lets the longest length to remain at 2
        #   - Issue is that we should have had a mechanism in place for
        #     evaluation of vdf whcih actually outputs 3
        # - Thus, we need a sliding windo solution so let's try to figure that out
        # - We need a mechanism that:
        #   - When we see a duplicate, we need to not consider the first occurrence
        #     of that character in the string we are targeting
        # - How about when we see a second occurrence of a character already
        #   inside of the currentString we are tracking, we remove it's first occurrence
        # - Here it is in action:
        #   - e.g. s = "dvdf"
        #   - currentString = set()
        #   - longestSubstringLen = 0
        #   - @ i = 0:
        #     - s[0] = d
        #     - Is d in currentString? No
        #     - currentString = ['d']
        #     - longestSubstringLen = 1
        #   - @ i = 1:
        #     - s[1] = v
        #     - Is v in currentString? No
        #     - currentString = ['d','v']
        #     - longestSubstringLen = 2
        #   - @ i = 2:
        #     - s[2] = d
        #     - Is d in currentString? Yes
        #     - currentString.remove('d) and then currentString.add('d')
        #       - Essemtially we do nothing to currentString
        #     - currentString = ['v','d']
        #     - longestSubstringLen = 2
        #   - @ i = 3:
        #     - s[3] = f
        #     - Is f in currentString? No
        #     - currentString = ['v','d','f']
        #     - longestSubstringLen = 3
        # - Now, is this ideal in terms of complexity?
        #   - Here's what google has to say:
        #     - Breakdown of Complexity:
        #       - Average Case: O(1) - (Constant Time)
        #         - The HashSet uses a hash function to instantly 
        #           look up the memory bucket where the element 
        #           is stored, allowing immediate removal regardless 
        #           of how large the set is.
        #       - Worst Case: O(n) - (Linear Time)
        #         - This only occurs if there are extreme hash 
        #           collisions, meaning many different values generate 
        #           the exact same hash code and end up in the same 
        #           bucket. The program must then search through a 
        #           linked list or tree within that bucket to find 
        #           the item.
        #   - I don't think there are similar values which would 
        #     cause hash collisions in this question

        # - Let's try this approach with anoth er e.g. to confirm it works universally:
        #   - e.g. s = "zxyzxyz"
        #   - currentString = set()
        #   - longestSubstringLen = 0
        #   - @ i = 0:
        #     - s[0] = z
        #     - Is z in currentString? No
        #     - currentString = ['z']
        #     - longestSubstringLen = 1
        #   - @ i = 1:
        #     - s[1] = x
        #     - Is x in currentString? No
        #     - currentString = ['z','x']
        #     - longestSubstringLen = 2
        #   - @ i = 2:
        #     - s[2] = y
        #     - Is y in currentString? No
        #     - currentString = ['z','x','y']
        #     - longestSubstringLen = 3
        #   - @ i = 3:
        #     - s[3] = z
        #     - Is z in currentString? Yes
        #     - currentString = ['x','y','z']
        #     - longestSubstringLen = 3
        #   - @ i = 4:
        #     - s[4] = x
        #     - Is x in currentString? Yes
        #     - currentString = ['y','z','x']
        #     - longestSubstringLen = 3
        #  ...
        
        # - Let's apply the tweak:
        # longestSubStringLength = 0
        # currentString = set()
        # for index,character in enumerate(s):
        #     if character not in currentString:
        #         currentString.add(character)
        #     elif s[index-1]==character:
        #         currentString = set()
        #         currentString.add(character)
        #     longestSubStringLength = max(longestSubStringLength, len(currentString))
        #     print(currentString, longestSubStringLength)   
        # return longestSubStringLength

        # - 25/32 test cases pass this time adn the following test case fails it:
        #   - s="thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsovert"
        # - I see what the issue is:
        #   - In s, the longest substring is thequickbrownfoxj and when it sees
        #     another u, it needs to start looking at the string starting
        #     from the index after the first u meaning at the second u, we
        #     must look at ickbrownfoxju so far

        # - Will this work for s = "pwwkew"?
        #   - p -> pw -> w -> wk -> wke -> w Yes!!!

        # - Let's look at the desired behavior:
        #   - e.g. s = "pwwkew"
        #   - characterLocation = {}
        #   - longestSubstringLen = 0
        #   - currentStringBounds = [0,0]
        #   - highestSwitchCounter = 0
        #   - @ i = 0:
        #     - s[0] = p
        #     - Is p in characterLocation? No
        #     - characterLocation = {p:0}
        #     - currentStringBounds = [0,1]
        #     - lengthOfTrackingString = 1-0 = 1
        #     - longestSubstringLen = 1
        #   - @ i = 1:
        #     - s[1] = w
        #     - Is w in characterLocation? No
        #     - characterLocation = {p:0,w:1}
        #     - currentStringBounds = [0,2]
        #     - lengthOfTrackingString = 2-0 = 2
        #     - longestSubstringLen = 2
        #   - @ i = 2:
        #     - s[2] = w
        #     - Is w in characterLocation? Yes
        #       - Currently characterLocation = {p:0,w:1}
        #       - Is previous index value (i=1) the same value? Yes
        #         - Find value/location of w in characterLocation -> 1
        #         - Is this location of w's first occurrence < highestSwitchCounter? No
        #           - currentStringBounds[0] = 1+1 = 2
        #           - Reset characterLocation = {} and add the new w and its location
        #           - highestSwitchCounter = index = 2
        #         - characterLocation = {w:2}
        #         - currentStringBounds = [2,3]
        #         - lengthOfTrackingString = 3-2 = 1
        #         - longestSubstringLen = 2
        #   - @ i = 3:
        #     - s[3] = k
        #     - Is k in characterLocation? No
        #     - characterLocation = {w:2,k:3}
        #     - currentStringBounds = [2,4]
        #     - lengthOfTrackingString = 4-2 = 2
        #     - longestSubstringLen = 2
        #   - @ i = 4:
        #     - s[4] = e
        #     - Is e in characterLocation? No
        #     - characterLocation = {w:2,k:3,e:4}
        #     - currentStringBounds = [2,5]
        #     - lengthOfTrackingString = 5-2 = 3
        #     - longestSubstringLen = 3
        #   - @ i = 5:
        #     - s[5] = w
        #     - Is w in characterLocation? Yes
        #       - Currently characterLocation = {w:2,k:3,e:4}
        #       - Is previous index value (i=4) the same value? No
        #         - Find value/location of w in characterLocation -> 2
        #         - Is this location of w's first occurrence < highestSwitchCounter? No:
        #           - currentStringBounds[0] = 2+1 = 3
        #           - highestSwitchCounter = index of w's first occurrence = 2
        #         - If that were'nt the case:
        #           - Then we currentStringBounds[0] = highestSwitchCounter+1
        #         - characterLocation = {w:6,k:3,e:4}
        #         - currentStringBounds = [3,6]
        #         - lengthOfTrackingString = 6-2 = 3
        #         - longestSubstringLen = 3
        # 
        # - Let's apply to e.g. s="abba"
        #   - characterLocation = {}
        #   - longestSubstringLen = 0
        #   - currentStringBounds = [0,0]
        #   - highestSwitchCounter = 0
        #   - @ i = 0:
        #     - s[0] = a
        #     - Is a in characterLocation? No
        #     - characterLocation = {a:0}
        #     - currentStringBounds = [0,1]
        #     - lengthOfTrackingString = 1-0 = 1
        #     - longestSubstringLen = 1
        #   - @ i = 1:
        #     - s[1] = b
        #     - Is b in characterLocation? No
        #     - characterLocation = {a:0,b:1}
        #     - currentStringBounds = [0,2]
        #     - lengthOfTrackingString = 2-0 = 2
        #     - longestSubstringLen = 2
        #   - @ i = 2:
        #     - s[2] = b
        #     - Is b in characterLocation? Yes
        #       - Currently characterLocation = {a:0,b:1}
        #       - Is previous index value (i=1) the same value? Yes
        #         - Find value/location of b in characterLocation -> 1
        #         - Is this location of b's first occurrence < highestSwitchCounter? or (1<0)? No
        #           - currentStringBounds[0] = 1+1 = 2
        #           - Reset characterLocation = {} and add the new w and its location
        #           - highestSwitchCounter = index of b's first occurrence = 1
        #         - characterLocation = {b:2}
        #         - currentStringBounds = [2,3]
        #         - lengthOfTrackingString = 3-2 = 1
        #         - longestSubstringLen = 2
        #   - @ i = 3:
        #     - s[3] = a
        #     - Is a in characterLocation? No
        #     - characterLocation = {b:1,a:3}
        #     - currentStringBounds = [2,4]
        #     - lengthOfTrackingString = 4-2 = 2
        #     - longestSubstringLen = 2

        # - Let's apply to e.g. s="abcabcbab"
        #   - characterLocation = {}
        #   - longestSubstringLen = 0
        #   - currentStringBounds = [0,0]
        #   - highestSwitchCounter = 0
        #   - @ i = 0:
        #     - s[0] = a
        #     - Is a in characterLocation? No
        #     - characterLocation = {a:0}
        #     - currentStringBounds = [0,1]
        #     - lengthOfTrackingString = 1-0 = 1
        #     - longestSubstringLen = 1
        #   - @ i = 1:
        #     - s[1] = b
        #     - Is b in characterLocation? No
        #     - characterLocation = {a:0,b:1}
        #     - currentStringBounds = [0,2]
        #     - lengthOfTrackingString = 2-0 = 2
        #     - longestSubstringLen = 2
        #   - @ i = 2:
        #     - s[2] = c
        #     - Is c in characterLocation? No
        #     - characterLocation = {a:0,b:1,c:2}
        #     - currentStringBounds = [0,3]
        #     - lengthOfTrackingString = 3-0 = 3
        #     - longestSubstringLen = 3
        #   - @ i = 3:
        #     - s[3] = a
        #     - Is a in characterLocation? Yes
        #       - Currently characterLocation = {a:0,b:1,c:2}
        #       - Is previous index value (i=2) the same value? No
        #         - Find value/location of a in characterLocation -> 0
        #         - Is this location of a's first occurrence < highestSwitchCounter? or (0<0)? No:
        #           - currentStringBounds[0] = 0+1 = 1
        #           - highestSwitchCounter = index of a's first occurrence = 0
        #         - characterLocation = {a:3,b:1,c:2}
        #         - currentStringBounds = [1,4]
        #         - lengthOfTrackingString = 4-1 = 3
        #         - longestSubstringLen = 3
        #   - @ i = 4:
        #     - s[4] = b
        #     - Is b in characterLocation? Yes
        #       - Currently characterLocation = {a:3,b:1,c:2}
        #       - Is previous index value (i=3) the same value? No
        #         - Find value/location of b in characterLocation -> 1
        #         - Is this location of b's first occurrence < highestSwitchCounter? or (0<0)? No:
        #           - currentStringBounds[0] = 1+1 = 2
        #           - highestSwitchCounter = index of b's first occurrence = 1
        #         - characterLocation = {a:3,b:4,c:2}
        #         - currentStringBounds = [2,5]
        #         - lengthOfTrackingString = 5-2 = 3
        #         - longestSubstringLen = 3
        #   - @ i = 5:
        #     - s[5] = c
        #     - Is c in characterLocation? Yes
        #       - Currently characterLocation = {a:3,b:4,c:2}
        #       - Is previous index value (i=4) the same value? No
        #         - Find value/location of c in characterLocation -> 2
        #         - Is this location of c's first occurrence < highestSwitchCounter? or (2<1)? No:
        #           - currentStringBounds[0] = 2+1 = 3
        #           - highestSwitchCounter = index of c's first occurrence = 2
        #         - characterLocation = {a:3,b:4,c:5}
        #         - currentStringBounds = [3,6]
        #         - lengthOfTrackingString = 6-3 = 3
        #         - longestSubstringLen = 3
        #   - @ i = 6:
        #     - s[6] = b
        #     - Is b in characterLocation? Yes
        #       - Currently characterLocation = {a:3,b:4,c:5}
        #       - Is previous index value (i=5) the same value? No
        #         - Find value/location of b in characterLocation -> 4
        #         - Is this location of 4's first occurrence < highestSwitchCounter? or (4<2)? No:
        #           - currentStringBounds[0] = 4+1 = 5
        #           - highestSwitchCounter = index of b's first occurrence = 4
        #         - characterLocation = {a:3,b:6,c:5}
        #         - currentStringBounds = [5,7]
        #         - lengthOfTrackingString = 7-5 = 2
        #         - longestSubstringLen = 3
        #   - @ i = 7:
        #     - s[7] = a
        #     - Is a in characterLocation? Yes
        #       - Currently characterLocation = {a:3,b:6,c:5}
        #       - Is previous index value (i=6) the same value? No
        #         - Find value/location of a in characterLocation -> 3
        #         - Is this location of a's first occurrence < highestSwitchCounter? or (3<4)? Yes:
        #           - currentStringBounds[0] = highestSwitchCounter + 1 = 4+1 = 5
        #           - highestSwitchCounter stays the same = 4
        #         - characterLocation = {a:7,b:6,c:5}
        #         - currentStringBounds = [5,8]
        #         - lengthOfTrackingString = 8-5 = 3
        #         - longestSubstringLen = 3
        #   - @ i = 8:
        #     - s[8] = b
        #     - Is b in characterLocation? Yes
        #       - Currently characterLocation = {a:7,b:6,c:5}
        #       - Is previous index value (i=7) the same value? No
        #         - Find value/location of b in characterLocation -> 6
        #         - Is this location of b's first occurrence < highestSwitchCounter? or (6<4)? No:
        #           - currentStringBounds[0] = 6+1 = 7
        #           - highestSwitchCounter = index of b's first occurrence = 6
        #         - characterLocation = {a:7,b:8,c:5}
        #         - currentStringBounds = [7,9]
        #         - lengthOfTrackingString = 9-7 = 2
        #         - longestSubstringLen = 3
        # ... 
        # - I think this could work well

        # - Algorithm:
        #   - characterLocation = {}
        #   - longestSubstringLen = 0
        #   - currentStringBounds = [0,0]
        #   - highestSwitchCounter = 0
        #   - Iterate through s and for each character and its index:
        #     - If character in characterLocation as a key:
        #       - firstOccurrenceOfChar = characterLocation.get(character)
        #       - If firstOccurrenceOfChar >= highestSwitchCounter:
        #         - currentStringBounds[0] = firstOccurrenceOfChar + 1
        #         - highestSwitchCounter = firstOccurrenceOfChar
        #       - Else:
        #         - currentStringBounds[0] = highestSwitchCounter + 1
        #       - If previous index (index-1) has same value:
        #         - characterLocation = {}
        #     - characterLocation[character] = index
        #     - currentStringBounds[1] = index+1
        #     - lengthOfTrackingString = currentStringBounds[1] - currentStringBounds[0]
        #     - longestSubstringLen = max(longestSubstringLen,lengthOfTrackingString)
        #   - Return longestSubstringLen

        characterLocation = {}
        longestSubstringLen = 0
        currentStringBounds = [0,0]
        highestSwitchCounter = 0
        for index,character in enumerate(s):
            if character in characterLocation:
                firstOccurrenceOfChar = characterLocation.get(character)
                if firstOccurrenceOfChar >= highestSwitchCounter:
                    currentStringBounds[0] = firstOccurrenceOfChar + 1
                    highestSwitchCounter = firstOccurrenceOfChar
                else:
                    currentStringBounds[0] = highestSwitchCounter + 1
                if s[index-1]==character:
                    characterLocation = {}
            characterLocation[character] = index
            currentStringBounds[1] = index + 1
            lengthOfTrackingString = currentStringBounds[1] - currentStringBounds[0]
            longestSubstringLen = max(longestSubstringLen,lengthOfTrackingString)
        return longestSubstringLen