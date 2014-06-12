def get_cost(arr, n):
    cost = 0
    arr_1 = [0] * n
    arr_2 = [0] * n
    arr_1[0] = 0
    arr_2[0] = 0

    i = 1
    while(i<n):
        arr_1[i] = max(arr_1[i-1], arr_2[i-1] + abs(arr[i-1] - 1))
        arr_2[i] = max(arr_1[i-1]+ abs(arr[i]-1), arr_2[i-1] + abs(arr[i-1] - arr[i]))
        i+=1

    return max(arr_1[n-1], arr_2[n-1])

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        n = int(raw_input())
        arr = map(int, raw_input().strip().split(' '))
        print get_cost(arr, n)
