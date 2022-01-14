maxMinAnno=[]
#maxMinAnno.append("2011")
maxMinAnno.append(80)
#maxMinAnno.append("2012")
maxMinAnno.append(33)
#maxMinAnno.append("2013")
maxMinAnno.append(90)
#maxMinAnno.append("2014")
maxMinAnno.append(24)
#maxMinAnno.append("2015")
maxMinAnno.append(1)
#maxMinAnno.append("2016")
maxMinAnno.append(36)

"""print(maxMinAnno)
max= max(maxMinAnno)
min= min(maxMinAnno)
print(max)
print(min)"""
i=0
max = maxMinAnno[0]
min = maxMinAnno[0]
while(i < 6):
    if(maxMinAnno[i]>max):
        max=maxMinAnno[i]
    if(maxMinAnno[i]<min):
        min=maxMinAnno[i]
    i+=1

print(max)
print(min)



maxMinAnno=[]
sA1,sA2,sA3,sA4,sA5,sA6=0,0,0,0,0,0
due = 2
for k in range(176):
    if(spesaMeseAnno[k]=="2011"):
        sA1=sA1+(spesaMeseAnno[due])
        due = due+3
    if(spesaMeseAnno[k]=="2012"):
        sA2=sA2+(spesaMeseAnno[due])
        due = due+3
    if(spesaMeseAnno[k]=="2013"):
        sA3=sA3+(spesaMeseAnno[due])
        due = due+3
    if(spesaMeseAnno[k]=="2014"):
        sA4=sA4+(spesaMeseAnno[due])
        due = due+3
    if(spesaMeseAnno[k]=="2015"):
        sA5=sA5+(spesaMeseAnno[due])
        due = due+3
    if(spesaMeseAnno[k]=="2016"):
        sA6=sA6+(spesaMeseAnno[due])
        due = due+3

maxMinAnno.append(sA1)
maxMinAnno.append(sA2)
maxMinAnno.append(sA3)
maxMinAnno.append(sA4)
maxMinAnno.append(sA5)
maxMinAnno.append(sA6)

print(maxMinAnno)
i=0
maxDIM = maxMinAnno[0]
minDIM = maxMinAnno[0]
while(i < 6):
    if(maxMinAnno[i] > max):
        maxDIM=maxMinAnno[i]
    if(maxMinAnno[i] < min):
        minDIM=maxMinAnno[i]
    i+=1

print(maxDIM)
print(minDIM)


   