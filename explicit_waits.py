from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait# as WDW
from selenium.webdriver.support import expected_conditions as EC
import time
import math
  
link = "http://suninjuly.github.io/explicit_wait2.html" 
  
  
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	webdriver = webdriver.Chrome()
	webdriver.get(link)
	#wait 5 sec for each element
	webdriver.implicitly_wait(5)
	#WebDriverWait и expected_conditions)
	price = WebDriverWait(webdriver, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "$100")
		)
	book = webdriver.find_element_by_id("book")
	book.click()
	
	x = webdriver.find_element_by_id("input_value").text
	y = calc(x)
	
	input_field = webdriver.find_element_by_id('answer').send_keys(y)
	
	submit = webdriver.find_element_by_id('solve').click()
	
	
	
finally:
	time.sleep(5)
	webdriver.quit()