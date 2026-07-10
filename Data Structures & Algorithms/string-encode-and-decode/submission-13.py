# class Solution:

#     ascii_to_prime = {
#         chr(0): 2, chr(1): 3, chr(2): 5, chr(3): 7, chr(4): 11, chr(5): 13, 
#         chr(6): 17, chr(7): 19, chr(8): 23, chr(9): 29, chr(10): 31, chr(11): 37, 
#         chr(12): 41, chr(13): 43, chr(14): 47, chr(15): 53, chr(16): 59, chr(17): 61, 
#         chr(18): 67, chr(19): 71, chr(20): 73, chr(21): 79, chr(22): 83, chr(23): 89, 
#         chr(24): 97, chr(25): 101, chr(26): 103, chr(27): 107, chr(28): 109, chr(29): 113, 
#         chr(30): 127, chr(31): 131, chr(32): 137, chr(33): 139, chr(34): 149, chr(35): 151, 
#         chr(36): 157, chr(37): 163, chr(38): 167, chr(39): 173, chr(40): 179, chr(41): 181, 
#         chr(42): 191, chr(43): 193, chr(44): 197, chr(45): 199, chr(46): 211, chr(47): 223, 
#         chr(48): 227, chr(49): 229, chr(50): 233, chr(51): 239, chr(52): 241, chr(53): 251, 
#         chr(54): 257, chr(55): 263, chr(56): 269, chr(57): 271, chr(58): 277, chr(59): 281, 
#         chr(60): 283, chr(61): 293, chr(62): 307, chr(63): 311, chr(64): 313, chr(65): 317, 
#         chr(66): 331, chr(67): 337, chr(68): 347, chr(69): 349, chr(70): 353, chr(71): 359, 
#         chr(72): 367, chr(73): 373, chr(74): 379, chr(75): 383, chr(76): 389, chr(77): 397, 
#         chr(78): 401, chr(79): 409, chr(80): 419, chr(81): 421, chr(82): 431, chr(83): 433, 
#         chr(84): 439, chr(85): 443, chr(86): 449, chr(87): 457, chr(88): 461, chr(89): 463, 
#         chr(90): 467, chr(91): 479, chr(92): 487, chr(93): 491, chr(94): 499, chr(95): 503, 
#         chr(96): 509, chr(97): 521, chr(98): 523, chr(99): 541, chr(100): 547, chr(101): 557, 
#         chr(102): 563, chr(103): 569, chr(104): 571, chr(105): 577, chr(106): 587, chr(107): 593, 
#         chr(108): 599, chr(109): 601, chr(110): 607, chr(111): 613, chr(112): 617, chr(113): 619, 
#         chr(114): 631, chr(115): 641, chr(116): 643, chr(117): 647, chr(118): 653, chr(119): 659, 
#         chr(120): 661, chr(121): 673, chr(122): 677, chr(123): 683, chr(124): 691, chr(125): 701, 
#         chr(126): 709, chr(127): 719, chr(128): 727, chr(129): 733, chr(130): 739, chr(131): 743, 
#         chr(132): 751, chr(133): 757, chr(134): 761, chr(135): 769, chr(136): 773, chr(137): 787, 
#         chr(138): 797, chr(139): 809, chr(140): 811, chr(141): 821, chr(142): 823, chr(143): 827, 
#         chr(144): 829, chr(145): 839, chr(146): 853, chr(147): 857, chr(148): 859, chr(149): 863, 
#         chr(150): 877, chr(151): 881, chr(152): 883, chr(153): 887, chr(154): 907, chr(155): 911, 
#         chr(156): 919, chr(157): 929, chr(158): 937, chr(159): 941, chr(160): 947, chr(161): 953, 
#         chr(162): 967, chr(163): 971, chr(164): 977, chr(165): 983, chr(166): 991, chr(167): 997, 
#         chr(168): 1009, chr(169): 1013, chr(170): 1019, chr(171): 1021, chr(172): 1031, chr(173): 1033, 
#         chr(174): 1039, chr(175): 1049, chr(176): 1051, chr(177): 1061, chr(178): 1063, chr(179): 1069, 
#         chr(180): 1087, chr(181): 1091, chr(182): 1093, chr(183): 1097, chr(184): 1103, chr(185): 1109, 
#         chr(186): 1117, chr(187): 1123, chr(188): 1129, chr(189): 1151, chr(190): 1153, chr(191): 1163, 
#         chr(192): 1171, chr(193): 1181, chr(194): 1187, chr(195): 1193, chr(196): 1201, chr(197): 1213, 
#         chr(198): 1217, chr(199): 1223, chr(200): 1229, chr(201): 1231, chr(202): 1237, chr(203): 1249, 
#         chr(204): 1259, chr(205): 1277, chr(206): 1279, chr(207): 1283, chr(208): 1289, chr(209): 1291, 
#         chr(210): 1297, chr(211): 1301, chr(212): 1303, chr(213): 1307, chr(214): 1319, chr(215): 1321, 
#         chr(216): 1327, chr(217): 1361, chr(218): 1367, chr(219): 1373, chr(220): 1381, chr(221): 1399, 
#         chr(222): 1409, chr(223): 1423, chr(224): 1427, chr(225): 1429, chr(226): 1433, chr(227): 1439, 
#         chr(228): 1447, chr(229): 1451, chr(230): 1453, chr(231): 1459, chr(232): 1471, chr(233): 1481, 
#         chr(234): 1483, chr(235): 1487, chr(236): 1489, chr(237): 1493, chr(238): 1499, chr(239): 1511, 
#         chr(240): 1523, chr(241): 1531, chr(242): 1543, chr(243): 1549, chr(244): 1553, chr(245): 1559, 
#         chr(246): 1567, chr(247): 1571, chr(248): 1579, chr(249): 1583, chr(250): 1597, chr(251): 1601, 
#         chr(252): 1607, chr(253): 1609, chr(254): 1613, chr(255): 1619
#     }

