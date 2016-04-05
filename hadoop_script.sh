python python_process.py

#hadoop fs -rm -r /home/training/Desktop/loganalysis/hdfsdata
#hadoop fs -rm -r /home/training/Desktop/loganalysis/queryoutput1
#hadoop fs -rm -r /home/training/Desktop/loganalysis/queryoutput2

hive -e 'create schema nasa'

hive -e 'create table nasa (src string,
							valid string,
							uid	string,
							ts string,
							url string,
							statcode int,
							bytes int)
			row format delimited fields 
			terminated by "|" 
				stored as textfile;'

hive -e 'load data local inpath "/home/training/Desktop/loganalysis/server-logs-mod.txt" into table nasa'

hive -e "SELECT COUNT(*) AS NROWS FROM (SELECT SPLIT(ts, '/')[1] as month from nasa where statcode==200 ) df where month ='Aug';"

hive -e "SELECT COUNT(distinct src) AS NROWS FROM (SELECT src, SPLIT(ts, '/')[1] as month from nasa) df where month ='Sept';"

hive -e "SELECT url, count(*) s nrows FROM  nasa where split(ts,'/')[2]='1995' group by url order by nrows desc limit 1 "

hive -e "select day, count(*) as nrows from (SELECT split(ts, '/')[0] as day, split(ts,'/')[1] as month, split(ts,'/')[2] as year from nasa) df where month='Oct' and year='1995' group by day, month, year;" >> plotdata.txt

python plot_hist.py

hadoop fs -put /home/training/Desktop/loganalysis/server-logs-mod.txt /home/training/Desktop/loganalysis/hdfsdata

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper /home/training/Desktop/loganalysis/mapper1.py -reducer /home/training/Desktop/loganalysis/reducer1.py -input /home/training/Desktop/loganalysis/hdfsdata -output /home/training/Desktop/loganalysis/queryoutput1 -file /home/training/Desktop/loganalysis/mapper1.py -file /home/training/Desktop/loganalysis/reducer1.py

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper /home/training/Desktop/loganalysis/mapper2.py -reducer /home/training/Desktop/loganalysis/reducer2.py -input /home/training/Desktop/loganalysis/hdfsdata -output /home/training/Desktop/loganalysis/queryoutput2 -file /home/training/Desktop/loganalysis/mapper2.py -file /home/training/Desktop/loganalysis/reducer2.py

hadoop fs -text /home/training/Desktop/loganalysis/queryoutput1/part* | sort >> query1hadoop.txt

hadoop fs -text /home/training/Desktop/loganalysis/queryoutput2/part*>> query2hadoop.txt

