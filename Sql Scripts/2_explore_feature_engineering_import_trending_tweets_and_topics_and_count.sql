drop table bma.dzw_twitter_classification_trending_tweets_and_topics_raw;
create table bma.dzw_twitter_classification_trending_tweets_and_topics_raw
( id varchar(1000),
text varchar(10000),
event_dt varchar(1000),
country_code varchar(1000),
city_state varchar(1000),
lat varchar(1000),
lng varchar(1000),
--state varchar(1000),
retweet_Count varchar(1000),
trend_topic varchar(1000)
);
commit;

--drop table bma.dzw_twitter_classification_trending_topics_summarized;
create table bma.dzw_twitter_classification_trending_topics_tweet_rates_summarized_by_hour
( topic varchar(1000),
event_Dt datetime,
hourofday integer,
tweet_count integer
);
commit;

truncate table bma.dzw_twitter_classification_trending_tweets_and_topics_raw;
--copy bma.dzw_twitter_classification_trending_tweets_and_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Analysis\01052015\trending_tweets_20150106_cleaned_step3_reformat_datetime.csv' delimiter ',' enclosed by '"' ;
copy bma.dzw_twitter_classification_trending_tweets_and_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Analysis\01102015\sample_trending_tweets_20150110_cleaned_step3_reformat_datetime.csv' delimiter ',' enclosed by '"' ;

--copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20141222.csv' delimiter ',';
--copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20141223.csv' delimiter ',';
--copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20141224.csv' delimiter ',';
--copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20141225.csv' delimiter ',';
--copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20141226.csv' delimiter ',';
--copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20141227.csv' delimiter ',';
--copy bma.dzw_twitter_classification_trending_topics_raw from local 'C:\Users\dwoo57\Google Drive\Career\Projects\Trending Topics\Scipts\Data\Topics\usa_trending_topics20141228.csv' delimiter ',';

select count(*) from bma.dzw_twitter_classification_trending_tweets_and_topics_raw

select trend_topic,cast (event_Dt as date) as event_Dt,hour(cast (event_dt as datetime)),count(trend_topic) as tweets_rate_hr from bma.dzw_twitter_classification_trending_tweets_and_topics_raw
group by trend_topic, cast (event_Dt as date),hour(cast (event_dt as datetime))
--limit 1000
order by cast (event_Dt as date)
