import time

from selenium import webdriver
from RahulShetty.Login import Login
from RahulShetty.readproperties import Readconfig
import test_readexcel


class Testlogin(test_readexcel):
    # baseurl1: "https:www.zales.com"
    baseurl: Readconfig.getapplicationurl()
    path = ".//Desktop/test_Testdata.xlsx"
    # username1: ""
    username: Readconfig.getemail()
    # password1: ""
    password: Readconfig.getpassword()

    def test_Title(self):
        self.driver = webdriver.chrome()
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == "":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("#name of folder where want to save screenshot.\\Screenshots\\+test.png")
            self.driver.close()
            assert False

    def test_Login(self, openchrome):
        self.driver = openchrome
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        rows = test_readexcel.getRowCount(self.path, 'Sheet1')
        lst_status = []
        for r in range(2, self.rows + 1):
            self.user = test_readexcel.readData(self.path, 'Sheet1', r, 1)
            self.password = test_readexcel.readData(self.path, 'Sheet1', r, 2)
            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(4)
            act_title = self.driver.title
            exp_title = "title of page"
            if act_title == exp_title:
                print("Test case is pass")
                self.lp.clicklogout();
                lst_status.append("pass")
            else:
                print("Test case is fail")
                self.lp.clicklogout();
                lst_status.append("fail")



        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        # self.driver.close
        act_title = self.driver.title()
        if act_title == "":
            assert True
            self.driver.close()
        else:
            assert False
            self.driver.save_screenshot("#name of folder where want to save screenshot.\\Screenshots\\+test.png")
            self.driver.close()

