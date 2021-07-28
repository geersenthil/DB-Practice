class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNeg = False
        if (x<0):
            isNeg = True
            x=-x
        reversedNum = 0
        while x:
            reversedNum = 10 * reversedNum + (x % 10)
            x//=10
        if reversedNum >= 2 ** 31 - 1 or reversedNum <= -2 ** 31:
            return 0
        return -reversedNum if isNeg else reversedNum
  