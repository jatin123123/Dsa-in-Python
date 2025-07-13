arr1 = [1,3,5,6,6,6,7,8,10,11,22,66,88,99]
arr2 = [1,2,3,4,5,6,9]


def merg_sorted(arr1,arr2):
     result = []
     i,j = 0,0
     
     while i < len(arr1) and j < len(arr2):
          if arr1[i] <= arr2[j]:
               if len(result)==0 or result[-1] != arr1[i]:
                    result.append(arr1[i])
               i += 1
          else:
               if len(result)==0 or result[-1] != arr2[j]:
                    result.append(arr2[j])
               j += 1
               
     
     
     
     while i < len(arr1):
          if len(result) == 0 or result[-1] != arr1[i]:
            result.append(arr1[i])
          i += 1
     while j < len(arr2):
          if len(result)==0 or result[-1] != arr2[j]:
                    result.append(arr2[j])
          j += 1
     
     return result
     
     
print(merg_sorted(arr1,arr2))