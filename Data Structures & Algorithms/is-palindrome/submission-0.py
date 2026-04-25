class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''.join([x.lower() for x in s if x.isalnum()])
        return temp == temp[::-1] 