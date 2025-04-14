class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length_of_nums= len(nums)

        ## error handling check first to see if 
        if length_of_nums < 2:
            raise ValueError("You did not enter more than two values")
        
        first_index =0

        # first loop to go through the first index
        while first_index != length_of_nums-1:
            #set second index at beginning of loop so its always one ahead of the first index
            second_index = first_index+1

            #second loop to go through the second 
            while second_index != length_of_nums:
                sum = nums[first_index] + nums[second_index]

                print("Index 1 second loop: ",first_index, "value index 1: ", nums[first_index])
                print("Index 2 second loop: ",second_index, "value index 2: ", nums[second_index])
                print("Sum is: ",sum)
                if(sum==target):
                    return [first_index,second_index]
                #bump inner index for the second up
                second_index+=1

            #add one to bump the index for the first to the next level
            first_index+=1





# Example usage:
if __name__ == "__main__":
    solution = Solution()
    combinations = solution.twoSum(nums = [3,2,4], target = 6)  # Ensure the method name is correct here
    print("Answer is :",combinations)