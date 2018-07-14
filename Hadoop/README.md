# Cloud-Computing
AWS, Python, Automation

Word Count Implementation
Hadoop

1) Using HPC (High Performnce Computing)

HDFS
HDFS or Hadoop FileSystem is the filesystem where Hadoop expects the input files to be. When a job completes, HDFS is also where the final result will be placed by Hadoop.


2) Using AWS Elastic Mapredcer (AWS EMR)
i) Head over to the EMR console and click on Create Cluster.
ii) The next step is to add a MR step. Click on Add Step and fill in the details as shown below. Be sure to change these paths for your S3 bucket.
iii) When done, the status of the cluster will change from Waiting to Running. After a few minutes, your job should be complete. This is indicated by the status of the cluster again going back to Waiting. You can now head over to the S3 bucket and see the output being generated.
