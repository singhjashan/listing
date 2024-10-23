import webbrowser 
  
# then make a url variable 
url = "https://seller.flipkart.com/index.html#dashboard/listingsInProgress?filters=%7B%22statusFilter%22%3A%7B%22checked%22%3A%5B%5D%7D%2C%22categoryFilter%22%3A%7B%22checked%22%3A%5B%5D%7D%2C%22marketplaceFilter%22%3A%7B%22checked%22%3A%5B%22FLIPKART%22%5D%7D%2C%22search%22%3A%22%22%2C%22bulkTypeIndex%22%3A0%2C%22requestType%22%3A%22cpui%22%2C%22listingType%22%3A%22single%22%2C%22epuiStatus%22%3A%22%22%2C%22searchType%22%3A%22%22%7D"
  
# then call the default open method described above 
webbrowser.open(url)