class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for i in strs:
            en = en + str(len(i))+"#"+i

        return en
            

    def decode(self, s: str) -> List[str]:

        de = []
        i=0

        while i <len(s):
            j = i
            while s[j] != "#":
                j+=1
            le = int(s[i:j])
            i =j+1
            j= i+ le
            de.append(s[i:j])
            i = j
        return de
                