#     def encode(self, strs: List[str]) -> str:
#         # - We need to combine all the strings and form a bigger string but we also need delimiters to let the decoder
#         #   know where to set the strinsg apart
#         # - Let's look at the behavior we want here:
#         #   - e.g. ["Hello","World"]:
#         #     - "Hello\World" from encoder
#         #     - Decoder receives "Hello\World" and it separates Hello and World due to a \
#         #     - But if we have ["Hello\","World"], then "Hello\\World" causes an issue
#         #       - Decoder sees "Hello\\World" and it separates "Hello" and "\\World"
#         #   - We need the decoder to be smart enough to recognize that it sees a "\" and it changes the delimiter
#         #   - How about we have it do the following:
#         #     - Encoder encodes ["Hello","World"] into the following:
#         #       - Value of "Hello":
#         #         - ASCII(H) = 72, PRIMENUM(H) = 19 -> 72*19*1 = 1398
#         #         - ASCII(e) = 101, PRIMENUM(e) = 11 -> 101*11*2 = 2222
#         #         - ASCII(l) = 108, PRIMENUM(l) = 37 -> 108*37*3 = 11988
#         #         - ASCII(l = 108, PRIMENUM(l) = 37 -> 108*37*4 = 15984
#         #         - ASCII(o) = 111, PRIMENUM(o) = 47 -> 111*47*5 = 26085
#         #       - Value of Hello is 1398 + 2222 + 11988 + 15984 + 26085 = 57677
#         #       - Find value of "World"
#         #     - Encoder turns ["Hello\","World","I'm","Gaurav"] into "Hello|>>76752<<World|I'm|Gaurav|"
#         #     - Decoder receives "Hello|>>76752<<World|I'm|Gaurav|" and does the following:
#         #       - @ H -> "H"!="|" -> ASCII..., PRIME..., INDEX+1, gets a value
#         #       - @ e -> "e"!="|" -> ASCII..., PRIME..., INDEX+1, gets a value
#         #         ...
#         #       - @ \ -> "|"=="|" -> get total of all values collected
#         #                         -> Is next so and so indices == ">>76752<<"?
#         #                            -> If yes, then Add "Hello\" to the final list of strings
#         #                            -> If not, then ASCII..., PRIME..., INDEX+1, gets a value
#         #   ["Hello","World,"I'm", "Saad"] -> "Hello|World|I'm|Saad|"
#         #   ["Hello|","World,"I'm", "Saad"] -> "Hello||World|I'm|Saad|"
#         #   ["Hello|","|World,"I'm","","Saad"] -> "Hello|>>372723<<|World|I'm|>>372723<<Saad|"]

