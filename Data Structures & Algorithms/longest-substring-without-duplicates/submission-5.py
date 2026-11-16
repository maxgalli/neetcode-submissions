class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #mx = 0
        #l = 0
        #r = 1
        #dim = len(s)
        #while r <= dim:
        #    substring = s[l:r]
        #    if substring == "".join(dict.fromkeys(substring)):
        #        if len(substring) > mx:
        #            mx = len(substring)
        #        r += 1
        #    else:
        #        l += 1
        #return mx
        seen = set()
        add, rem = seen.add, seen.remove   # skip the method lookup each iteration
        mx = l = r = 0
        n = len(s)                          # compute length once
        while r < n:
            c = s[r]
            if c not in seen:
                add(c)
                r += 1
                if r - l > mx:              # a plain if is faster than calling max()
                    mx = r - l
            else:
                rem(s[l])
                l += 1
        return mx