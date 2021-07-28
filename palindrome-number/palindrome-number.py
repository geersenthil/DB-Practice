class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        isPal = True
        reversedNum = 0
        originalNum = x
        while (x > 0):
            reversedNum = 10 * reversedNum + (x % 10)
            x//=10
        if reversedNum != originalNum:
            isPal = False
        return isPal