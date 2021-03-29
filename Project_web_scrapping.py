# web scrapping using python with requests and BeautifulSoup

import requests
from bs4 import BeautifulSoup4

import pandas # we are using this library for storing our output 

url = "https://www.oyorooms.com/hotels-in-bangalore/"

# Now we are taking HTML from website
r = requests.get(url)
content = r.content
print(content) # here just printing HTML code for just our consern

# now just we are parsing HTML code
soup = BeautifulSoup(content , 'html.parser')
print(soup.prettify)

hotels = soup.find_all("div", {"class": "hotelCardListing"})
Hotels_info_list = []

for hotel in hotels:
    
    hotel_name["Name"] = hotel.find("h3", {"class": "listingHotelDescription__hotelName"}).text
    hotel_address["Address"] = hotel.find("span" , {"itemprop" : "StreetAddress"}).text
    hotel_price["Price"] = hotel.find("span" , {"class" : "listingPrice__finalPrice"}).text

    parent_amenities = hotel.find("div" , {"class" : "amenityWrapper"})
    parent_amenity = parent_amenities.find_all("div" , {"class" : "amenityWrapper__amenity"})    
    
    amenity_list = []
    for amenity in parent_amenity:
        amenity_list.append(amenity.find("span" , {"class" : "d-body-sm"}).text.strip())

        # By this we are joining list objects with string fuction: "join"
        # And creating dictionary to store values
        # here (-1) stands for list neglates last element
        hotel_dict["amenity"] = ', '.join(amenity_list[:-1])
        
        Hotels_info_list.append(hotel_dict)

Information = pandas.DataFrame(Hotels_info_list)
# just creating csv file with function "to_csv"
Information.to_csv("Hotels_Information.csv")