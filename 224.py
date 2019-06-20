from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
# import os
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait




def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

browser.implicitly_wait(12)
browser.get(link)

WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '10000 RUR')
    )


browser.find_element_by_class_name('btn.btn-primary').click()

# browser.switch_to.alert.accept()

# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)
x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

# browser.find_element_by_name('firstname').send_keys('IMA')
# browser.find_element_by_name('lastname').send_keys('IMA2')
# browser.find_element_by_name('email').send_keys('IMA2@dsf.rt')
#
# browser.find_element_by_id('file').send_keys(file_path)

browser.find_element_by_name('text').send_keys(y)
# browser.find_element_by_class_name('btn.btn-primary').click()
browser.find_element_by_id('solve').click()