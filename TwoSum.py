class TwoSum(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        returnArray = [0,0];
        store = {};
        for i in range(len(nums)):
            if(target - nums[i] in store):
                if( i < store[target - nums[i]]):
                    returnArray[0] = i;
                    returnArray[1] = store[target - nums[i]];
                else:
                    returnArray[1] = i;
                    returnArray[0] = store[target - nums[i]];
            else:
                store[nums[i]] = i;
        
        return returnArray;