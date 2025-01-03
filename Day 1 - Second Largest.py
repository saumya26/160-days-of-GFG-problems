class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        arr = list(set(arr))
        arr.sort(reverse=True)
        max_ele = arr[0]
        arr.remove(max_ele)
        if arr:
            return (arr[0])
        else:
            return -1

#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends