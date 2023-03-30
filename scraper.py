from requests import get
#3 product_code = input ("Please enter a prodcut code: ")
product_code= "36991221"
url = "https://www.ceneo.pl/{product_code}#tab=reviews"

response = get(url)
print(response.status_code)