l=[]
def createList():
    for i in range(5):
        s=input("Enter string:")
        l.append(s)
        
def length(l):
    v=0
    for i in l:
        for j in i:
            v=v+1
        print(v)
        v-=v
    createList()
length(l)
