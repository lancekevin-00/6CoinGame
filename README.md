# 6CoinGame
A quick python project to model the 6 coin game from my game theory class.

## Rules:
The setup for the game is 6 coins laid out in 3 rows:  
0  
0, 0  
0, 0, 0  

For their turn a player can take 1 or 2 coins from a row.
The player who takes the last coin wins the game.

## possible moves:
There are 9 possible moves in this game; in order to construct the game tree I indexed all the moves.
### key
0 - coin may be taken or avaliable, unaffected by the move  
X - coin being taken by this move  
I - a coin that must have already been taken to make this move  

1:  
X  
0, 0  
0, 0, 0  

2:  
0  
X, 0  
0, 0, 0  

3:  
0  
X, X  
0, 0, 0  

4:  
0  
I, X  
0, 0, 0  

5:  
0  
0, 0  
X, 0, 0  

6:  
0  
0, 0  
X, X, 0  

7:  
0  
0, 0  
I, X, 0  

8:  
0  
0, 0  
I, X, X  

9:  
0  
0, 0  
I, I, X  
