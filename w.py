from selenium import webdriver

from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

# n1 = browser.find_element_by_id('num1').text
# n2 = browser.find_element_by_id('num2').text
#
# y = int(n1) + int(n2)
# print(y)

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

browser.execute_script("window.scrollBy(0, 100);")

browser.find_element_by_id('answer').send_keys(y)
# select = Select(browser.find_element_by_tag_name("select"))
# select.select_by_value(str(y))

browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_id('robotsRule').click()
button = browser.find_element_by_xpath('//button[@type="submit"]')
button.click()