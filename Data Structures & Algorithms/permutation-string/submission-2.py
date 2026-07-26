class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count_s1 = {}
        window = {}
        for i in range(len(s1)):
            count_s1[s1[i]] = 1 + count_s1.get(s1[i], 0)
            window[s2[i]] = 1 + window.get(s2[i], 0)
        
        l = 0
        if window == count_s1:
                return True

        for r in range(len(s1), len(s2)):
            
            window[s2[r]] = 1 + window.get(s2[r], 0)
            window[s2[l]] -= 1

            if window[s2[l]] == 0:
                del window[s2[l]]
                
            if window == count_s1:
                return True
            l += 1
        return False


