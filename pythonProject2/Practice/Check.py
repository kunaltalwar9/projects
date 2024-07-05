import time
import OpenBrowser
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Firefox(
    #executable_path=r"C:\Users\Kunal Talwar\eclipse-workspace\libs\geckodriver-v0.30.0-win64\geckodriver.exe")

OpenBrowser.openchrome()
time.sleep(1)


def signin():
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="main-container"]/div[2]/header/div[1]/div/div[2]/ul/li[1]/a[1]').click()


'''
class MyTestCase(unittest.TestCase):
    def read_data():
        path= 
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
'''
