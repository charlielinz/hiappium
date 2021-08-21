from appium import webdriver

desired_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.google.android.calculator",
    "appActivity": "com.android.calculator2.Calculator",
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

# numbers
num1 = driver.find_element_by_id("com.google.android.calculator:id/digit_1")
num2 = driver.find_element_by_id("com.google.android.calculator:id/digit_2")
num3 = driver.find_element_by_id("com.google.android.calculator:id/digit_3")
num4 = driver.find_element_by_id("com.google.android.calculator:id/digit_4")
num5 = driver.find_element_by_id("com.google.android.calculator:id/digit_5")
num6 = driver.find_element_by_id("com.google.android.calculator:id/digit_6")
num7 = driver.find_element_by_id("com.google.android.calculator:id/digit_7")
num8 = driver.find_element_by_id("com.google.android.calculator:id/digit_8")
num9 = driver.find_element_by_id("com.google.android.calculator:id/digit_9")
num0 = driver.find_element_by_id("com.google.android.calculator:id/digit_0")

# operators
op_mais = driver.find_element_by_accessibility_id("plus")
op_multi = driver.find_element_by_accessibility_id("multiply")
op_menos = driver.find_element_by_accessibility_id("minus")
op_div = driver.find_element_by_accessibility_id("divide")

# common
op_igual = driver.find_element_by_accessibility_id("equals")


num1.click()
op_mais.click()
num2.click()
op_igual.click()
