from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(.3)
    apply_style(original_style)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/maps")
print(driver.title)

#ENTER INTO MAIN SEARCH BAR
search = driver.find_element_by_id("searchboxinput")
#search = driver.find_element_by_name("q")
highlight(search)
search.send_keys("Belmar, Ocean Avenue, Belmar, NJ")
search.send_keys(Keys.RETURN)
time.sleep(5)

#CLICK ON DIRECTIONS BUTTON
#print(driver.page_source)
search = driver.find_element_by_class_name("iRxY3GoUYUY__taparea")
highlight(search)
search.click()
time.sleep(5)


#ENTER IN HOME ADDRESS

search = driver.find_element_by_xpath("//input[@placeholder='Choose starting point, or click on the map...']")
#search = driver.find_element_by_class_name("sbib_b")
#search = driver.find_element_by_class_name("tactile-searchbox-input")
highlight(search)
print("Element is visible? " + str(search.is_displayed()))
search.send_keys("Montville, NJ")
search.send_keys(Keys.RETURN)
time.sleep(5)


#GET THE DETAILS
search = driver.find_element_by_id("section-directions-trip-details-msg-0")
highlight(search)
search.click()
time.sleep(5)

#CLICK ON DRIVING BUTTON
search = driver.find_element_by_class_name("directions-travel-mode-underline")
highlight(search)
#print("Element is visible? " + str(search.is_displayed()))
#search[0].click()
time.sleep(5)



#search.send_keys("Montville, New Jersey")


#search.send_keys(Keys.RETURN)


time.sleep(20)

driver.quit()

