from selenium import webdriver
import time


def main():
	try:
		link = "http://suninjuly.github.io/selects2.html"
		browser = webdriver.Chrome()
		browser.get(link)


		x_ = browser.find_element_by_css_selector("h2 #num1")
		x = x_.text

		y_ = browser.find_element_by_css_selector("h2 #num2")
		y = y_.text

		sum_ = int(x) + int(y)

		browser.find_element_by_css_selector("[value='{0}']".format(sum_)).click()
		

		button = browser.find_element_by_css_selector("button.btn")
		button.click()

	finally:
		time.sleep(10)
		browser.quit()

if __name__ == '__main__':
	main()
