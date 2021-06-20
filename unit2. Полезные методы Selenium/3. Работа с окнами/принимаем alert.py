from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def main():
	try:
		link = "http://suninjuly.github.io/alert_accept.html"
		browser = webdriver.Chrome()
		browser.get(link)

		button1 = browser.find_element_by_css_selector("button.btn")
		button1.click()

		confirm = browser.switch_to.alert
		confirm.accept()

		x_ = browser.find_element_by_css_selector("label span#input_value")
		x = int(x_.text)
		y = calc(x)


		input1 = browser.find_element_by_css_selector("input#answer")
		input1.send_keys(y)

		button = browser.find_element_by_css_selector("button.btn")
		button.click()

	finally:
		time.sleep(5)
		browser.quit()

if __name__ == '__main__':
	main()
