__author__ = 'HaoBin'


def mprint(board):
    for i in board:
        print(i)
    print()

def sud(board, ncount,nx,ny):
    if ncount == 0:
        mprint(board)
    else:
        pos,nnx,nny = nextpos(board,nx,ny)
        for p in pos:
            board[nnx][nny] = p
            sud(board,ncount-1,nnx,nny)
            board[nnx][nny] = None

def nextpos(board,nx,ny):
    nny = ny + 1
    nnx = nx
    if nnx == nny:
        nny += 1


    if nny >= 4:
        nnx = nx + 1
        nny = 0

    pos = []
    for x in range(1,4+1):
        if check(board,x,nnx,nny):
            pos.append(x)


    if board[nnx][nny] is None:
        return pos, nnx, nny


def check(board,x,nnx,nny):
    for a in range(4):
        if board[nnx][a] == x:
            return False
        if board[a+1][nny] == x:
            return False
    return True


board2 = [[1,None,None,None],
         [None,2,None,None],
         [None,None,3,None],
         [None,None,None,4],
         [1,2,3,4]]

board = [[1,None,None,None],
         [None,2,None,None],
         [None,None,3,None],
         [None,None,None,4],
         [1,2,3,4]]

#print(nextpos(board,0,0))


sud(board,12,0,0)

# 0,1
# 0,2
# 0,3
# 1,0
# 1,2
# 1,3
# 2,0
# 2,1
# 2,3
# 3,0
# 3,1
# 3,2