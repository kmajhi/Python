class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        dic = {}
        sortedNum = sorted(nums)
        ans = []

        for i in range(len(sortedNum)):
            if sortedNum[i] not in dic :
                dic[sortedNum[i]] = i

        for num in nums:
            ans.append(dic[num])
        return ans
