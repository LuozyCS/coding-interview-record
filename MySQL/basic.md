### 关键字
select distinct university as xx from table limit 0,2
order by desc/asc


select device_id, university from user_profile
where university = "北京大学" (单引号也可以) AND age = xx

select device_id,university from user_profile where university like '%北京%'

JOIN result ON student.sid = result.sid
根据sid将学生表和成绩表连接在一起
select的时候可以选择 student.sid result.cname这样


打印成绩前2
order by result.score desc limit 2


别名
SELECT r.cname
FROM result r

子查询
看小林SQL面试题, 求各个科目前3名的学生(腾讯)
很巧妙

分组
每个班级总分
SELECT s. classid, SUM(r. score) as total_score
FROM student s
JOIN result r ON s.sid = r. sid
GROUP BY s. classid;


select 