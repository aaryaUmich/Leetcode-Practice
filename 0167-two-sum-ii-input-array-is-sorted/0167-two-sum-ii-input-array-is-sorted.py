class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while(left<right):
            answer = numbers[left]+numbers[right]
            if answer==target:
                return [left+1, right+1]
            elif answer<target:
                left+=1
            elif answer>target:
                right-=1
            