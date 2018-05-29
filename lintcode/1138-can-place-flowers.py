class Solution:
    """
    @param flowerbed: an array
    @param n: an Integer
    @return: if n new flowers can be planted in it without violating the no-adjacent-flowers rule
    """

    def canPlaceFlowers(self, flowerbed, n):
        # Write your code here
        cnt = 0
        for i in range(len(flowerbed)):
            if cnt >= n: break
            if flowerbed[i] == 0:
                nxt = 0 if i == len(flowerbed) - 1 else flowerbed[i + 1]
                pre = 0 if i == 0 else flowerbed[i - 1]
                if nxt == 0 and pre == 0:
                    flowerbed[i] = 1
                    cnt += 1
        return cnt == n
