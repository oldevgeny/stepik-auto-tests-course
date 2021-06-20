from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def main():
	try:
		link = "http://suninjuly.github.io/redirect_accept.html"
		browser = webdriver.Chrome()
		browser.implicitly_wait(5)
		browser.get(link)

		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		new_window = browser.window_handles[1]
		browser.switch_to.window(new_window)

		x_ = browser.find_element_by_css_selector("label span#input_value")
		x = int(x_.text)
		y = calc(x)

		input1 = browser.find_element_by_css_selector("input#answer")
		input1.send_keys(y)

		submit_button = browser.find_element_by_css_selector("button.btn")
		submit_button.click()

		print(browser.switch_to.alert.text.split(': ')[-1])

	finally:
		time.sleep(1)
		browser.quit()

if __name__ == '__main__':
	main()
