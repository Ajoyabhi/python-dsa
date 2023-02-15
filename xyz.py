class Solution:
    def binarysearch(self, arr, n, k):
        low = 0
        high = n-1
        flag=0
        while(low<=high):
            mid = (low+high) // 2
            if(arr[mid]==k):
                return mid
            elif(k>arr[mid]):
                low = mid+1
            else:
                high = mid -1
        return 0






def main():
    search = Solution()
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    x = search.binarysearch(arr, n, k)
    if(x==0):
        print(-1)
    else:
        print(x)


if __name__=='__main__':
    main()