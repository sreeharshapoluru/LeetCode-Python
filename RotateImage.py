class RotateImage(object):
    
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        
        """
        size = len(matrix);
        for i in range(size):
            for j in range(i+1,size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(size):
            j = 0;k=size-1;
            while(j<=k):
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
                j+=1;
                k-=1;
    
    
        