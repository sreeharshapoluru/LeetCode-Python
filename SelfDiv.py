class SelfDiv(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        retList = [];
        for i in range(left,right+1):
            copy = i;
            while(copy > 0):
                div = copy % 10;
                if(div == 0 or i % div != 0):
                    break;
                copy = copy//10;
                if(copy == 0):
                    retList.append(i);
        return retList;
        