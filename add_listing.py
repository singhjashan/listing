# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time

# service = Service(r"D:\\PROJECTS\\listing\\chromedriver.exe")

# options = Options()
# options.add_argument("user-data-dir=D:\\PROJECTS\\listing\\user_profile")

# driver = webdriver.Chrome(service=service, options=options)
# driver.get("https://seller.flipkart.com/index.html#dashboard/listingsInProgress")

# time.sleep(2)

# listing_btn = driver.find_element(By.CLASS_NAME, "styles__ButtonStyle-sekd9q-0.uQOWs.add-new-listing-btn")
# listing_btn.click()
# # time.sleep(2)

# add_single_listing_btn = driver.find_element(By.CLASS_NAME, "styles__ListItem-sc-4vyflt-1 iZtuGw")
# add_single_listing_btn.click()
# # time.sleep(2)


# # Keep the browser open
# try:
#     input("Press Enter to close the browser...")  # Keeps the browser open until you manually close it
# finally:
#     driver.quit()




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import webbrowser 

  
# then make a url variable 
url = "https://seller.flipkart.com/index.html#dashboard/listingsInProgress?filters=%7B%22statusFilter%22%3A%7B%22checked%22%3A%5B%5D%7D%2C%22categoryFilter%22%3A%7B%22checked%22%3A%5B%5D%7D%2C%22marketplaceFilter%22%3A%7B%22checked%22%3A%5B%22FLIPKART%22%5D%7D%2C%22search%22%3A%22%22%2C%22bulkTypeIndex%22%3A0%2C%22requestType%22%3A%22cpui%22%2C%22listingType%22%3A%22single%22%2C%22epuiStatus%22%3A%22%22%2C%22searchType%22%3A%22%22%7D"

service = Service(r"D:\\PROJECTS\\listing\\chromedriver.exe")
driver = webdriver.Chrome(service=service)


# then call the default open method described above 
webbrowser.open(url)
time.sleep(2)



listing_btn = driver.find_element(By.CLASS_NAME, "styles__ButtonStyle-sekd9q-0 uQOWs add-new-listing-btn")
listing_btn.click()
time.sleep(2)

# add_single_listing_btn = driver.find_element(By.CLASS_NAME, "styles__ListItem-sc-4vyflt-1 iZtuGw")
# add_single_listing_btn.click()
# time.sleep(2)

