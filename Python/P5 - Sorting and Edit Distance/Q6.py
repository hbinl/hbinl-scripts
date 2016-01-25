__author__ = 'HaoBin'


def NeedlemanWunsch(s1,s2):
    d = DPEditDistance(s1,s2)
    #print(d)
    # print()
    a = ""
    b = ""
    i = len(s1)
    j = len(s2)
    while i > 0 or j > 0:
        #print(i,j)
        #print(d[i][j] == d[i-1][j-1][0])
        if (i > 0 and j > 0) and d[i][j][1] == 0:
            a = s1[i-1] + a
            b = s2[j-1] + b
            i -= 1
            j -= 1
        elif i > 0 and d[i][j][1] == 1:
            a = s1[i-1] + a
            b = "-" + b
            i -= 1
        elif j > 0 and d[i][j][1] == 2:
            a = "-" + a
            b = s2[j-1] + b
            j -= 1

    # print("Optimal alignment:")
    # print(a)
    # print(b)

    return a,b




def DPEditDistance(s1,s2):
    n_s1 = len(s1)
    n_s2 = len(s2)

    d = [[None for i in range(n_s2+1)] for j in range(n_s1+1)]
    d[0][0] = [0,-1]

    for i in range(1,n_s2+1):
        d[0][i] = [1 + d[0][i-1][0], 2]
    for j in range(1,n_s1+1):
        d[j][0] = [1 + d[j-1][0][0], 1]
    #print(d)
    for i in range(1,n_s1+1):
        for j in range(1,n_s2+1):
            #print(i,j)
            diagonal = d[i-1][j-1][0]
            if s1[i-1] != s2[j-1]:
                diagonal += 1
            d[i][j] =  minima(diagonal, d[i-1][j][0]+1, d[i][j-1][0]+1)
            #print(d)


    # for i in range(n_s1+1):
    #     print(d[i])

    return d

def minima(x0,x1,x2):
    # -1 means no link
    # 0 means diagonal
    # 1 means up
    # 2 means left
    x = min(x0,x1,x2)
    lst = [x0,x1,x2]
    idx = -1
    for i in range(3):
        if lst[i] == x:
            idx = i
            break
    return [x, idx]


def main():
    s1 = "DENTIST"
    s2 = "DENTEST"
    s1 = "ABCD"
    s2 = "CBDA"
    s1="INTENTION"
    s2="EXECUTION"
    s1 = "DIRTYROOM"
    s2 = "DORMITORY"
    s1 = "AGTA"
    s2 = "TATGC"
    #DPEditDistance(s1,s2)
    x,y = NeedlemanWunsch(s1,s2)

    print(x)
    print(y)
if __name__ == "__main__":
    main()