import pytest


# if writing fixture in conftest, then do not need to write in any else testcase
@pytest.fixture(scope="class") # scope = class will run method within fixture once before the class and
# yield's below statement after class, will run once and after class not before and after each test case
def beforeTest():  # will work like beforemethod
    print(" Wil run before test ")
    yield  # statement after yield keyword will work like aftermethod
    print("Will run after test")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul ","SHetty","rahulshetty.com"]

@pytest.fixture(params=[" chrome"," firefox"," IE"])  # params=[("chrome", "ABCD", "DEF")," firefox"," IE"]
def crossBrowser(request):
    return request.param
