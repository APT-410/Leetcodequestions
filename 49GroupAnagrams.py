import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        cols_dict=collections.defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            cols_dict[sorted_word].append(word)
        
        return list(cols_dict.values())
            


if __name__ == "__main__":
    test_case1 = ["eat","tea","tan","ate","nat","bat"]
    test_case2 = [""]
    test_case3 = ["a"]
    solution = Solution()
    print(solution.groupAnagrams(test_case1))
    print(solution.groupAnagrams(test_case2))
    print(solution.groupAnagrams(test_case3))