-- 不是前1, 需要distinct
# Write your MySQL query statement below
select 
    D.name as Department, 
    E.name as Employee, 
    E.salary as Salary
from 
    Employee E
join 
    Department D on D.id = E.departmentId
where (
    select count(distinct E2.Salary)
    from Employee E2
    where E2.departmentId = E.departmentId and E2.salary > E.salary 
) < 3