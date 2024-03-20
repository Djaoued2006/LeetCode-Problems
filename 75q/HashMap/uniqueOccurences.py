class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        l = len(arr)
        nocc = dict()

        for i in range(l):
            if arr[i] in nocc:
                nocc[arr[i]] += 1
            else:
                nocc[arr[i]] = 1
        
        occ = dict()

        for key in nocc:
            if nocc[key] in occ:
                return False
            else:
                occ[nocc[key]] = True

        return True
        

    
        return True

        