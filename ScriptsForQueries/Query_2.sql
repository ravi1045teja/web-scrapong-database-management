#GET THE DEPARTMENT WHICH HAS MORE UNDERGRADUATE PROGRAMS
SELECT DEPARTMENTID,DEPARTMENTNAME FROM DEPARTMENT WHERE DEPARTMENTID=
(SELECT DEPARTMENTID  FROM UNDERGRADUATEPROGRAMS GROUP BY DEPARTMENTID HAVING COUNT(DEPARTMENTID)=(SELECT MAX(MAX_D) FROM
(SELECT DEPARTMENTID,COUNT(DEPARTMENTID)AS MAX_D FROM UNDERGRADUATEPROGRAMS GROUP BY DEPARTMENTID)A));