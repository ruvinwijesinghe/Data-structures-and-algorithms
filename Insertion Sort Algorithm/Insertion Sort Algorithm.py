def insertion_sort(list):
    looping_length = range(1,len(list))
    for i in looping_length:
        key=list[i];
        while list[i-1]>key and i>0:
            list[i],list[i-1]=list[i-1],list[i]
            i=i-1
    return list

print(insertion_sort([7,10,2,8,9,1,78]))
