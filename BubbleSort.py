def BubbleSort(lista):
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if lista[j]>lista[j+1]:
                temp=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=temp
    return lista

list1=[1,3,0,2,5,-3]
a = [1, [2, 5, 6, 10, 12], 3, 4, 5]
list2 = BubbleSort(list1)
print(list2)