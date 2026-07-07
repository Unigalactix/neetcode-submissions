class Solution:

    def encode(self, strs: List[str]) -> str:
        result =""
        for word in strs:
            result += str(len(word))+"#"+word
        return result

    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            start_of_word = j+1
            end_of_word = start_of_word+length
            result.append(s[start_of_word:end_of_word])
            i=end_of_word
        return result