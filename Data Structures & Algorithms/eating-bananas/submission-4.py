class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # choose initial k value
        # process time for that k
        # return if it is under h
        # update min
        # continue increasing k until it exceeds


        #k = 1
        res = max(piles)

        def processK(k: int) -> bool:
            needH = 0
            
            for p in piles:
                #curr = p
                if p % k == 0:
                    needH += (p // k)
                elif p < k:
                    needH += 1
                else:
                    needH += 1 + (p // k)
            
            return needH <= h
        
        lK, rK = 1, max(piles)
        while lK < rK:
            mK = (lK + rK) // 2

            if processK(mK):
                res = min(mK, res)
                rK = mK
            else:
                lK = mK + 1

        return res
            



