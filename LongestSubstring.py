class Solution:
    def lengthOfLongestSubstring(self, s) :
        l = 0
        d = dict()
        start, end = 0, 0

        l = 0
        d = dict()
        start, end = 0, 0

        while end < len(s):
            if s[end] in d:

                print('before', start)
                start = max(d[s[end]] + 1, start)

            l = max(l, end - start + 1)
            print(d)
            print('length',l)
            print('after',start)


            d[s[end]] = end
            end += 1

        return l

S=Solution()
print(S.lengthOfLongestSubstring("abcb")) #bcdeccbag"))