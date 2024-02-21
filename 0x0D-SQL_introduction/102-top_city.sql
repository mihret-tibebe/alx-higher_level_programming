-- top city
SELECT city, AVG(value) AS avg_temp FROM (SELECT *  FROM temperatures WHERE
    month BETWEEN 7 AND 8) AS result GROUP BY result.city ORDER BY avg_temp DESC
    LIMIT 3 ;
