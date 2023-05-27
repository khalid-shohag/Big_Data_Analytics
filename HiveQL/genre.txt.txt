-- Hive query run to determine average ratings of each music genre. Data collected from yahoo.

-- starting Hadoop
start-all.sh

-- start hive metastore
hive --service metastore;

-- open hive cli
hive

-- creating song_ratings tables from test data.
CREATE TABLE song_ratings( user_id STRING, song_id STRING, rating INT) ROW FORMAT delimited FIELDS terminited BY '\t';

CREATE TABLE song_ratings_two( user_id STRING, song_id STRING, rating INT) ROW FORMAT delimited FIELDS terminited BY '\t';

CREATE TABLE song_ratings_three( user_id STRING, song_id STRING, rating INT) ROW FORMAT delimited FIELDS terminited BY '\t';

CREATE TABLE song_ratings_four( user_id STRING, song_id STRING, rating INT) ROW FORMAT delimited FIELDS terminited BY '\t';

CREATE TABLE song_ratings_five( user_id STRING, song_id STRING, rating INT) ROW FORMAT delimited FIELDS terminited BY '\t';

CREATE TABLE song_ratings_six( user_id STRING, song_id STRING, rating INT) ROW FORMAT delimited FIELDS terminited BY '\t';

CREATE TABLE song_ratings_seven( user_id STRING, song_id STRING, rating INT) ROW FORMAT delimited FIELDS terminited BY '\t';

CREATE TABLE song_ratings_eight( user_id STRING, song_id STRING, rating INT) ROW FORMAT delimited FIELDS terminited BY '\t';

CREATE TABLE song_ratings_nine( user_id STRING, song_id STRING, rating INT) ROW FORMAT delimited FIELDS terminited BY '\t';

CREATE TABLE song_ratings_ten( user_id STRING, song_id STRING, rating INT) ROW FORMAT delimited FIELDS terminited BY '\t';

-- Load data from local path
LOAD DATA LOCAL inpath 'file path/test_0.txt' overwrite INTO TABLE song_ratings;

LOAD DATA LOCAL inpath 'file path/test_2.txt' overwrite INTO TABLE song_ratings_two;

LOAD DATA LOCAL inpath 'file path/test_3.txt' overwrite INTO TABLE song_ratings_three;

LOAD DATA LOCAL inpath 'file path/test_4.txt' overwrite INTO TABLE song_ratings_four;

LOAD DATA LOCAL inpath 'file path/test_5.txt' overwrite INTO TABLE song_ratings_five;

LOAD DATA LOCAL inpath 'file path/test_6.txt' overwrite INTO TABLE song_ratings_six;

LOAD DATA LOCAL inpath 'file path/test_7.txt' overwrite INTO TABLE song_ratings_seven;

LOAD DATA LOCAL inpath 'file path/test_8.txt' overwrite INTO TABLE song_ratings_eight;

LOAD DATA LOCAL inpath 'file path/test_9.txt' overwrite INTO TABLE song_ratings_nine;

LOAD DATA LOCAL inpath 'file path/test_1.txt' overwrite INTO TABLE song_ratings_ten;

-- create table song_ratings_final to combine 10 song_ratings into one
CREATE TABLE song_ratings_final( user_id STRING, song_id STRING, rating INT) ROW FORMAT delimited FIELDS terminited BY '\t';

-- insert value into the table
INSERT overwrite TABLE song_ratings_final ( 
	SELECT * FROM song_ratings UNION ALL 
	SELECT * FROM song_ratings_two UNION ALL
	SELECT * FROM song_ratings_three UNION ALL
	SELECT * FROM song_ratings_four UNION ALL
	SELECT * FROM song_ratings_five UNION ALL
	SELECT * FROM song_ratings_six UNION ALL
	SELECT * FROM song_ratings_seven UNION ALL
	SELECT * FROM song_ratings_eight UNION ALL
	SELECT * FROM song_ratings_nine UNION ALL
	SELECT * FROM song_ratings_ten);
	
-- create table for song attributes
CREATE TABLE song_attributes (
		song_id STRING,
		album_id STRING,
		artist_id STRING,
		genre_id STRING);

-- load data from local path for the table
LOAD DATA LOCAL inpath 'file path/song_attributes.txt' overwrite INTO TABLE song_attributes;

-- create table for genre attributes
CREATE TABLE genre_attributes (
		genre_id STRING,
		parent_genre_id STRING,
		song_level STRING,
		genre_name STRING);
-- load data from local path for the table
LOAD DATA LOCAL inpath 'file path/genre_attributes.txt' overwrite INTO TABLE genre_attributes;

-- Query to determinme average ratings of each genre

1. SET hive.auto.convert.join = FALSE;

2. SELECT genre_attributes.genre_name, AVG(song_ratings.final)
			 FROM song_ratings_final 
			 JOIN song_attributes 
			 JOIN genre_attributes
			 ON (song_ratings_final.song_id = song_attributes.song_id 
			 AND song_attributes.genre_id = genre_atributes.genre_id)
	GROUP BY genre_attributes.genre_name;

