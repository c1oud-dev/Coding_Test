import java.util.Arrays;

class Solution {
    public int solution(int[] mats, String[][] park) {
        // 1. 돗자리 크기를 오름차순으로 정렬
        Arrays.sort(mats);
        
        int rows = park.length;
        int cols = park[0].length;
        
        // 2. 가장 큰 돗자리부터 역순으로 깔 수 있는지 확인
        for (int i = mats.length - 1; i >= 0; i--) {
            int size = mats[i];
            
            // 공원 배열을 돌며 (r, c)를 돗자리의 왼쪽 위 꼭짓점으로 잡을 수 있는지 확인
            for (int r = 0; r <= rows - size; r++) {
                for (int c = 0; c <= cols - size; c++) {
                    
                    // 해당 위치에 size x size 크기만큼 돗자리를 깔 수 있는지 체크
                    if (canPlace(park, r, c, size)) {
                        return size; // 가장 큰 것부터 확인했으므로 바로 정답 반환
                    }
                }
            }
        }
        
        // 깔 수 있는 돗자리가 아무것도 없다면 -1 반환
        return -1;
    }
    
    // (startR, startC)부터 size 크기의 정사각형 영역이 모두 "-1"인지 확인하는 메서드
    private boolean canPlace(String[][] park, int startR, int startC, int size) {
        for (int r = startR; r < startR + size; r++) {
            for (int c = startC; c < startC + size; c++) {
                // 한 칸이라도 사람이 있으면("-1"이 아니면) 깔 수 없음
                if (!park[r][c].equals("-1")) {
                    return false;
                }
            }
        }
        return true;
    }
}