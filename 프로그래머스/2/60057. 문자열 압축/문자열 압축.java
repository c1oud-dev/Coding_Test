class Solution {
    public int solution(String s) {
        int answer = s.length(); // 문자열 길이
        
        // 최소 2번 반복 되려면 단위가 전체 길이의 절반 이하여야 한다.
        for (int k = 1; k <= s.length() / 2; k++) {
            answer = Math.min(answer, compress(s, k)); // 최소값으로 갱신
        }
        return answer;
    }
    
    private int compress(String s, int k) {
        StringBuilder result = new StringBuilder();
        String prev = s.substring(0, k); // 첫 번째 조각
        int count = 1;
        
        for (int i = k; i < s.length(); i += k) {
            String curr = s.substring(i, Math.min(i + k, s.length()));
            
            if (prev.equals(curr)) {
                count++; // 같으면 카운트 증가
            } else {
                // 다르면 이전 조각 결과에 추가
                if (count > 1) result.append(count);
                result.append(prev);
                prev = curr;
                count = 1;
            }
        }
        // 마지막 조각 처리
        if (count > 1) result.append(count);
        result.append(prev);
        
        return result.length();
    }
}