s1 = input("enter string s1: ")
s2 = input("enter string s2: ")

m = len(s1)
n = len(s2)

#Brute Force -
'''
def LCS(s1,s2,m,n):
    lcs = [[0 for i in range(n+1)] for j in range(m+1)]
    ans = 0

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
                ans = max(ans,lcs[i][j])
            else:
                lcs[i][j] = 0

    return ans

print(LCS(s1,s2,m,n))
'''

#Recursion - Time Complexity and Space Complexity = O(m*n)

def LCS(i,j,count):

    if i == 0 or j == 0:
        return count

    if s1[i-1] == s2[j-1]:
        count = LCS(i-1,j-1,count + 1)
    count = max(count, max(LCS(i,j-1,0) , LCS(i-1,j,0)))
    return count

print(LCS(m,n,0))
