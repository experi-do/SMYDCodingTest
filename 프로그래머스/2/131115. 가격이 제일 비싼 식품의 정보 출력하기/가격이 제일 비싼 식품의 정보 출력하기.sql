-- 코드를 입력하세요
-- FOOD_PRODUCT 테이블에서 가격이 제일 비싼 식품의 
-- 식품 ID, 식품 이름, 식품 코드, 식품분류, 식품 가격을 조회하는 SQL문을 작성해주세요.
SELECT *
FROM FOOD_PRODUCT F
WHERE F.PRICE = (
    SELECT MAX(F2.PRICE)
    FROM FOOD_PRODUCT F2
);