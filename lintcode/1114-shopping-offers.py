class Solution:
    """
    @param price: List[int]
    @param special: List[List[int]]
    @param needs: List[int]
    @return: return an integer
    """

    def shoppingOffers(self, price, special, needs):
        # write your code here
        def shopping(price, special, needs, mem):
            if tuple(needs) in mem: return mem[tuple(needs)]

            j, res = 0, get_cost(needs, price)
            for s in special:
                clone = [nn - ss for nn, ss in zip(needs, s) if nn - ss >= 0]
                if len(clone) != len(needs): continue
                res = min(res, s[len(needs)] + shopping(price, special, clone, mem))
            mem[tuple(needs)] = res
            return res

        def get_cost(needs, price):
            return sum(n * p for n, p in zip(needs, price))

        mem = {}
        return shopping(price, special, needs, mem)
