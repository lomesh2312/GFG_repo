from collections import Counter

class Solution:
    def smallestWindow(self, s, p):
        need = Counter(p)
        window = {}
        have, need_count = 0, len(need)
        
        res = ""
        res_len = float('inf')
        left = 0
        
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            
            if c in need and window[c] == need[c]:
                have += 1
            
            # Try to shrink the window when all chars are matched
            while have == need_count:
                window_len = right - left + 1
                if window_len < res_len:
                    res_len = window_len
                    res = s[left:right+1]
                
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1
        
        return res
