import pyautogui
import time
import webbrowser 
import read_data as book_info

            
# then make a url variable 
url = "https://seller.flipkart.com/index.html#dashboard/listingsInProgress?filters=%7B%22statusFilter%22%3A%7B%22checked%22%3A%5B%5D%7D%2C%22categoryFilter%22%3A%7B%22checked%22%3A%5B%5D%7D%2C%22marketplaceFilter%22%3A%7B%22checked%22%3A%5B%22FLIPKART%22%5D%7D%2C%22search%22%3A%22%22%2C%22bulkTypeIndex%22%3A0%2C%22requestType%22%3A%22cpui%22%2C%22listingType%22%3A%22single%22%2C%22epuiStatus%22%3A%22%22%2C%22searchType%22%3A%22%22%7D"
  

# then call the default open method described above 
webbrowser.open(url)
time.sleep(5)


for index, row in book_info.df.iterrows():
        
        
        # print(f"Processing row {index}: {row.to_dict()}")
        book_info = row.to_dict()
        # print(book_info)
        sku = book_info['SKU']
        isbn = book_info['ISBN']
        author = book_info['Author']
        title = book_info['Title']
        price = book_info['Price']
        print(sku)
        print(isbn)
        print(author)
        print(title)
        print(price)
        print("------------------------------------------------------------------------------")
        
        # click on add new listing button
        pyautogui.click(1761,307, duration=2 )

        # click on Add single listing button
        pyautogui.click(1759,373, duration=1 )
        time.sleep(5)

        # click on book
        pyautogui.click(508,784, duration=2)
        time.sleep(3)

        # click on select publisher
        pyautogui.click(1547,942, duration=2)
        time.sleep(2)


        # click on Enter publisher name
        pyautogui.click(231,575, duration=2)

        # entring book name
        pyautogui.typewrite(title)

        # click on check brand
        pyautogui.click(451,577,duration=2)


        # click on create new listing btn
        pyautogui.click(166,704,duration=2)

        # click on + to add a picutre
        pyautogui.click(454,820, duration=2)

        # click to upload a photo
        pyautogui.click(82,657,duration=2)

        # click to enter path of pic
        # setting all type 
        pyautogui.click(944,588,duration=2)
        pyautogui.typewrite("All Files")
        
        
        time.sleep(0.5)
        pyautogui.doubleClick(388,589,duration=2)
        # enter path of picture
        pyautogui.typewrite(f"D:\\books\\{isbn}")
        # uploading the image
        pyautogui.press("enter")
        time.sleep(3)

        # saving the image
        pyautogui.click(788,597,duration=2)
        time.sleep(5)

        # click on edit to eter details
        pyautogui.click(1462,586,duration=1)

        # click on SKU ID
        pyautogui.click(1044,859,duration=1)
        pyautogui.typewrite(sku)
        # time.sleep(0.5)


        pyautogui.press("tab")

        # Listing Status
        pyautogui.typewrite("Active")
        # time.sleep(0.5)
        pyautogui.press("tab")


        # MRP 
        pyautogui.typewrite(str(price))
        # time.sleep(0.5)
        pyautogui.press("tab")

        # Sell price
        sell_price = price - 50
        pyautogui.typewrite(str(sell_price))
        # time.sleep(0.5)
        pyautogui.press("tab")

        # Minimum Order Quantity 
        pyautogui.typewrite("1")
        # time.sleep(0.5)
        pyautogui.press("tab")

        # Fullfilment by
        pyautogui.typewrite("Seller")
        # time.sleep(0.5)
        pyautogui.press("tab")

        # Procurement type 
        pyautogui.typewrite("Instock")
        # time.sleep(0.5)
        pyautogui.press("tab")

        # Procurement SLA 
        pyautogui.typewrite("2")
        # time.sleep(0.5)
        pyautogui.press("tab")

        # Stock 
        pyautogui.typewrite("1")
        # time.sleep(0.5)
        pyautogui.press("tab")

        # Shipping provider
        pyautogui.typewrite("Flipcart")
        # time.sleep(0.5)
        pyautogui.press("tab")

        # Local delivery charge
        pyautogui.typewrite("0")
        # time.sleep(0.5)
        pyautogui.press("tab")
        # Zonal delivery charge
        pyautogui.typewrite("0")
        # time.sleep(0.5)
        pyautogui.press("tab")
        # National delivery charge
        pyautogui.typewrite("0")
        # time.sleep(0.5)
        pyautogui.press("tab")

        # Length
        # time.sleep(2)
        pyautogui.typewrite("2")
        pyautogui.press("tab")

        # pyautogui.click()
        pyautogui.typewrite("22")
        time.sleep(0.5)
        pyautogui.press("tab")
        # Breadth 
        pyautogui.typewrite("14")
        # time.sleep(0.5)
        pyautogui.press("tab")
        # Height 
        pyautogui.typewrite("7")
        # time.sleep(0.5)
        pyautogui.press("tab")
        # Weight 
        pyautogui.typewrite("0.111")
        # time.sleep(0.5)
        pyautogui.press("tab")

        # HSN 
        pyautogui.typewrite("49011010")
        # time.sleep(0.5)
        pyautogui.press("tab")

        # Luxury Cess
        pyautogui.typewrite("1")
        # time.sleep(0.5)
        pyautogui.press("tab")

        # Tax Code
        pyautogui.typewrite("GST_0")
        # time.sleep(0.5)
        pyautogui.press("tab")

        # Country Of Origin
        pyautogui.typewrite("India")
        # time.sleep(0.5)
        pyautogui.press("tab")

        # Manufacturer Details
        pyautogui.typewrite("Made in India")
        # time.sleep(0.5)
        pyautogui.press("tab")

        # Packer Details
        pyautogui.typewrite("Made in India")
        # time.sleep(0.5)
        # pyautogui.press("tab")

        # clicl on save to save details
        pyautogui.click(1440,556,duration=1)

        time.sleep(2)
        # click on edit to edit #Product Description # 
        pyautogui.click(1808,652,duration=2)

        # click ISBN13 
        pyautogui.click(1339,839,duration=2)
        pyautogui.typewrite(str(isbn))
        pyautogui.press("tab")
        pyautogui.press("tab")

        # Title 
        pyautogui.typewrite(title)
        pyautogui.press("tab")


        # Author 
        pyautogui.typewrite(author)
        pyautogui.press("tab")
        pyautogui.press("tab")

        # Product Form
        pyautogui.typewrite("Paperback")
        pyautogui.press("tab")


        # Language 
        pyautogui.typewrite("English")
        pyautogui.press("tab")
        pyautogui.press("tab")

        # Book Subcategory
        pyautogui.typewrite("Other Books")

        # click on save to save Product Description  details
        pyautogui.click(1782,571,duration=2)


        time.sleep(5)
        # click on send to QC
        pyautogui.click(1768,337,duration=3)
        
        time.sleep(3)
        
        pyautogui.scroll(1000)



  









x, y = pyautogui.position()
print("Current mouse position: X =", x, "Y =", y)
