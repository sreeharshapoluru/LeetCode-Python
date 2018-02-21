class Anagram(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        arr1 = list(s);
        arr2 = list(t);
        size1 = len(arr1);
        size2 = len(arr2);
        if(size1 != size2):
            return False;
        store = {};
        for i in range(size1):
            if arr1[i] in store:
                store[arr1[i]] += 1;
            else:
                store[arr1[i]] = 1;
        for i in range(size2):
            if arr2[i] in store:
                store[arr2[i]] -= 1;
                if(store[arr2[i]] < 0):
                    return False;
        for k,v in store.items():
            if(v!=0):
                return False;
        return True;
            