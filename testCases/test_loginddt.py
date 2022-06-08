import pytest

from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen
from utilities import XLUtils

file = r"C:\Users\\rajee\OneDrive\Desktop\Selenium\Hybrid_framework\TestData\Data.xlsx"
row = XLUtils.getRowCount(file, "Sheet1")
lis_data = []
for r in range(2, row + 1):
    usrname = XLUtils.readData(file, "Sheet1", r, 1)
    password = XLUtils.readData(file, "Sheet1", r, 2)
    exp = XLUtils.readData(file, "Sheet1", r, 3)
    lis_data.append((usrname, password, exp))


@pytest.mark.parametrize("usernam, pas,expected", lis_data)
class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationUrl()
    logger = LogGen.loggen()
    lis_status = []

    def test_login(self, setup, usernam, pas, expected):
        self.logger.info("************Test_002_DDT_Login started ***************")
        self.logger.info("************test_login started ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(usernam)
        self.lp.setPassword(pas)
        self.lp.clickLogin()
        actual_title = self.driver.title
        expected_title = "Dashboard / nopCommerce administration"

        if actual_title == expected_title:
            if expected == "pass":
                self.logger.info("******Passed****")
                self.lp.clickLogout()
                self.lis_status.append("pass")
            elif expected == "fail":
                self.logger.info("******Failed****")
                self.lp.clickLogout()
                self.lis_status.append("fail")

        elif actual_title != expected_title:
            if expected == "pass":
                self.logger.info("******Failed****")
                self.lis_status.append("fail")
            elif expected == "fail":
                self.logger.info("******Passed****")
                self.lis_status.append("pass")
        self.driver.quit()
        print(self.lis_status)

        if "fail" not in self.lis_status:
            self.logger.info("******Test_002_DDT_Login success****")
            print("DDT is passed")
            assert True
        else:
            self.logger.info("******Test_002_DDT_Login Unsuccess****")
            print("DDT is Failed")
            assert False
