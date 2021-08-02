# JProfiler

## Remotely Profiling Tomcat 8

1. Upload the [JProfiler 8.1 tar.gz archive](https://download-gcdn.ej-technologies.com/jprofiler/jprofiler_linux_8_1_4.tar.gz) to the target machine
1. `ssh` to the target machine
1. Unpack the archive and cd into it
1. Run the `jpenable` tool as the tomcat user to start the profiling listener:

        sudo -u tomcat8 bin/jpenable

1. Take note of the port number it gives you (31757 by default)
1. Create a new JProfiler session on your local machine with the following settings:
    1. Attach to an already running JVM
    1. Attach to a profiled JVM (local or remote)
    1. Enter host of the machine and the profiling port given in the command output above
1. Click OK
1. Choose session settings based on your need: for CPU, sampling is lower-overhead, but instrumentation is more accurate

References:

* [https://stackoverflow.com/a/12949796/2833126](https://stackoverflow.com/a/12949796/2833126)

## Without JPEnable

1. Add the following to JAVA_OPTS in /etc/default/tomcat8:

        -agentpath:/home/nmx/jprofiler/jprofiler8/bin/linux-x64/libjprofilerti.so=port=31758,nowait

# JStack to Get a Stack Dump from a Runing Java Program

* `jps` lists running Java processes
* `jstack -l <pid-from-jps-ouput>` dumps the stack

# Debugging
* [IBM thread analyzer](https://publib.boulder.ibm.com/httpserv/cookbook/Major_Tools-IBM_Thread_and_Monitor_Dump_Analyzer_TMDA.html)
* [IBM Garbage Collection and Memory Visualizer](https://publib.boulder.ibm.com/httpserv/cookbook/Major_Tools-Garbage_Collection_and_Memory_Visualizer_GCMV.html)
* [Memory leak patterns](https://dzone.com/articles/memory-leaks-fallacies-and-misconceptions)

# Other

* [JavaPoet source code generation API](https://github.com/square/javapoet)
