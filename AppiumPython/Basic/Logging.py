"""
Logging means tracking the events or steps during the execution of programme or software.

Log Levels
==========
Critical
Error
Warning
Info
Debug


29/03/2020 03:48:17 PM Sunday: INFO: Text Entered in edit box
29/03/2020 03:48:17 PM Sunday: ERROR: Unable to click on search button

"""

"""
Install pytest using pip (pip3 install pytest)

##### Naming Conventions of PyTest ###########
1) File name should start with "test_PytestExample1.py"
2) Method name should start with "test_methodA"

######## 3 Ways of executing the code in pytest #############

py.test -v -s files_path    # run all tests in specific files_path
py.test -v -s test_mod.py py.  # run tests in module or in test file
py.test -v -s test_module.py::test_method  # only run test_method in test_module.py

-v : verbose (verbose is an argument which is used to report more information about an operation in your program )
-s : to print statements
"""
import logging
import PythonLogging.CustomLogger as cl

# logging.basicConfig(filename="test.log",level=logging.DEBUG), datefmt = %I means 12 hours format, %H means 24 hours
# format, filemode = a means append new logs in same file, filemode = w means overridden the same file
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%m/%y %I:%M:%S %p %A' , level=logging.DEBUG ,filename="test2.log",filemode="a")
logging.critical("This is critical msg")
logging.error("This is a error msg")
logging.warning("this is warning msg")
logging.info("This is a Info msg")
logging.debug("This is a Debug msg")

logger.setLevel(logging.DEBUG)



class CustomLoggerDemo():
    log = cl.customLogger()

    def methodOne(self):
        self.log.critical("This is a critical")
        self.log.error("This is a error msg")
        self.log.warning("Warn msg")
        self.log.info("Info msg")
        self.log.debug("Debug msg")

    def methodTwo(self):
        m2 = cl.customLogger()
        m2.critical("Critical Msg")
        m2.error("Error msg")
        m2.warning("Warn msg")
        m2.info("Info msg")
        m2.debug("Debug msg")

cld =CustomLoggerDemo()
cld.methodOne()
cld.methodTwo()
