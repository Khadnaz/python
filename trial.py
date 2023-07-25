f =  open(r"C:\Users\User\Documents\Learnings\Python_scripts\xyz.txt","w")

x = 5

for i in range(1,11):
    f.write(" " + str(x) + ' X \t'+ str(i) + ' = '+ str(x*i) + "\n"  )
    print(x,'X',i,'=',x*i)
    