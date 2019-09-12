``` Analysis on sales data for chain of stores using Cloud Era platform ```

For Detailed, Explanation, Refer my blog:
https://medium.com/@n.maajidkhan/get-your-hands-dirty-with-hadoop-map-reduce-job-using-cloud-era-platform-big-data-f929fe0f12b4?source=friends_link&sk=2db02eb7fb73bc3ebac71b9eb04254b6

-> To analyse and determine the revenue earned across different stores  in a country/region.
-> Use the core concepts, HDFS and MapReduce of Big Data Hadoop Platform to solve the problem.
-> Processing large volumes of data in parallel by dividing the work into a set of independent tasks.
-> Use MapReduce process file to break it into chunks and process it parallelly.

Objectives:
-> Analyse different use-cases where MapReduce is used.
-> Implement basic MapReduce Concepts.
-> Run a MapReduce program.
-> Understand Input Splits concept in MapReduce.
-> Understand Map Reduce Job Submission flow.
-> Implement Job Tracker and Job Tracer in MapReduce.

purchases.txt file can be downloaded from this link:
https://drive.google.com/file/d/1Ar12GZISlf-JMQSj1FQsy0_XhSqMH4F9/view?usp=sharing

How to Run:
I am assuming that you have already installed the virtual machine. Once you open the machine go to the directory where your project files are located. It will have an mapper and reducer program. It contains a file ``` purchases.txt ```that contains the sales data for a dummy store. First, we need to add this input into the Hadoop cluster. To run any command on the Hadoop cluster we need to append it with Hadoop fs.
1. Go to the folder where your project files are located in your machine.
2. Put the purchases.txt file in the hadoop cluster using hadoop fs -put purchases.txt
3. Check if the file is in the hadoop cluster using hadoop fs -ls
We are assuming that we are having only one reducer that will get the sorted input from the mappers. The reducer.py takes in the sorted input and keeps on checking whether the new key is equal to the previous key. When the change occurs, it prints the store name and the total sales for the store.

Once you have written the mappers and reducers you can start the map reduce job using the command:
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input myinput -output joboutput

After you run this, it takes some time to compute. You can watch how mappers and reducers are running in the output terminal. The terminal will shows variety of information like the percentage of the completion of job.

The output of our program gets saved in the file joboutput/part-00000
You can view the output in the same terminal by running the command hadoop fs -ls joboutput

Instead of viewing the whole output, you can view a smaller part of our output by using the command hadoop fs -cat joboutput/part-00000 | less
Once your task is done, now you can delete that joboutput file from out HDFS system. Reason being, we can’t have different output workloads being generated with the same output file name. This can be achieved by running the following command hadoop fs -rm -r -f joboutput
Meanwhile, you can export the data into a text file and save it in your directory if you want for future use.


