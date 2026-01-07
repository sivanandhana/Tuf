class BinarySearch:

    def solution(self,arr,element):

        arr.sort()

        low = 0

        upp = len(arr)-1

        is_present = False

        while(low<=upp):

            mid = (low+upp)//2

            if element == arr[mid]:

                is_present = True

                break

            elif element < arr[mid]:

                upp = mid-1

            elif element > arr[mid]:

                low = mid+1

        print(is_present)

b_search = BinarySearch()

arr = [10,12,14,15,17,21]

element=14

b_search.solution(arr,element)