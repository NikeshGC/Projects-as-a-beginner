#my first module in machine learning
x=[2,3,4,5,6,7,8, 9, 10]
y=[4,6,8,10,12,14,16,18, 20]
m = 0
c=0
learning_rate= 0.01
for iteration in range(1000):
 #prediction
 pre=[]
 for i in range(len(x)):
    pre_y= m* x[i]+c 
    pre.append(pre_y)
 #loss calculation
 loss=0
 for i in range(len(pre)):
    loss=loss+(pre[i]-y[i])**2
 loss=loss/len(pre)
 #gradident
 dm=0
 dc=0
 for i in range(len(x)):
    dm=dm+(pre[i]-y[i])*(+2)*x[i]
    dc=dc+(pre[i]-y[i])*(2)
 dm=dm/len(x)
 dc=dc/len(x)

 #update
 m=m-learning_rate*dm
 c=c-learning_rate*dc

print(m)
print(c)
o=int(input("Enter the number:"))
out=m*o+c
print(f"The outupt is {out}")