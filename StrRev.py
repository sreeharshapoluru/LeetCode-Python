class StrRev(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(len(s) == 1):
            return s;
        strArray = list(s);
        size = len(strArray);
        i=0;
        j=size-1;
        while(i < j):
            strArray[i], strArray[j] = strArray[j], strArray[i];
            i += 1;
            j -= 1;
        retString  = ''.join(strArray);
        return retString;