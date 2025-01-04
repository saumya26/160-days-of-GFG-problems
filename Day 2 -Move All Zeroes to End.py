class Solution:
    def pushZerosToEnd(self, arr):
        # code here
        j = -1
        # find first zero
        for i in range(0, len(arr)):
            if arr[i] == 0:
                j = i
                break
        
        # 2 ptr approach
        if j != -1:
            for i in range(j + 1, len(arr)):
                # print(arr[i])
                if arr[i] != 0:
                    # swap
                    arr[j], arr[i] = arr[i], arr[j]
                    j += 1
        return arr

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1    