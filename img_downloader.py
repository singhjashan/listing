import requests

def download_image(url, file_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while downloading the image: {e}")

# Example usage
image_url = 'Fundamentals of Communication Systems'
file_path = r'D:\\PROJECTS\\listing\\images\\01.jpg'
download_image(image_url, file_path)
