class Solution:
    def removeStars(self, s: str) -> str:
        l = len(s)
        st = [''] * l
        j = 0

        for i in range(l):
            if s[i] == '*':
                if j:
                    j -= 1
                    
            else:
                st[j] = s[i]
                j += 1
        
        return "".join(st[:j])
    
# class Solution:
#     def removeStars(self, s: str) -> str:
#         st = []
#         l = len(s)

#         for i in range(l):
#             if s[i] == '*':
#                 if st:
#                     st.pop()
#             else:
#                 st.append(s[i])
        
#         return "".join(st)

print(Solution().removeStars("leet**cod*e"))
