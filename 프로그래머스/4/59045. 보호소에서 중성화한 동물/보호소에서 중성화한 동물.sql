-- 코드를 입력하세요
SELECT O.ANIMAL_ID, O.ANIMAL_TYPE, O.NAME
FROM ANIMAL_OUTS O
JOIN ANIMAL_INS I ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE SEX_UPON_INTAKE LIKE "%Intact%" AND (O.SEX_UPON_OUTCOME LIKE "%Spayed%" OR O.SEX_UPON_OUTCOME LIKE "%Neutered%")
ORDER BY ANIMAL_ID ASC;

-- 보호소에서 중성화 수술을 거친 동물 정보
-- 보호소 들어오기 이전에 중성화 동물은 제외
-- 보호소 나갈 당시 중성화된 동물 아이디, 종, 이름
-- ID 순
-- 중성화 거친 동물은 Spayed OR Neutered