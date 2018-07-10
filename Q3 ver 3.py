def bsearch(arr, start, end, num):
    while start <= end:
        mid = start + (end - start)//2;
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return -1

a = [0,1,2,3,4,5,6,7,8,9]

result = bsearch(a, 0, len(a)-1, 10)

class MyError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return(repr(self.value))
        if(Exception == -1):
            self.value = -1

try:
    ans = MyError(result)
    print(ans)

except MyError as error:
    print('Element not found ',error.value)
    
    
    
    