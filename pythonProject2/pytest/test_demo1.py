# any pytest file should start from word test_ or end with _test, function should also with test
# every line of code should be written in function only in pytest
# from console directory name\ py.test : all files in the director, py.test -v -s : all files detailed report
# py.test testcase name : will run only testcase, py.test -k ABCD -v -s dX : will runtestcases whose namecontains ABCD
# -k stands for methods name execution, - s for logs, -v for detailed report
# mark with name smokeorABC, then use py.test -m smokeorABC to run test marked with smokeorABC
# data driven and parametrization can be done with return statements in tuple format
# pytest-s to run without capture
# functions must start from test, and classes must start from Test, classes cannot have constructors
# pytestmark = [pytest.mark.frontend, pytest.marl.slow]
# pytest --html = my_report.html --self-contained-html, css goes with the html, so you can export the file and send over email etc
# docs.qameta.io/allure/#_pytest
# pytest -W ignore::pytest.Warning name like pytest.PytestUnknownMarkWarning
# driver.switch_to_default_content(), to switch to original window back from iFrame
#original_window_handle = driver.current.window_handles; all_windows_handles = driver.window_handles # driver.window_handles will values of all windows open in the browser
#new_window = all_windows_handles[1]; driver.switch_to_window(original_window_handle)
#import string; import random
#letters = string.ascii_lowercase  ;  rand_string = ''.join(random.choice(letters) for i in range(15))
#random_email = rand_string +'@outlook.com'

import pytest


@pytest.mark.smokeorABC  # will mark the test case with name smokeorABC and can use - m smokeorABC to run
# all testcases marked with name smokeorABC
@pytest.mark.skip  # will skip the specific tescase
@pytest.mark.xfail  # will not show pass or fail of testcase in results, but will run and will give output like print
def test_first():
    print("Pytest Tests Code")


@pytest.fixture()
def beforeTest():  # will work like beforemethod
    print(" Wil run before test ")
    yield  # statement after yield keyword will work like aftermethod
    print("Will run after test")


def test_Test1(beforeTest):  # beforeTest in brackets will search for beforeTest method, and will execute that
    # first, also when writing beforeTest method in conftest, then any new method for which beforeTest method is
    # needed, we need to give beforeTest in bracket for that method, so it calls that first automatically
    # if beforeTest method is present in same file, will check for that first, if not then will check in conftest file
    print(" Run Test 1")


def test_Test2(beforeTest):
    print(" Run Test 2")


@pytest.mark.usefixtures("beforeTest")
class TestExample:

    def test_Test3(self): #defining a method under class, self keyword is mandatory
        print(" Run Test 3")

    def test_Test4(self):
        print(" Run Test 4")

@pytest.mark.usefixtures("dataLoad")
class TestExample2:
    def test_editProfile(self, dataLoad):
        print(dataLoad)
        print(dataLoad[0], dataLoad[1])

def test_crossbrowser(crossBrowser): #self not required as not within class
    print(crossBrowser)# print(crossBrowser[0])

