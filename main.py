import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
index= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
number=0
url = f"https://www.systemrequirementslab.com/all-games-list/?filter={index[number]}"
length=len(index)


while True:

# Send an HTTP GET request to the URL
    response = requests.get(url)

# Check if the request was successful (status code 200)
    if response.status_code == 200:
    # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

    # Find the HTML elements that contain the product names
    # You need to inspect the website's HTML to find the right selector
        product_name_elements = soup.find_all('li', class_='page-item')

        if not product_name_elements:
            break
    
    
    # Extract and write the product names to a text file
        with open('product_names.txt', 'w') as file:
            for product_name_element in product_name_elements:
                product_name = product_name_element.text.strip()
                file.write(product_name + '\n')

        print(f"finished {index[number]}")

        
        if(number!=length):
            number+=1
        

    else:
        print(f"Failed to retrieve page {index}. Status code:", response.status_code)
        break

print("Product names have been written to product_names.txt")
