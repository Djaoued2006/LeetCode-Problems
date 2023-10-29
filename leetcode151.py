class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.strip() + " "

        length = len(s)
        i = 0

        result = ""
        word = ""
        arr = []

        while True:

            if i == length: 
                break
            
            if s[i] != " " :
                word += s[i]
            else :
                if word != "":
                    result = word +  " " + result
                    word = ""
            
            i += 1
            
        return result[0 , len(result)-1]



                
            
            
            
            


            

            
print(Solution().reverseWords("hello     that is me"))
          
                
            
