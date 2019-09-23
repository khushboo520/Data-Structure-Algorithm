def longestPalindrome(s):
    l=0
    dictP={}
    dictC={}
    end=0
    st=0
    e=0
    while end < len(s):
        if s[end]  in dictC:
            start=dictC[s[end]]
            if(start+1 in dictP and end== dictP[start+1]+1):
                if(l> end-start+1):
                    st=start
                    e=end
                dictP(start, end)

            else:
                t=end
                isPalindrom=True
                while(start <=t):
                    if(s[start]!=s[t]):
                        isPalindrom=False
                        break;
                    start+=1
                    t-=1
                if(isPalindrom):
                    if (l < end - start + 1):
                        st = dictC[s[end]]
                        e = end
                    dictP[s[end]]=t
        else:
           dictC[s[end]] = end
        end+=1


    return s[st:e+1]

print("found "+ longestPalindrome("cccabbac"))