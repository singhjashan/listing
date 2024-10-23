# import pygetwindow as gw

# # Print all window titles and their sizes
# for window in gw.getAllWindows():
#     title = window.title
#     width, height = window.width, window.height
#     print(f"Title: {title} - Width: {width}, Height: {height}")

import pygetwindow as gw

def resize_window(title, width, height):
    try:
        # Get the window by title
        window = gw.getWindowsWithTitle(title)[0]

        # Resize the window
        window.resizeTo(width, height)
        print(f"Resized '{title}' to Width: {width}, Height: {height}")
    except IndexError:
        print(f"Window with title '{title}' not found.")

# Example usage
resize_window('chrome', 942, 543)

