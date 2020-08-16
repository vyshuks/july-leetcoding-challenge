"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        if r==0:
            return False
        c = len(board[0])
        
        word_len = len(word)
        
        def dfs(i, j, pos):
            if pos >= word_len:
                return True
            if 0<=i<r and 0<=j<c and board[i][j] == word[pos]:
                temp = board[i][j]
                board[i][j] = None
                if dfs(i-1,j,pos+1) or dfs(i+1,j,pos+1) or dfs(i,j-1,pos+1) or dfs(i,j+1,pos+1):
                    return True
                board[i][j]=temp
            return False
            
        
        for i in range(r):
            for j in range(c):
                if dfs(i,j,0):
                    return True
        return False