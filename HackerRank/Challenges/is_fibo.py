import math
def is_fabo(n):
    n_square = n*n
    if math.sqrt(5*n_square +4) % 1 == 0 or math.sqrt(5*n_square - 4) % 1 == 0:
        print "IsFibo"
    else:
        print "IsNotFibo"
    
if __name__ == "__main__":
    t = int(raw_input())
    for x in range(t):
        is_fabo(int(raw_input()))
