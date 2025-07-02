class Solution {
    public boolean exist(char[][] board, String word) {
        int row = board.length;
        int col = board[0].length;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (dfs(0, i, j, row, col, board, word)) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean dfs(int ind, int i, int j, int row, int col, char[][] board, String word) {
        if (ind == word.length()) return true;

        if (i < 0 || j < 0 || i == row || j == col || (board[i][j] != word.charAt(ind))) {
            return false;
        }

        char temp = board[i][j];
        board[i][j] = '*'; 

        int[] ro = {0, 1, 0, -1};
        int[] co = {1, 0, -1, 0};

        for (int d = 0; d < 4; d++) {
            if (dfs(ind + 1, i + ro[d], j + co[d], row, col, board, word)) {
                board[i][j] = temp; 
                return true;
            }
        }

        board[i][j] = temp;
        return false;
    }
}
