e=[]
y=int(input("Enter the no.of records:"))

for i in range (y):
     t=input("Enter the record (Roll no, Name, Marks):")
     s=t.split()
     d=list(s)
     e.append(d)
print("Roll no", "Name", "Marks", sep='   ')
for i in e:
    print(i[0], i[1], i[2], sep=' ')
print('ii')
l = e[1]
print(l[0], l[1], l[2], sep='   ')
