import pytest


@pytest.mark.usefixtures('init_driver')
class TestDummy:
    def test_dummy(self):
        print("Hi")
        self.driver.get("https://www.amazon.in/")
        import pdb; pdb.set_trace()


