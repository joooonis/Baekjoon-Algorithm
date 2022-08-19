n = int(input())
n_cards = list(map(int,input().split()))

m = int(input())
m_cards = list(map(int,input().split()))

n_cards.sort()

ans = ''

def binarySearch(n, arr):
    left,right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == n:
            return True
        elif n > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return False
        

for card in m_cards:
    if binarySearch(card, n_cards):
        ans += '1 '
    else:
        ans += '0 '

print(ans)
