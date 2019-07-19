arr2 = [2,1,4,3,9,6]
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
#arr2 = [943,790,427,722,860,550,225,846,715,320]
#arr1 = [943,715,427,790,860,722,225,320,846,550]
#arr1 = [26,21,11,20,50,34,1,18]
#arr2 = [21,11,26,20]
#arr1=[28,6,22,8,44,17]
#arr2=[22,28,8,6]

arr_spare = []
last_seen = 0 
idx = last_seen
idx_main = 0
sub = arr1[last_seen]

while idx_main < len(arr2) :
    idx = last_seen
    while idx < len(arr1) :
        if arr2[idx_main] == arr1[idx] :
            sub = arr1[last_seen]
            arr1[last_seen] = arr1[idx]
            arr1[idx] = sub
            last_seen +=1
        idx +=1    
    idx_main +=1

'''
 sorter
'''
try :
    if len(arr2) != len(arr1):
        for i in range(last_seen,len(arr1)) :
            arr_spare.append(arr1.pop(last_seen))
        arr_spare = sorted(arr_spare)
        arr1.extend(arr_spare)
except:
    pass

print(arr1)
