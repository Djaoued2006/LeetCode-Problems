class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        l1 = len(word1)
        l2 = len(word2)

        dict1 = dict()
        dict2 = dict()

        for i in range(l1):
            if word1[i] in dict1:
                dict1[word1[i]] += 1
            else: 
                dict1[word1[i]] = 1
        
        for i in range(l2):
            if word2[i] in dict2:
                dict2[word2[i]] += 1
            else: 
                dict2[word2[i]] = 1
            
        for key in dict1:
            if key not in dict2:
                return False

        for key in dict2:
            if key not in dict1:
                return False

        