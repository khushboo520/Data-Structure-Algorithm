class Solution:
    def convert(self, s, numRows):
        l = {}
        goDown = False
        pos = 1
        if numRows == 1:
            return s
        for c in s:
            if pos not in l:
                l[pos] = c
            else:
                l[pos] += c
            if pos == 1 or pos == numRows:
                goDown =  False if goDown   else  True
            pos += 1 if goDown else -1

        so = "".join(x for x in l.values())

        return so
s=Solution()
print(s.convert("PAYPALISHIRING",3))