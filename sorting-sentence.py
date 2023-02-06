class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split()
 
        for i in range(1,len(words)):
            key=words[i]
        
            j=i-1
            while j>=0 and int(key[-1])<int(words[j][-1]):
                words[j+1]=words[j]
                j-=1
            words[j+1]=key
        ns=''
        for word in words:

            ns=ns+' '+word[:-1]
        return ns.lstrip()
