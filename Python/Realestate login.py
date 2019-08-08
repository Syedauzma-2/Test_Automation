from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome("C:\\Users\\lts\\PycharmProjects\\Test_Automation\\Drivers\\chromedriver.exe")

driver.maximize_window()


driver.get("http://real-estate.itechscripts.com/login.php")

time.sleep(5)

driver.find_element_by_xpath("//input[@id='login_username']").clear()
time.sleep(3)

driver.find_element_by_xpath("//input[@id='login_username']").send_keys("userdemo@yourmail.com")
time.sleep(3)

driver.find_element_by_xpath("//input[@id='login_password']").clear()
time.sleep(3)


driver.find_element_by_xpath("//input[@id='login_password']").send_keys("userdemo")
time.sleep(3)

driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
time.sleep(2)

driver.switch_to.alert.accept()



# #register
# element=driver.find_element_by_xpath(".//*[@id='undefined-sticky-wrapper']/div/div/div/div/nav/ul/li[2]/a")
# time.sleep(2)
#
# hover = ActionChains(driver).move_to_element(element)
# hover.perform()
# driver.implicitly_wait(5)
#
# driver.find_element_by_xpath(".//*[@id='undefined-sticky-wrapper']/div/div/div/div/nav/ul/li[2]/ul/li/a").click()
# time.sleep(1)
#
# # Register form
# driver.find_element_by_xpath(".//*[@id='company_name']").send_keys("Mindsnxt")
# time.sleep(3)
#
# driver.find_element_by_xpath(".//*[@id='contact_prson']").send_keys("xyz")
# time.sleep(3)
#
# driver.find_element_by_xpath(".//*[@id='cmpny_email']").send_keys("userdemo@gmail.com")
# time.sleep(3)
#
# driver.find_element_by_xpath("//*[@id='profile_image']").send_keys('C:\\Users\\lts\\Desktop\\intrenship\\upload.PNG')
#
# driver.find_element_by_xpath(".//*[@id='mobile_phone']").send_keys("1234565677")
# time.sleep(2)
#
# driver.find_element_by_xpath(".//*[@id='work_phone']").send_keys("9876543210")
# time.sleep(3)
#
# driver.find_element_by_xpath(".//*[@id='about_me']").send_keys("iam a good person")
# time.sleep(3)
#
# driver.find_element_by_xpath(".//*[@id='agnt_password']").send_keys("@1234")
# time.sleep(3)
#
# driver.find_element_by_xpath(".//*[@id='agnt_cpassword']").send_keys("@1234")
# time.sleep(3)
#
# driver.find_element_by_xpath(".//*[@id='agent_registration']/input").click()
# time.sleep(3)
#
# # driver.switch_to.alert.accept()
#
#
# driver.find_element_by_xpath(".//*[@id='undefined-sticky-wrapper']/div/div/div/div/nav/ul/li[1]/a").click()
# time.sleep(8)

#drop_down
#Contract
driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/button[1]').click()
time.sleep(1)
driver.find_element_by_xpath('html/body/div[2]/div/ul/li[2]/a').click()
time.sleep(2)

#type

driver.find_element_by_xpath("html/body/div[1]/div[1]/div[3]/div/div/form/div/div[1]/div[2]/div/button").send_keys("All Residential")
time.sleep(2)



#country
driver.find_element_by_xpath("html/body/div[1]/div[1]/div[3]/div/div/form/div/div[1]/div[3]/div/button").click()
time.sleep(2)
driver.find_element_by_xpath("html/body/div[4]/div/ul/li[2]/a").click()
time.sleep(4)

#city
driver.find_element_by_xpath(".//*[@id='city']").send_keys("Chennai")
time.sleep(2)


#Advanced search
driver.find_element_by_xpath("//a[@id='ads-trigger']").click()
time.sleep(2)

#max and min price

driver.find_element_by_xpath("//input[@id='min_price']").clear()
time.sleep(3)
driver.find_element_by_xpath("//input[@id='min_price']").send_keys("0")
time.sleep(3)

driver.find_element_by_xpath("//input[@id='max_price']").clear()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='max_price']").send_keys("20000")
time.sleep(3)
#search
driver.find_element_by_xpath("html/body/div[1]/div[1]/div[3]/div/div/form/div/div[1]/div[5]/button").click()
time.sleep(3)


#image details
driver.find_element_by_xpath(".//*[@id='content']/div/div/div[1]/div[2]/ul/li[1]/div[1]/a/div").click()
time.sleep(3)

#Scroll_Down
elm = driver.find_element_by_tag_name('html')
elm.send_keys(Keys.END)
time.sleep(3)
elm.send_keys(Keys.PAGE_UP)
time.sleep(4)
elm.send_keys(Keys.HOME)


#Screenshots
driver.get_screenshot_as_file("C:\\Users\\lts\\Pictures\\Screenshot\\Real.png")

#Agent Mouse Hover
element=driver.find_element_by_xpath(".//*[@id='undefined-sticky-wrapper']/div/div/div/div/nav/ul/li[3]/a")
time.sleep(2)
hover = ActionChains(driver).move_to_element(element)
hover.perform()
driver.implicitly_wait(5)

driver.find_element_by_xpath(".//*[@id='undefined-sticky-wrapper']/div/div/div/div/nav/ul/li[3]/ul/li/a").click()
time.sleep(3)

#Agent scroll down
elm = driver.find_element_by_tag_name('html')
elm.send_keys(Keys.END)
time.sleep(3)
elm.send_keys(Keys.PAGE_UP)
time.sleep(4)
elm.send_keys(Keys.HOME)

#properties mouse hover
element=driver.find_element_by_xpath(".//*[@id='undefined-sticky-wrapper']/div/div/div/div/nav/ul/li[4]/a")
time.sleep(2)
hover = ActionChains(driver).move_to_element(element)
hover.perform()
driver.implicitly_wait(5)

driver.find_element_by_xpath(".//*[@id='undefined-sticky-wrapper']/div/div/div/div/nav/ul/li[4]/ul/li[1]/a").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='undefined-sticky-wrapper']/div/div/div/div/nav/ul/li[4]/ul/li[1]/ul/li[2]/a").click()
time.sleep(3)


driver.quit()



