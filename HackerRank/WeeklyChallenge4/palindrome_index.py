def palindrome_index(string):
    n = len(string)
    start = 0
    end = n-1
    while(start < n and (string[start] == string[end])):
        start += 1
        end -= 1
    #print start, end
    if start >= end:
        return -1
    elif string[start] == string[end - 1]:
        return end
    else:
        return start

if __name__ == '__main__':
    t = int(raw_input())
    for x in range(t):
        print palindrome_index(raw_input())
