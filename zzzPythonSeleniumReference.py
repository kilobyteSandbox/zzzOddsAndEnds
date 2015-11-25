# =========================
# Python Selenium Reference 
# =========================


# Selenium Docs:
# http://selenium-python.readthedocs.org/en/latest/getting-started.html


# Scripting resource:
# http://www.slideshare.net/Lohika_Odessa_TechTalks/selenium-py-test-by-alexandr-vasyliev





# Script Snipits
# ==============

# Use example:
# driver.find_element_by_xpath(".//*[@id='Password']").send_keys("Aardvark")

# def login_field(self):
#	return self.wait.until(EC.element_to_be_clickable((By.NAME, 'Login')))


# XPath
driver.find_element_by_xpath()


# Click
.click()


# Keys
.send_keys("StringText")
.send_keys(Keys.ARROW_DOWN)


# Clear
.clear()


# Wait (in seconds)
time.sleep(1)


# Focus on alert
alert = driver.switch_to.alert
# May need a wait before proceeding
# Accept alert
alert.accept()
# Dismiss alert
alert.dismiss()


# Assert (stops test if fails)
# Title is webpage title
assert "Python" in driver.title
self.assertIn("Python", driver.title)
assert "No results found." not in driver.page_source


#Verify (does not stop test if fails)





# List of find_
# =============

find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector





# Tools
# =====

#Create date and time string
timeHours = time.strftime("%H:%M:%S")
timeDate = time.strftime("%Y/%m/%d")
varDateHours = timeDate + "_" + timeHours


# Lorem Ipsum string (450 chars)
varLoremIpsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In in enim a sapien ultricies mollis. Nulla facilisis ac dui a dictum. Ut vel commodo est. Phasellus ex neque, egestas quis accumsan pellentesque, facilisis ut quam. Pellentesque pellentesque nisi ex, sed eleifend diam auctor et. Morbi quis diam non ipsum ullamcorper commodo sed quis augue. Cras mollis, nisl sodales bibendum lobortis, sem risus lobortis elit, vehicula elit magna nec nulla. "





# Boilerplate
# ===========

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time



class NameOfTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_nameOfCase(self):
        driver = self.driver
        driver.get("http://website.com")


        # Automation start

        # elem = driver.find_element_by_id("UserEmailOrUsername")
       
        # Etc.


if __name__ == "__main__":
    unittest.main()







