--select count(*) from frequency where docid="10398_txt_earn";

--select count(term) from frequency where docid="10398_txt_earn" and count=1;

--select count(*) from ( select term from frequency where docid="10398_txt_earn" and count=1 UNION select term from frequency where docid="925_txt_trade" and count=1 );

--select count(distinct(docid)) from frequency where term = 'parliament';

--select count(*) from (select docid from frequency group by docid having sum(count) > 300);

--select count(*) from (select * from frequency f1 where f1.term = 'transactions') f1 JOIN (select * from frequency where term = 'world') f2 ON f1.docid=f2.docid;

--select value from (select A.row_num as row_num, B.col_num as col_num, sum(A.value * B.value) as value from A,B where A.col_num=B.row_num group by A.row_num, B.col_num) t where t.row_num=2 and t.col_num=3;

--select sum(a.count*b.count) from (select * from frequency where docid = "10080_txt_crude") a join (select * from frequency where docid = "17035_txt_earn" ) b on a.term=b.term  where a.docid <b.docid group by a.docid, b.docid;

select similarity from (
select a.docid, sum(a.count*b.count) similarity from
(select * from frequency) a
join 
(
select * from frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count) b 
on a.term=b.term   
where b.docid = 'q'
group by a.docid, b.docid)
order by similarity DESC limit 1
;








