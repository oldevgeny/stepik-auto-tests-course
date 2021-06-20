from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def main():
	try:
		link = "http://suninjuly.github.io/execute_script.html"
		browser = webdriver.Chrome()
		browser.get(link)


		x_ = browser.find_element_by_css_selector("label span#input_value")
		x = int(x_.text)
		y = calc(x)


		input1 = browser.find_element_by_css_selector("input#answer")
		input1.send_keys(y)


		option1 = browser.find_element_by_css_selector("input#robotCheckbox")
		_ = option1.location_once_scrolled_into_view
		option1.click()

		option2 = browser.find_element_by_css_selector("input#robotsRule")
		_ = option2.location_once_scrolled_into_view
		option2.click()
		

		button = browser.find_element_by_css_selector("button.btn")
		_ = button.location_once_scrolled_into_view
		button.click()

	finally:
		time.sleep(5)
		browser.quit()

if __name__ == '__main__':
	main()
