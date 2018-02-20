class PlusOne(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result =0;
        carry = 0;
        size = len(digits);
        for i in reversed(range(size)):
            if(i == size-1):
                result = digits[i] + 1 + carry;
            else:
                result = digits[i] + carry;
            if(result > 9):
                digits[i] = result % 10;
                carry = result/10;
                if(i == 0):
                    returnArray = [None]*(size+1);
                    returnArray[0] = carry;
                    for i in range(size):
                        returnArray[i+1] = digits[i];
                    return returnArray;
            else:
                digits[i] = result;
            
            return digits;
        