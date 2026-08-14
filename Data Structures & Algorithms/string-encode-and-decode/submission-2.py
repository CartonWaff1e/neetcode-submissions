
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for st in strs:
            encoded += str(len(st)) + "#" + st
        return encoded


    def decode(self, s: str) -> List[str]:
        decode = list()
        i = j = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decode.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return decode
            


        
        
            
        
        
           
       



        

        
        

   


