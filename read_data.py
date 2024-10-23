import pandas as pd

# Load the Excel file
file_path = r'D:\\PROJECTS\\listing\\price list.xlsx'
df = pd.read_excel(file_path)


# Display the first few rows of the dataframe
# print(df.head(100))
# price_lst = df.head(100)

# print(df.iterrows())

# for index, row in df.iterrows():
#         # print(f"Processing row {index}: {row.to_dict()}")
#         book_info = row.to_dict()
#         # print(book_info)
#         isbn = book_info['ISBN']
#         author = book_info['Author']
#         title = book_info['Title']
#         price = book_info['Price']
#         print(isbn)
#         print(author)
#         print(title)
#         print(price)
#         print("------------------------------------------------------------------------------")