##Question link: https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        current = n
        sum = 0
        sum_list = []  # keep track of all sums

        while sum != 1:  # if number is not happy we keep processing current
            sum = 0
            while current > 0:  # keep summing
                sum += (current % 10) * (current % 10)  # squaring last digit
                current = current // 10  # get rid of last digit

            if sum in sum_list:
                return False
            else:
                sum_list.append(sum)

            current = sum  # reset sum

        return True

#Reflection:
#When there are multiple variables, need to keep track of their value each time a loop is run.
