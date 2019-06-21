import unittest
from selenium import webdriver

class TestAbs(unittest.TestCase):

    def test_b(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_xpath('//input[@placeholder = "Введите имя"]').send_keys('qwe')
        browser.find_element_by_xpath('//input[@placeholder = "Введите фамилию"]').send_keys('qwe2')
        browser.find_element_by_xpath('//input[@placeholder = "Введите Email"]').send_keys('qwe3')

        browser.find_element_by_class_name('btn.btn-default').click()
        gt = browser.find_element_by_tag_name('h1').text


        self.assertEqual(gt, 'Поздравляем! Вы успешно зарегистировались!', 'успешно зарегистировались!')

    def test_a(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_xpath('//input[@placeholder = "Введите имя"]').send_keys('qwe')
        browser.find_element_by_xpath('//input[@placeholder = "Введите фамилию"]').send_keys('qwe2')
        browser.find_element_by_xpath('//input[@placeholder = "Введите Email"]').send_keys('qwe3')

        browser.find_element_by_class_name('btn.btn-default').click()
        gt = browser.find_element_by_tag_name('h1').text

        self.assertEqual(gt, 'Поздравляем! Вы успешно зарегистировались!', 'успешно зарегистировались!')


if __name__ == "__main__":
    unittest.main()