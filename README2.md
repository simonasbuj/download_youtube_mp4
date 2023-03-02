# Steps to run on new environment

1)  
  Download and install java: https://www.oracle.com/java/technologies/downloads/  
  Create Enviromental variable: JAVA_HOME = java_installation/jdk.  

2)  
  Download spark: https://spark.apache.org/downloads.html  
  Create Enviromental variabls:  
    HADOOP_HOME = spark_installation/spark-3.3.2-bin-hadoop3  
    SPARK_HOME = spark_installation/spark-3.3.2-bin-hadoop3  
    PYSPARK_DRIVER_PYTHON = python  
    
3)  
  Install python: https://www.python.org/downloads/  
  Install pyspark library in python enviroment you're going to use: pip install pyspark  
  
4)  
  You can run pyspark programs in terminal with: spark-submit python_program.py  
