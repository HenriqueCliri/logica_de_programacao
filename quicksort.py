
def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pic = list[0]
        min = [i for i in list[1:] if i <= pic]
        max = [i for i in list[1:] if i > pic]
        return quicksort(min) + [pic] + quicksort(max)


arr = [5,1,2,1,6,3]
print(quicksort(arr))