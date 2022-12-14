#coding="utf-8"
#7，编码循环打印列表中的内容[1,2,3,4,55,66,77,88]
dist=[1,2,3,4,55,66,77,88]
for i in dist:
    print(i)
sum=0
for i in range(100,201):
    sum=sum+i;
    continue
print(sum)

dist1=[1,99,77,3,6,10,99,45]
# dist1.sort()
# print(dist1)
i=0
for i in range(0,len(dist1)-1):
    for j in range(i+1,len(dist1)):
        if dist1[i]<dist1[j]:
            dist1[i],dist1[j]=dist1[j],dist1[i]
        print("小循环第%s,%s次"%(i,j),dist1)
    print("大循环第%s次"%(i+1),dist1)
print("循环结束",dist1)




