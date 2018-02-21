class IntRev(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x >= -9 and x <=9):
            return x;
        xString = str(x);
        strArray = list(xString);
        i =0;
        j = len(xString)-1;
        if(x < 0):
            i =1;
        while(i < j):
            strArray[i], strArray[j] = strArray[j], strArray[i];
            i +=1;
            j -=1;
        ret = ''.join(strArray);
        result = int(ret);
        if(abs(result) > (2**31)-1):
            return 0;
        else:
            return result;
            
        
        