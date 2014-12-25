class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        size1 = len(word1)
        size2 = len(word2)
        m = {}
        for i in range(0,size1+1):
            m[(0,i)] = i
        for i in range(1,size2+1):
            m[(i,0)] = i
        for i  in range(1,size2+1):
            for j in range(1,size1+1):
                mymin = min(m[(i-1,j)]+1, m[(i,j-1)] + 1)
                temp = m[(i-1,j-1)] +  (0 if word1[j-1]==word2[i-1] else 1)
                mymin = min(temp,mymin)
                m[(i,j)] = mymin
                #print i,j,mymin
        return m[(size2,size1)]

s = Solution()
print s.minDistance("failing","sailn")
print s.minDistance("","")
                        
