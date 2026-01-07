class LinearSearching:

    def solution(self,arr,element):

        i=0

        is_present = False

        while(1<len(arr)):

            if arr[i]==element:

                is_present=True

                break
            i+=1

        print(is_present)


lsearch_instance = LinearSearching()

lst=[10,12,13,15,16,17,21]

element =15

lsearch_instance.solution(lst,element)