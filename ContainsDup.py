class ContainsDup(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result =False;
        size = len(nums);
        store = {};
        for i in range(size):
            if(nums[i] in store):
                result = True;
                break;
            else:
                store[nums[i]] = 1;
        return result;
        