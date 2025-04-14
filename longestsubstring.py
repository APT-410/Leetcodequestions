class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        This will be given a string and will return the length of the longest substring without repeating characters.
        """
        char_index = {}  # This dictionary will store the most recent index of each character.
        max_length = 0   # This variable will record the length of the longest substring found so far.
        start = 0        # 'start' marks the beginning of our current substring (or "window") without duplicates.

        for i, char in enumerate(s):
            # Check if the character has been seen before AND if its last seen index is within the current window.
            if char in char_index and char_index[char] >= start:
                # If both conditions are true, it means the current character is a duplicate within our current window.
                # To remove the duplicate, we move the start of the window to one position after the previous occurrence.
                start = char_index[char] + 1

            # Update the dictionary with the current index for this character.
            char_index[char] = i

            # Calculate the length of the current window (substring) and update max_length if it's longer.
            max_length = max(max_length, i - start + 1)
            print("current postition index", i ," char: ",char, "\nchar_index: ",char_index, "\nStart: ",start,"\nchar_index[char]: ", char_index[char] if char in char_index else None)
            print("Max Length: ",max_length, "\n")
        return max_length

if __name__ == "__main__":
    solution = Solution()
    test_string = "abcabcbb"
    #solution.lengthOfLongestSubstring(test_string)
    result = solution.lengthOfLongestSubstring(test_string)
    print(f"The length of the longest substring without repeating characters is: {result}")