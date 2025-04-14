class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        Generate all combinations of well-formed parentheses for n pairs.
        
        Args:
            n (int): Number of pairs of parentheses.
            
        Returns:
            List[str]: A list of all valid combinations.
        """
        results = []

        def backtrack(current: str, open_count: int, close_count: int) -> None:
            print("Current: ", current, "result: ", results)

            # Base Case: If the current string has reached the length of 2*n,
            # it means we've used all pairs of parentheses.
            if len(current) == 2 * n:
                results.append(current)  # Add the complete combination to the results.
                print("finished combo: ",current)
                return

            # If we can add an open parenthesis (i.e., we haven't used all n yet),
            # then add '(' and increment the open_count.
            if open_count < n:
                print("checking to add (")
                backtrack(current + "(", open_count + 1, close_count)

            # If we can add a closing parenthesis without violating the rules
            # (i.e., there are more open than close parentheses),
            # then add ')' and increment the close_count.
            if close_count < open_count:
                print("checking to add )")
                backtrack(current + ")", open_count, close_count + 1)
            
            print("End of backtrack iteration, current: ", current)


        # Start the backtracking process with an empty string and 0 counts for both open and close.
        backtrack("", 0, 0)

        print("Done backtrack")
        return results

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    n=2
    combinations = solution.generateParenthesis(n)  # Ensure the method name is correct here
    print(f"All well-formed parentheses combinations for {n} pairs:")
    for combo in combinations:
        print(combo)