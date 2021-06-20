from selenium import webdriver
import time

def main():
    try: 
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        num_list = ['first', 'second', 'third']
        for num in num_list:
            element = browser.find_element_by_css_selector(".first_block .form-control.{}".format(num))
            element.send_keys("My answer")

        time.sleep(2)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(3)
        browser.quit()

if __name__ == '__main__':
    main()
