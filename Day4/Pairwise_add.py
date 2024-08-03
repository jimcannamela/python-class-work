list1=[1,2,3,4]
list2=[4,5,6,7]
list3=[100,200,300]
list4=[10,1,180]

newlist1=[]
newlist2=[]

def pairwise_add(list1, list2):
    newlist=[]
    for a,b in zip(list1,list2):
        newlist.append(a+b)
    return newlist