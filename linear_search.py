class LinearSearch:
    def solution( self,arr,element):
        i=0
        is_present=False
        while i<len(arr):
            if arr[i]==element:
                is_present=True
                break
            i+=1
        print(is_present)

instance=LinearSearch()

instance.solution([10,2,3,5,6,7,12],12)
instance.solution([10,2,3,5,6,7,12],8)