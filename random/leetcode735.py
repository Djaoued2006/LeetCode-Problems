class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        length = len(asteroids)

        result = [asteroids[0]]

        size = 1

        i = 1

        while (i < length):
            if (asteroids[i] * result[size - 1] >= 0):
                result.append(asteroids[i])
                size += 1
                i += 1
            else :
                j = size - 1

                while (j >= 0):
                    if (size == 0):
                        result.append(asteroids[i])
                    else :
                        while (abs(asteroids[i]) > abs(result[j])):
                            result.pop()
                            size -= 1
                            j -= 1
                        else :
                            if (abs(asteroids[i]) == abs(result[j])) :
                                result.pop()
                                size -= 1
                            else :
                                if (result[j] * asteroids[i] >= 0) :
                                    result.append(asteroids[i])
                                    size += 1
                                else : 
                                    break

            i += 1 
        
        return result


array = [10,-12]
print(Solution().asteroidCollision(array))

                    

