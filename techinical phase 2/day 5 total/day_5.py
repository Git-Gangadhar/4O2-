##merge sort
#splitting into two parts and further repeating the same process  and then compare

def merge_sort(arr,left,right,middle):
    left_arr=arr[left:middle+1]
    right_arr=arr[middle+1,right]

    left_index=0
    right_index=0
    index=left
    while left_index<len(left_arr>) and right_index<len(right_arr):





    while left_index<len(left_arr):
        arr[index]=left_arr[left_index]
        left_index+=1
        index+=1
    while right_index<len(right_arr):
        arr[index]=right_arr[right_index]
        right_index+=1
        index+=1

def merge_sort(arr,left,right):

#quick sort


'''space complexity O(n)
step! : pivot element is a random element
step2: sort less then pivot and greater than pivot
using i and j compare greater than and less than pivot respectively
compare both

'''
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left_arr=[i for i in arr[1:] if i<=pivot]
    right_arr = [i for i in arr[1:] if i >pivot]
    return quick_sort(left_arr)+[pivot]+quick_sort(right_arr)


arr=[30,20,50,40,10,80]
print(arr)
arr1=quick_sort(arr)
print(arr1)

"""GRAPHS
        In Real life graphs are used at app recommendations ,gps maps,'''''''''''''

     """
def bfs(graph,start):
    visited=[]
    q=[]
    while len(q)!=0:
        ele=q.pop(0)
        print(ele)
        for i in graph[ele]:
            if i not in visited:
                q.append(i)
                visited.append(i)



raph_elements={}
