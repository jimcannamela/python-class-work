def add_csv_lines(csv_lines):
    outlist=[]
    for x in range(len(csv_lines)):     
        newlist=csv_lines[x].split(',')
        print(newlist)
        mysum=0
        for y in range(len(newlist)):
            print(f"Newlist Item Type: {type(newlist[y])} Item: {newlist[y]} Type: {type(int(newlist[y]))}")
            mysum+=int(newlist[y])
        print(f"x: {x} sum: {mysum}")
        outlist.append(mysum)
    return outlist

add_csv_lines([])
add_csv_lines(['1,2,10', '3', '100,1,3'])
add_csv_lines(['1,2,10'])