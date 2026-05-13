my_list = [1, 4, 5, 6, 2, 3]

def merge_sort(array, left, right):
    array_p = left
    p1 = 0
    p2 = 0
    if left < right:
        mid = (left + right) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        
        length1 = mid - left + 1
        length2 = right - mid
        
        L = [0]*length1
        R = [0]*length2
        
        for i in range(length1):
            L[i] = array[left + i]
        for i in range(length2):
            R[i] = array[mid + 1 + i]
        
        while p1 < length1 and p2 < length2:
            if L[p1] < R[p2]:
                array[array_p] = L[p1]
                p1 += 1
            else:
                array[array_p] = R[p2]
                p2 += 1
            array_p += 1
            
        while p1 < length1:
            array[array_p] = L[p1]
            p1 += 1
            array_p += 1
        while p2 < length2:
            array[array_p] = R[p2]
            p2 += 1
            array_p += 1

merge_sort(my_list, 0, len(my_list) - 1)
print(my_list)
        
        
    
        
    
