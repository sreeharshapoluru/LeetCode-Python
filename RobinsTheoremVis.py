import math;
import matplotlib.pyplot as plt;

plot1 = [0] * 9998;
plot2 = [0] * 9998;
plot3 = [0] * 9998;
constant = 1.781974;
for i in range(2,10000):
    lhs = 0;
    rhs = 0;
    logTerms = i*(math.log(math.log(i)));
    rhs = constant*logTerms;
    for j in range(1,i+1):
        if(i%j == 0):
            lhs = lhs+j;
    plot1[i-2] = i;
    plot2[i-2] = lhs;
    plot3[i-2] = rhs;

plt.plot(plot1,plot2,'r');
plt.plot(plot1,plot3,'b');
plt.show();







