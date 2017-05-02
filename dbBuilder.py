mysql.server start
mysql -u root -p --local-infile uDebt


CREATE TABLE debtDB (word VARCHAR(40) NOT NULL, date DATE NOT NULL, source VARCHAR(10) NOT NULL, instance int NOT NULL, title VARCHAR(200) NOT NULL, CONSTRAINT pKey PRIMARY KEY(word, date, instance));
CREATE TABLE titles (date DATE NOT NULL, title VARCHAR(400) NOT NULL, CONSTRAINT pKey PRIMARY KEY(title, date));
CREATE TABLE articleWordCount (word VARCHAR(20) NOT NULL, count int NOT NULL, CONSTRAINT pKey PRIMARY KEY(word, count));

LOAD DATA LOCAL INFILE 'dbInfo.txt' INTO TABLE debtDB;
LOAD DATA LOCAL INFILE 'titles.txt' INTO TABLE titlesDB;


SELECT date,title
FROM titlesDB
INTO OUTFILE 'titles.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';