#         # - "6|Hello5|5|World"
#         #   "5|Hello|0||5|World|
#         #   ["5|Hello"]
#         #   ["Hello||", "|World"]

#         # - ["Hello","World,"I'm","Saad"] -> "Hello|375282|World|567562|I'm|3245|Saad|21312|"

#         # encodedString = ""
#         # for string in strs:
#         #     stringToAppend = string
#         #     if(string[-1]=="|"):
#         #         valueOfString = 0
#         #         for index,character in enumerate(string):
#         #             asciiValueOfChar = ord(character)
#         #             primeNumOfChar = self.ascii_to_prime.get(character)
#         #             valueOfString+=(asciiValueOfChar * primeNumOfChar * (index+1))
#         #         stringToAppend+=f">>{valueOfString}<<"
#         #     else:
#         #         stringToAppend+="|"
#         #     encodedString+=str(stringToAppend)
#         # print(encodedString)
#         # return encodedString

#         # - ["Hello","World,"I'm","Saad"] -> "Hello|<375282>|World|<56756>|I'm|<3245>|Saad|<21312>|"
#         # - ["Hello|","|World,"I'm","","Saad"] -> "Hello||<4657567>||World|<464636>|I'm|<3245>||<4657567>|Saad|<21312>|"
#         encodedString = ""
#         currentHighestValue = 0
#         for string in strs:
#             stringToAppend = string
#             if(string!=""):
#                 valueOfString = 0
#                 for index,character in enumerate(string):
#                     asciiValueOfChar = ord(character)
#                     primeNumOfChar = self.ascii_to_prime.get(character)
#                     valueOfString+=(asciiValueOfChar * primeNumOfChar * (index+1))
#                 if valueOfString > currentHighestValue:
#                     currentHighestValue = valueOfString
#                 stringToAppend+=f"|<{valueOfString}>|"
#             else:
#                 stringToAppend+=f"|<{currentHighestValue}>|"
#             encodedString+=str(stringToAppend)
#         return encodedString

#     def decode(self, s: str) -> List[str]:
#         # - ["Hello|","|World,"I'm","","Saad"] -> "Hello||<4657567>||World|<464636>|I'm|<3245>||<4657567>|Saad|<21312>|"
#         # Algorithm:
#         # - trackingIndex = 1
#         # - trackingString = ""
#         # - trackingValue = 0
#         # - currentHighestValue = 0
#         # - originalStrs = []
#         # - Iterate through each character in the string s and for each character:
#         #   - If character is not "|":
#         #     - asciiValueOfChar = ord(character)
#         #     - primeNumOfChar = self.ascii_to_prime.get(character)
#         #     - trackingValue+=(asciiValueOfChar * primeNumOfChar * trackingIndex)
#         #     - trackingString+=character
#         #     - trackingIndex+=1
#         #     - If current trackingValue is larger than currentHighestValue:
#         #       - currentHighestValue = trackingValue
#         #   - Else:
#         #     - If the character at the next index is "<":
#         #       - If s[currentIndex:len(str(trackingValue)+5)]==f"|<{trackingValue}>|":
#         #         - originalStrs.append(trackingString)
#         #         - trackingIndex = 1
#         #         - trackingString = ""
#         #         - trackingValue = 0
#         #       - Else if s[currentIndex:len(str(trackingValue)+5)]==f"|<{currentHighestValue}>|":
#         #         - originalStrs.append(trackingString)
#         #     - Else if the character at the next index is not "<"
#         #       - asciiValueOfChar = ord(character)
#         #       - primeNumOfChar = self.ascii_to_prime.get(character)
#         #       - trackingValue+=(asciiValueOfChar * primeNumOfChar * trackingIndex)
#         #       - trackingString+=character
#         #       - trackingIndex+=1
#         #       - If current trackingValue is larger than currentHighestValue:
#         #         - currentHighestValue = trackingValue
        
