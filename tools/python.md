# Python

* [Interesting Python Libs Of 2020](https://tryolabs.com/blog/2020/12/21/top-10-python-libraries-of-2020/)
* [Python Testing](https://realpython.com/python-testing/). Extensive article. Covers testing, test runners, benchmarking to test for performance degredation, linting, security scanners, testing a flask app, integration tests, and more
* [Vulture Dead Code Finder](https://pypi.org/project/vulture/)


## Stack Dump from Running Interpreter

* Pyrasite
    * See the gist [here](https://gist.github.com/reywood/e221c4061bbf2eccea885c9b2e4ef496)
    * This did not work for me. It got OOM and the container got restarted
    * [Docs](https://readthedocs.org/projects/pyrasite/downloads/pdf/latest/)
    * Tried:
        ```
        apt-get update
        apt-get install python3 python3-pip
        pip3 install pyrasite
        pyrasite <pid> <payload>
        pyrasite 1 dump_stacks.py
        ```
* GDB Macros
    * See SO answer [here](https://stackoverflow.com/a/147114)
    * Steps:
        ```
        apt-get update
        apt-get install procps gdb python3-dbg vim
        vim ~/.gdbinit and paste the content of http://svn.python.org/projects/python/trunk/Misc/gdbinit
        gdb -p <sleeping pid>
        This failed because I did not have debugging symbols in deployed Python
        ```
* Run it with debugging python?
