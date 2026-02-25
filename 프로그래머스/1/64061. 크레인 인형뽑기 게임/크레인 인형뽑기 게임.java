import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        
        Stack<Integer> stack = new Stack<>();
        
        for (int move : moves) {
            int col = move - 1;     // 열
            
            for (int row = 0; row < board.length; row++) {  // board.length => 행의 개수 반환
                if (board[row][col] != 0) {
                    int doll = board[row][col];
                    board[row][col] = 0;    // 바구니에서 인형 꺼내기
                    
                    if (!stack.isEmpty() && stack.peek() == doll) {
                        answer += 2;
                        stack.pop();    // 같은 인형 있으면 터트리기
                    } else { 
                        stack.push(doll);
                    }
                    break;
                }
                
            }
        }
        
        return answer;
    }
}