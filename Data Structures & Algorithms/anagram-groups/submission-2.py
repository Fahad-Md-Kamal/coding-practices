class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmpDict = {}
        
        for wrd in strs:
            ordWrd = "".join(sorted(wrd))
            if ordWrd in tmpDict:
                tmpDict[ordWrd].append(wrd)
            else:
                tmpDict[ordWrd] = tmpDict.get(ordWrd, [wrd])
            
        return list(tmpDict.values())