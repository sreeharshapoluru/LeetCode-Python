class PerNum(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if(num <= 1):
            return False;
        ret = 1;
        for i in range(2,int(num ** (0.5))+1):
            if(num % i == 0):
                ret += i;
                if(i != num/i):
                    ret += num/i;
        
        return (ret == num);
    
        