drop table bma.dzw_twitter_classification_trending_topics_raw;
create table bma.dzw_twitter_classification_trending_topics_raw
( 
rank varchar(1000),
topic varchar(1000),
event_dt datetime
);
commit;

drop table bma.dzw_twitter_classification_trending_topics_summarized;
create table bma.dzw_twitter_classification_trending_topics_summarized
( 
rank varchar(1000),
topic varchar(1000),
start_dt datetime,
end_dt datetime,
duration_minutes integer
);
commit;

--1. import new topics
truncate table bma.dzw_twitter_classification_trending_topics_raw;
--copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20141221.csv' delimiter ',';
--copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20141222.csv' delimiter ',';
--copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20141223.csv' delimiter ',';
--copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20141224.csv' delimiter ',';
--copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20141225.csv' delimiter ',';
--copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20141226.csv' delimiter ',';
--copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20141227.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150103_v2_wrank.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150104_v2_wrank.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150105_v2_wrank.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150106_v2_wrank.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150107_v2_wrank.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150108_v2_wrank.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150109_v2_wrank.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150110_v2_wrank.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150111_v2_wrank.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150112_v2_wrank.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150113_v2_wrank.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150114_v2_wrank.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150115_v2_wrank.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150116_v2_wrank.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150117_v2_wrank.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150118_v2_wrank.csv' delimiter ',';
copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20150119_v2_wrank.csv' delimiter ',';

--2. check for headers
select count(topic) from bma.dzw_twitter_classification_trending_topics_raw
where topic = 'name';


select count(topic) from bma.dzw_twitter_classification_trending_topics_raw;

select * from bma.dzw_twitter_classification_trending_topics_raw
limit 10

--3. now summarize topics
truncate table bma.dzw_twitter_classification_trending_topics_summarized;
insert into bma.dzw_twitter_classification_trending_topics_summarized
(topic,rank,start_dt,end_dt,duration_minutes)
select topic,min(rank) as rank,min(event_Dt),max(event_dt),datediff(mi,min(event_dt),max(event_dt))
from bma.dzw_twitter_classification_trending_topics_raw
group by topic
--limit 10

-- Check for max date in table
select max(start_dt) from bma.dzw_twitter_classification_trending_topics_summarized

---4. get topics between range
select * from bma.dzw_twitter_classification_trending_topics_summarized
where duration_minutes between 120 and 1440 -- last more than 2hours and less than 24 hours
and start_dt between '2015-01-11' and '2015-01-19'
and rank in ('1','2','3','4','5','6')
order by rank,duration_minutes desc



--- get topics not in range
select * from bma.dzw_twitter_classification_trending_topics_summarized
where duration_minutes < 120 or duration_minutes > 1440
--and  start_dt between '2014-12-24' and '2014-12-25'
order by duration_minutes desc