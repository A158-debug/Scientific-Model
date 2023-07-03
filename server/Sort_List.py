def bubble_sort(array,index):
    n = len(array)

    for i in range(n):

        already_sorted = True

        for j in range(n - i - 1):
            if array[j][index] > array[j + 1][index]:

                for k in range(len(arr[0])):
                    array[j][k], array[j + 1][k] = array[j + 1][k], array[j][k]

                already_sorted = False

        if already_sorted:
            break

    return array


arr = [[2,4,5],[1,6,7],[3,5,2]]
arr = bubble_sort(arr,1)
print(arr)
