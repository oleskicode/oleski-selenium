from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

#Verify Page Name is correct and log the actual name into console
driver.get("https://www.saucedemo.com/")
print(f"driver.title: {driver.title}")
assert driver.title == "Swag Labs"
time.sleep(5)

#Verify clicking empty login pops up an error - Epic sadface: Username is required
assert driver.page_source.__contains__("Epic sadface: Username is required") == False #Verify Error is Absent
login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/form/input") #Full XPath
login_button.click()
time.sleep(5)
assert driver.page_source.__contains__("Epic sadface: Username is required") == True #Verify Error appears

#Verify clicking Close Error button removes the error
assert driver.page_source.__contains__("Epic sadface: Username is required") == True #Verify Error is shown
close_error_button = driver.find_element(By.CLASS_NAME, "error-button")
close_error_button.click()
time.sleep(5)
assert driver.page_source.__contains__("Epic sadface: Username is required") == False #Verify Error is Absent

#Fill in username WITHOUT password and click login - Error must appear
user_name_field = driver.find_element(By.ID, "user-name")
user_name_field.send_keys("standard_user")
login_button.click()
time.sleep(5)
assert driver.page_source.__contains__("Epic sadface: Password is required") == True #Verify Error is shown
time.sleep(5)

#Verify clicking Close Error button removes the error
close_error_button = driver.find_element(By.CLASS_NAME, "error-button")
close_error_button.click()
time.sleep(5)
assert driver.page_source.__contains__("Epic sadface: Password is required") == False #Verify Error is not shown

#Type in wrong password and click Login
password_field = driver.find_element(By.XPATH, '''//*[@id="password"]''') # Relative xpath
password_field.send_keys("some wrong password") #wrong password
login_button.click()
time.sleep(5)
assert driver.page_source.__contains__("Epic sadface: Password is required") == False #Verify Pass Req Error is not shown
assert driver.page_source.__contains__("Epic sadface: Username is required") == False #Verify Error is Absent
assert driver.page_source.__contains__("Epic sadface: Username and password do not match any user in this service") == True #Verify Error is Absent
time.sleep(5)

# Type correct login and pass. Verify login screen works and products are shown
# user_name_field = driver.find_element(By.ID, "user-name")
# user_name_field.send_keys("standard_user")
password_field = driver.find_element(By.XPATH, '''//*[@id="password"]''') # Relative xpath
password_field.clear() # delete/clear incorrect password from the field
time.sleep(5)
password_field.send_keys("secret_sauce") #correct password
login_button.click()
time.sleep(5)
assert driver.find_element(By.CSS_SELECTOR, "#header_container > div.header_secondary_container > span")
assert driver.find_element(By.CLASS_NAME, "shopping_cart_link")
assert driver.find_element(By.CLASS_NAME, "product_sort_container")

time.sleep(5)
# driver.quit()
print("Finishing up")