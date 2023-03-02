# Steps to run on new environment

1)  
  &emsp;Download and install java: https://www.oracle.com/java/technologies/downloads/  
  &emsp;Create Enviromental variable: JAVA_HOME = java_installation/jdk.  

2)  
  &emsp;Download spark: https://spark.apache.org/downloads.html  
  &emsp;Create Enviromental variables:  
    &emsp;&emsp;HADOOP_HOME = spark_installation/spark-3.3.2-bin-hadoop3  
    &emsp;&emsp;SPARK_HOME = spark_installation/spark-3.3.2-bin-hadoop3  
    &emsp;&emsp;PYSPARK_DRIVER_PYTHON = python  
    
3)  
  &emsp;Install python: https://www.python.org/downloads/  
  &emsp;Install pyspark library in python enviroment you're going to use: pip install pyspark  
  
4)  
  &emsp;You can run pyspark programs in terminal with: 
  &emsp;&emsp;spark-submit spark_program.py  
  &emsp;&emsp;python spark_program.py
