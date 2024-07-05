from AppiumFrameWork.base.DriverClass import Driver
import AppiumFrameWork.utilities.CustomLogger as cl
from AppiumFrameWork.base.BasePage import BasePage

driver1 = Driver()
log = cl.customLogger()
driver = driver1.getDriverMethod()
log.info("Launch APP")
bp = BasePage(driver)
bp.screenShot("App")
element = bp.waitForElement("com.code2lead.kwad:id/ContactUs","id")
element.click()
element = bp.isDisplayed("com.code2lead.kwad:id/ContactUs","id")
print(element)
bp.clickElement("com.code2lead.kwad:id/ContactUs","id")
bp.sendText("Code2Lead","Enter Name","text")
bp.screenShot("cod2Lead")