#ques4
a =input()
b= ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','n','p','q','r','s','t',' ','u','v','w','x','y','z']
c=[]
for i in a:
    if i not in c:
        c.append(i)
    
if sorted(b)==sorted(c):
    print('yes')
else:
    print("no")