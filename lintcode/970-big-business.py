class Solution:
    """
    @param a: The cost of the film
    @param b: The price of the selling of the film
    @param k: The principal
    @return: The answer
    """

    def bigBusiness(self, a, b, k):
        # Write your code here
        arr = list(zip(a, b))
        arr = sorted(arr)
        for i in range(len(a)):
            if arr[i][0] < arr[i][1] and arr[i][0] <= k:
                k = k - arr[i][0] + arr[i][1]
        return k
