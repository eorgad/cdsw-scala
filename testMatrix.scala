import scala.collection.mutable

import org.apache.log4j.{Level, Logger}
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.mllib.recommendation.{ALS, MatrixFactorizationModel, Rating}
import org.apache.spark.rdd.RDD
import sys.process._

//load local data to hdfs
"ls -lrth" !


"java -jar rddExample1.jar rddExample1.class" !
