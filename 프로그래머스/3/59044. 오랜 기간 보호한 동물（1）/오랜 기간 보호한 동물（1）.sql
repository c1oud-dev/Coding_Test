-- 코드를 입력하세요
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I
LEFT JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL  -- 입양 기록이 없는 동물만 선택
ORDER BY I.DATETIME ASC    -- 가장 예전 날짜부터(오래된 순)
LIMIT 3;                   -- 상위 3마리