#         trackingIndex = 1
#         trackingString = ""
#         trackingValue = 0
#         currentHighestValue = 0
#         originalStrs = []
#         index = 0
#         while index < len(s):
#             asciiValueOfChar = ord(s[index])
#             primeNumOfChar = self.ascii_to_prime.get(s[index])
#             if s[index]!="|":
#                 trackingValue+=(asciiValueOfChar * primeNumOfChar * trackingIndex)
#                 trackingString+=s[index]
#                 trackingIndex+=1
#             else:
#                 if((index+1)<len(s)) and s[index+1]=="<":
#                     delimiterProspect = s[index:index+len(str(trackingValue))+4]
#                     if delimiterProspect==f"|<{trackingValue}>|":
#                         originalStrs.append(trackingString)
#                         trackingIndex = 1
#                         trackingString = ""
#                         trackingValue = 0
#                         index+=(len(f"<{trackingValue}>")+6)
#                     else:
#                         originalStrs.append(trackingString)
#                         index+=(len(f"<{currentHighestValue}>")+6)
#                 elif((index+1)<len(s)) and s[index+1]!="<":
#                     trackingValue+=(asciiValueOfChar * primeNumOfChar * trackingIndex)
#                     trackingString+=s[index]
#                     trackingIndex+=1
#             index+=1
#             if(currentHighestValue < trackingValue):
#                 currentHighestValue = trackingValue
#         return originalStrs

                    
from typing import List

class Solution:
    # Kept your exact prime dictionary
    ascii_to_prime = {
        chr(i): p for i, p in enumerate([
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 
            127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 
            257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 
            401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 
            563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 
            709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 
            877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 
            1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 
            1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 
            1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 
            1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 
            1609, 1613, 1619
        ])
    }

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            valueOfString = 0
            for index, character in enumerate(string):
                asciiValueOfChar = ord(character)
                primeNumOfChar = self.ascii_to_prime.get(character, 1)
                valueOfString += (asciiValueOfChar * primeNumOfChar * (index + 1))
            
            # Form: text|<hash>|
            encodedString += f"{string}|<{valueOfString}>|"
        return encodedString

    def decode(self, s: str) -> List[str]:
        originalStrs = []
        
        trackingString = ""
        trackingValue = 0
        trackingIndex = 1
        
        index = 0
        while index < len(s):
            # Check if we are potentially looking at a delimiter signature
            if s[index] == '|' and (index + 1) < len(s) and s[index + 1] == '<':
                expected_delimiter = f"|<{trackingValue}>|"
                delimiter_length = len(expected_delimiter)
                
                # Check if the text matches our calculated hash token exactly
                if s[index:index + delimiter_length] == expected_delimiter:
                    originalStrs.append(trackingString)
                    
                    # Advance the pointer past the entire delimiter length
                    index += delimiter_length
                    
                    # Reset trackers for the next string block
                    trackingString = ""
                    trackingValue = 0
                    trackingIndex = 1
                    continue  # Bypass the standard +1 index advance at the bottom
            
            # If it's regular text, process it using your hash algorithm
            asciiValueOfChar = ord(s[index])
            primeNumOfChar = self.ascii_to_prime.get(s[index], 1)
            trackingValue += (asciiValueOfChar * primeNumOfChar * trackingIndex)
            
            trackingString += s[index]
            trackingIndex += 1
            index += 1
            
        return originalStrs