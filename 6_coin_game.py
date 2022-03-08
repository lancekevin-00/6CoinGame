from anytree import Node, RenderTree

class board():
    def __init__(self):
        self.movesInGame = 0
        self.pathOfPlay = []
        self.allPathsOfPlay =[]
        self.rootNode = Node("0")

        self.row1 = [True]
        self.row2 = [True, True]
        self.row3 = [True, True, True]
    
    def solve(self, parentNode):
        moves = self.possibleMoves()

        if(len(moves) == 0):
            self.allPathsOfPlay.append(self.formatGamePath(self.pathOfPlay))

            if(parentNode.p1_move):
                parentNode.p1_wins = True
            else:
                parentNode.p1_wins = False

        else:
            i = 0
            while (i < len(moves)):

                #remove pieces
                self.toggleMove(moves[i], False)

                if(self.movesInGame % 2 == 0):
                    p1 = False
                else:
                    p1 = True

                #add move to game tree
                currMove = Node(str(moves[i]), parent = parentNode, p1_move=p1, p1_wins = None)

                #see next players moves
                self.solve(currMove)

                #detemine if curr path leads to P1 victory
                if (not currMove.is_leaf):
                    childIDX = 0
                    while(childIDX < len(currMove.children)):
                        if (not currMove.p1_move):
                            if (currMove.children[childIDX].p1_wins):
                                currMove.p1_wins = True
                                break
                            else:
                                currMove.p1_wins = False
                        else:
                            if (not currMove.children[childIDX].p1_wins):
                                currMove.p1_wins = False
                                break
                            else:
                                currMove.p1_wins = True
                        childIDX = childIDX + 1

                #undo move to restore board and view next move
                self.toggleMove(moves[i], True)

                i = i+1

    def toggleMove(self, moveNum, replace_pieces):
        if (moveNum < 1 or moveNum > 9):
            return

        if (not replace_pieces):
            self.movesInGame = self.movesInGame + 1
            self.pathOfPlay.append(moveNum)
        else:
            self.movesInGame = self.movesInGame - 1
            self.pathOfPlay.pop(self.movesInGame)

        if(moveNum == 1):
            self.row1[0] = replace_pieces
        
        elif(moveNum == 2):
            self.row2[0] = replace_pieces

        elif(moveNum == 3):
            self.row2[0] = replace_pieces
            self.row2[1] = replace_pieces

        elif(moveNum == 4):
            self.row2[1] = replace_pieces

        elif(moveNum == 5):
            self.row3[0] = replace_pieces

        elif(moveNum == 6):
            self.row3[0] = replace_pieces
            self.row3[1] = replace_pieces

        elif(moveNum == 7):
            self.row3[1] = replace_pieces

        elif(moveNum == 8):
            self.row3[1] = replace_pieces
            self.row3[2] = replace_pieces

        elif(moveNum == 9):
            self.row3[2] = replace_pieces

    def possibleMoves(self):
        possMoves = []

        #moves in row 1
        if(self.row1[0]):
            possMoves.append(1)

        #moves in row 2
        if(self.row2[0]):
            possMoves.append(2)
            
            if(self.row2[1]):
                possMoves.append(3)
        
        elif(self.row2[1]):
            possMoves.append(4)
        
        if(self.row3[0]):
            possMoves.append(5)

            if(self.row3[1]):
                possMoves.append(6)
        
        elif(self.row3[1]):
            possMoves.append(7)

            if(self.row3[2]):
                possMoves.append(8)
        elif(self.row3[2]):
            possMoves.append(9)

        return possMoves

    def formatGamePath(self, path):
        gameStr = ""
        i = 0
        while (i < len(path)):
            gameStr = gameStr + str(path[i])
            i = i + 1

        if(len(path) % 2 == 0):
            gameStr = gameStr + ",P2_wins"
        else:
            gameStr = gameStr + ",P1_wins"
        return gameStr


game = board()
game.solve(game.rootNode)

#print(RenderTree(game.rootNode))

#determine the winning strategy
openingIDX = 0
p1_can_win = False
while (openingIDX < len(game.rootNode.children)):
    if (game.rootNode.children[openingIDX].p1_wins):
        print ("move " + str(openingIDX + 1) + " is a winning strategy for player 1")
        p1_can_win = True
    openingIDX = openingIDX + 1

if (not p1_can_win):
    print ("p2 can win off any opening from p1")