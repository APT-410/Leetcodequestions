
"""
plusone.py

Given a list of digits representing a non-negative integer (most significant
digit first), add one to the integer and return the resulting list of digits.

Example: [1,2,9] -> [1,3,0]

Approach:
```
Code block
```# Approach
I began thinking about this problem by breaking down how I would do this on paper. 
1. I will need to add 1 to the right most item in the list. 
2. First edge case: But what if the number was 9? And then the next?
3. We will need to check then the next integer to the left of it to see if its also 9, we will need to keep doing this until we dont hit a nine.
4. Second edge case: Then what if every item in the list is also a nine?
5. We will have to in this case make all current digits 0 and then add 1 to the beginning

Implementing the code
6. So starting now to think about the code i want to reverse iterate through all the items of the list with a for loop, range(start(the right most item),end (same place right most), step instead of 1 to move to the right we want to move left with -1)
7. We'll then check if each is less than 9 if it is we add one and return the list. If its not we will skip this and zero this out and go to the left one to to check if its 9, since the 1 carries over
8. If we now reach the end that means its all 9's and we will need ot manually insert at the beginning a new integer in the list of integers and this will be 1
"""

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Iterate backwards so we handle the least-significant digit first. The range piece = (start, stop, step)
        # start at the end of the list (right most) and most to the left and stop at the original end of the list
        for i in range(len(digits) - 1, -1, -1):
            # If current digit is not 9 we can safely increment and return.
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # Current digit is 9: it becomes 0 and we carry 1 to the next digit.
            digits[i] = 0

        # If we get here every digit was 9 (e.g. [9,9]) and turned into 0s.
        # Prepend 1 to represent the carried overflow: [9,9] -> [1,0,0].
        digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    # Quick manual test: expected output for [1,2,9,9] is [1,3,0,0]
    sol = Solution()
    testcase = [9, 9, 9, 9]
    print(sol.plusOne(digits=testcase))