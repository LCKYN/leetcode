class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = dict()
        
        for i,n in enumerate(nums):
            if(n not in temp):
                temp[n] = [i]
            else:
                temp[n].append(i)
                
        for i in temp.keys():
            if(len(temp[i]) >= 2):
                for j in range(1,len(temp[i])):
                    if(temp[i][j] - temp[i][j-1] <= k):
                        return True
            
        return False
        