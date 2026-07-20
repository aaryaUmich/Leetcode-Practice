class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r = 1,max(piles)
        k = 999999999

        while l<=r:
            mid = (l+r)//2

            total = 0


            for pile in piles:
                total+=(pile + mid - 1) // mid

            
            if total<=h:
                k=mid
                r = mid-1
            else:
                l = mid+1

        return k
        

            