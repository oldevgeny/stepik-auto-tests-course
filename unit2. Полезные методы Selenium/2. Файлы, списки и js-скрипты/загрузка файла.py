from selenium import webdriver
import time
import os

def main():
	try:
		link = "http://suninjuly.github.io/file_input.html"
		browser = webdriver.Chrome()
		browser.get(link)

		input1 = browser.find_element_by_css_selector(".form-group [name=firstname]")
		input1.send_keys("firstname")

		input2 = browser.find_element_by_css_selector(".form-group [name=lastname]")
		input2.send_keys("lastname")

		input3 = browser.find_element_by_css_selector(".form-group [name=email]")
		input3.send_keys("email@mail.ru")

		current_dir = os.path.abspath(os.path.dirname(__file__))
		file_path = os.path.join(current_dir, 'file.txt')
		input4 = browser.find_element_by_css_selector("input[type=file]")
		input4.send_keys(file_path)
		print(file_path)

		button = browser.find_element_by_css_selector("button.btn")
		_ = button.location_once_scrolled_into_view
		button.click()

	finally:
		time.sleep(5)
		browser.quit()

if __name__ == '__main__':
	main()
