class Solution:
    def restoreIpAddresses(self, ip_string: str) -> list[str]:
        # Validate input length.
        # if len(ip_string) < 4 or len(ip_string) > 20:
         #   raise ValueError("Input string length must be between 4 and 20")
        
        ip_list = []  # List to store valid IP addresses.

        def backtrack(start: int, segments: list[str]) -> None:
            # If we have 4 segments and have used all characters, it's a valid IP.
            if len(segments) == 4:
                if start == len(ip_string):
                    ip_list.append(".".join(segments))
                return

            # Try segments of length 1 to 3.
            for length in range(1, 4):
                if start + length > len(ip_string):
                    break

                segment = ip_string[start:start + length]

                # Skip segments with leading zeros (unless the segment is "0").
                if len(segment) > 1 and segment[0] == '0':
                    continue

                # Convert the segment to integer and check its range.
                if int(segment) > 255:
                    continue

                # Continue backtracking with the next part of the string.
                backtrack(start + length, segments + [segment])

        backtrack(0, [])
        return ip_list

if __name__ == "__main__":
    sol = Solution()
    test = "25525511135"
    result = sol.restoreIpAddresses(test)
    print(result)  # Expected output: ["255.255.11.135", "255.255.111.35"]
