if hdfs dfs -test -f /tmp/kmeans_data.txt ; then
                                echo "File  exists"
else
                                echo “File does not exists ”
				hdfs dfs -put data/kmeans_data.txt /tmp/
fi


