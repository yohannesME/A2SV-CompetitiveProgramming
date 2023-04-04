class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        answer=0
        nums=[nums1[i]-nums2[i] for i in range(len(nums1))]

        def mergeSort(left,right):
            if left==right:
                return [nums[left]]
            mid=(left+right)//2
            left_arr=mergeSort(left,mid)
            right_arr=mergeSort(mid+1,right)

            return merge(left_arr,right_arr)
        
        def merge(left,right):
            nonlocal answer
            pt1=len(left)-1
            pt2=len(right)-1
            temp=0
            prev=0
            while pt1>=0 or pt2>=0:
                if pt1>=0 and pt2>=0:
                    if left[pt1]-diff<=right[pt2]:
                        prev+=1
                        pt2-=1
                    else:
                        temp+=prev
                        pt1-=1
                elif pt1>=0 :
                    temp+=prev
                    pt1-=1
                else:
                    break 
            answer+=temp          

            result=[]
            i=j=0
            while i<len(left) or j<len(right):
                if i<len(left) and j<len(right):
                    if left[i]<right[j]:
                        result.append(left[i])
                        i+=1
                    else:
                        result.append(right[j])
                        j+=1
                elif i<len(left):
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            return result

        mergeSort(0,len(nums)-1)

        return answer