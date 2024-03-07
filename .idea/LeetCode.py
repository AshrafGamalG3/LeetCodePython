import roman
from typing import List
def subtractProductAndSum(self, n: int) -> int:
    sum=0
    m=1
    while n>0:
        x=n%10

        sum+=x
        m*=x

        n=n//10

    return m-sum



# print(subtractProductAndSum(None,234))
def reverseString(self, s: List[str]) -> None:
       f=0
       l=len(s)-1
       while(f<l):
           s[f],s[l]=s[l],s[f]

           f+=1
           l-=1
s = ["h", "e", "l", "l", "o"]
reverseString(None,s)
def reverseWords(self, s: str) -> str:
    l=s.split()
    return " ".join(l[::-1])

# print(reverseWords(None,"the sky     is blue"))
def fizzBuzz(self, n: int) -> List[str]:
    l=[]
    i=1
    while i<=n:
        if i%3==0  and i%5==0:
            l.append("FizzBuzz")
        elif i%3==0:
            l.append("Fizz")
        elif i%5==0:
            l.append("Buzz")
        else: l.append(str(i))
        i+=1
    return  l
def maximumWealth(self, accounts: List[List[int]]) -> int:
    m=0
    for i in accounts:
        m=max(m,sum(i))
    return m
# print(maximumWealth(None,[[1,2,3],[3,2,1]]))
def reverseVowels(self, s: str) -> str:
    vowels = "AEIOUaeiou"
    l = list(s)
    i, j = 0, len(s) - 1

    while i < j:
        if s[i] in vowels and s[j] in vowels:
            l[i], l[j] = s[j], s[i]
            i += 1
            j -= 1
        elif s[i] not in vowels:
            i += 1
        elif s[j] not in vowels:
            j -= 1

    return ''.join(l)
# print(reverseVowels(None,"hello"))
def isSubsequence(self, s: str, t: str) -> bool:
    o, p = 0, 0

    while o < len(s) and p < len(t):
        if s[o] == t[p]:
            o += 1
        p += 1

    return o == len(s)
# print(isSubsequence(None,"acb","ahbgdc"))
def isPalindrome(self, s: str) -> bool:
    s=s.lower()

    b=""
    for i in s:
        if i.isalnum():# a to z and 0-9
            b+=i


    return  b==b[::-1]
# print(isPalindrome(None,"0P"))
def moveZeroes(self, nums: List[int]) -> None:
            l=[]

            for i in nums:
                if i!=0:
                    l.append(i)

            o=len(nums)-len(l)
            l.extend([0]*o)
            for i in range(len(nums)):
                nums[i] = l[i]
            return nums
# print(moveZeroes(None,[0,1,0,3,12]))


def search(self, nums: List[int], target: int) -> int:
    try:
        return nums.index(target)
    except:
        return -1
# print(search(None, [-1, 0, 3, 5, 9, 12], 2))
def search(self, nums: List[int], target: int) -> int:
    s=0
    l=len(nums)-1

    while s<=l:
        m = (s + l) // 2
        if(nums[m]==target):
            return m
        elif(nums[m]>target):
            l=m-1
        else:
            s=m+1

    return -1



# print(search(None, [-1, 0, 3, 5, 9, 12], 2))


def findKthLargest(self, nums: List[int], k: int) -> int:
    nums.sort(reverse=True)
    if k <= 0 or k > len(nums):
        return None
    return nums[k - 1]

# print(findKthLargest(None,[1],1))


def romanToInt(self, s: str) -> int:
    return roman.fromRoman(s)


# print(romanToInt(None,"III"))

def removeStars(self, s: str) -> str:
    l = list(s)
    v=[]
    p=1

    for i in s:

        if i == '*':
            v.pop()
        else:
            v.append(i)

    return  ''.join(v)




# print(removeStars(None,"leet**cod*e"))

def findJudge(self, n: int, trust: List[List[int]]) -> int:
    x = [0] * (n + 1)
    y = [0] * (n + 1)

    for a, b in trust:
        y[a] += 1
        x[b] += 1
    print(x)
    print(y)
    for i in range(1, n + 1):
        if x[i] == n - 1 and y[i] == 0:

            return i

    return -1
# print(findJudge(None,3,[[1,3],[2,3]]))


def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    # l=[]
    # # q = list(map(lambda i: i + extraCandies, candies))
    #
    # for i in range(len(candies)):
    #     candies[i]=candies[i]+extraCandies
    #
    #     if max(candies)==candies[i] :
    #         candies[i]=candies[i]-extraCandies
    #         l.append(True)
    #     else:
    #         candies[i] = candies[i] - extraCandies
    #         l.append(False)
    #
    #
    # return  l

        l=[]
# q = list(map(lambda i: i + extraCandies, candies))
        m=max(candies)
        for i in candies:
            if i+extraCandies>=m :
                l.append(True)
            else:
                l.append(False)
        return  l

# print(kidsWithCandies(None,[2,3,5,1,3],3))