-- 코드를 작성해주세요
SELECT E.ID, COUNT(E2.ID) AS CHILD_COUNT -- 자식 수를 출력
FROM ECOLI_DATA E
-- 자식이 없어도(NULL)이어도 출력되도록
LEFT JOIN ECOLI_DATA E2 ON E.ID = E2.PARENT_ID 
-- 같은 테이블 조인해서 있는 ID 번호를 E.2에 가져오기
GROUP BY E.ID -- GROUP BY가 꼭 있어야함?
ORDER BY E.ID ASC;    -- 개체 ID 에 대해 오름차순