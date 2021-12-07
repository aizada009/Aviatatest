import webdriver

browser = webdriver.Chrome()
browser.get("http://https://aviata.kz/")
elem = browser.find_element_by_id("desktop-city-from").click()
elem.send_keys('Город')
