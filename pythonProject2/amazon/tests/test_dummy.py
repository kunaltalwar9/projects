import pytest

#pytest-s to run without capture
#functions must start from test, and classes must start from Test, classes cannot have constructors
@pytest.mark.usefixtures('init_driver')
class TestDummy:
    def test_dummy(self):
        print("Hi")
        self.driver.get("https://www.amazon.in/")
        #http://demostore.supersqa.com/my-account/
        import pdb; pdb.set_trace()


