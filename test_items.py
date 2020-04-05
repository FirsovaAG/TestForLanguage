import time
from selenium.webdriver.remote.errorhandler import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button_to_add(browser):
    browser.get(link)
    try:
        assert browser.find_element_by_class_name("btn-add-to-basket")
    except NoSuchElementException:
        assert False, 'Button to add stuff on basket is not found'

    time.sleep(10)

    
    
    
 
