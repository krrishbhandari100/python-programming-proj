# /html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[11]/div/div/div[2]/div[1]/div[1]/span/span - praveen
# /html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2] - textbox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
a = input("Enter any key")
praveen = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[11]/div/div/div[2]/div[1]/div[1]/span/span")
praveen.click()
text_box = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
text_box.send_keys("Can you listen me")
driver.close()