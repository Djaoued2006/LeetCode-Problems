class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st = []
        l = len(asteroids)
        value = 0

        if l == 1:
            return asteroids

        for i in range(l):
            curr = asteroids[i]
            
            if st:
                while st:
                    value = st.pop()

                    if value * curr > 0:
                        st.append(value)
                        st.append(curr)
                        break
                    else:
                        if abs(value) == abs(curr):
                            break
                        else:
                            if abs(value) > abs(curr):
                                st.append(value)
                                break
                
                if value * curr < 0 and abs(value) < abs(curr):
                    st.append(curr)
            else:
                st.append(curr)  

        return st

print(Solution().asteroidCollision([10,2,-5]))
