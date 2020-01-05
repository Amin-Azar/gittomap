import json
import plotly.express as px
import plotly.io as pio
import pandas as pd
import requests
import sys
from requests.auth import HTTPBasicAuth
from tkinter import *

locs= ['where the eigens are valued', None, 'UC Berkeley', 'Blacksburg, VA', None, None, None, 'Shanghai', 'Los Angeles', 'Vienna, Austria', None, None, 'NASA Ames Research Center', 'Amsterdam', 'University of Michigan', 'Germany', 'Philadelphia, PA', 'San Francisco, CA', 'San Francisco, CA', None, 'Darmstadt', None, None, None, 'California', 'Malmö, Sweden', 'Seattle, WA', None, 'Beijing, China', None, 'San Francisco, CA', 'Various places', None, 'Ukraine, Mariupol', None, None, None, 'Luxembourg & Shanghai', None, 'where the eigens are valued', 'Redmond, WA', None, 'Canberra', None, 'Turkiye', None, 'Wroclaw, Poland', 'Valencia, Spain', 'Lagos , Nigeria', None, None, 'Menlo Park, California', 'Redmond, WA', 'Seattle', 'Los Angeles, CA', None, 'Nova Friburgo - RJ - Brasil', None, None, 'Germany', 'Oakland, CA', None, 'Austria', 'Paris', 'Birmingham, UK', 'Redmond, WA', 'Universidad Autónoma de Madrid (Spain)', 'Omsk', None, 'Seattle, WA', None, 'Cologne', '東中野東京都', 'BeiJing, China', 'INRIA Rennes Bretagne Atlantique - France', 'United States', 'Grenoble, France - Lavras, Brazil - São Carlos, Brazil', None, 'Ukraine, Kiev UTC +03:00', None, 'Redmond, WA', None, None, 'Sweden', 'Victoria, BC', None, None, 'San Jose, CA', None, None, 'India', None, 'Tokyo, Japan', None, 'Troisdorf, Germany', None, 'Austria', 'Oslo', 'China', 'Menlo Park, California', None, None, None, None, None, None, 'USA', None, 'Sydney', None, None, None, None, 'Tulsa', 'South Korea', 'Worcester, MA', None, 'Bengaluru, India', None, 'San Francisco', 'London', None, 'The Milky Way', None, 'Redmond, WA', 'Sri Lanka', None, None, 'Toronto, Canada', None, 'Armonk, New York, U.S.', 'Istanbul', 'Hangzhou, China', None, 'Nanjing,China', 'Beijing', 'Redmond, WA', 'Japan', None, None, None, None, 'Vilnius', 'Edinburgh. Scotland', 'The Web', 'Tokyo, Japan', 'Seoul, South Korea', None, None, 'Saarland University', None, 'Redwood City, Ca', 'Shanghai', None, 'Brisbane, Australia', None, 'United States', 'San Diego, CA', 'Shanghai, China', None, 'San Jose, CA', None, 'Menlo Park, California', None, None, 'Toronto', 'NYC', 'San Jose', 'Toulouse, France', 'London, UK', 'Los Angeles, California', None, 'Barcelona', 'Nigeria', 'Beijing, China', 'Toronto, Canada', None, None, 'San Francisco, CA', 'Cambridge, MA', 'Porto', None, 'New York City', 'Cambridge, MA', None, 'Los Angeles, CA', 'Mountain View, CA', 'Philadelphia, PA', 'Beijing, China', None, None, None, 'San Jose, CA', 'brazil - sao paulo', None, None, 'Mountain View, CA', 'Birmingham, UK', 'Hangzhou, China', 'Chennai', 'Birmingham, UK', 'Linz, Austria', 'San Francisco, CA', 'Paris', None, None, None, None, None, None, 'Saint-Petersburg, Russia', 'Birmingham, UK', 'Reykjavík, Iceland', None, 'Shanghai', 'Toronto, Canada', None, 'Canada', 'London', 'Birmingham, UK', 'Redmond, WA', None, None, 'Ottawa, Canada', 'Berlin, Germany', None, None, None, 'Mountain View, CA', 'Pune, India', None, None, 'Enschede, The Netherlands', 'Birmingham, UK', 'HangZhou in China', 'San Francisco', 'Waterloo', 'San Francisco', 'Tokyo, Japan', None, None, 'Birmingham, UK', None, 'California', None, 'Bangkok', 'Boston, MA', None, 'Nanchang', 'Beijing, China', 'Bogotá', 'Amersfoort', 'Birmingham, UK', 'Redmond, WA', None, 'Austin, Texas', None, 'Edinburgh, UK', None, 'Zagreb', None, None, None, None, 'Netherlands', 'Croatia', None, None, 'Shunhua load No.1500,Jinan', 'Porto', 'Roseville, California', 'South Africa', 'Karlsruhe, Germany', 'Santiago, Chile', None, 'Taiwan', '成都', 'Beijing', None, 'London, ON', None, 'Santa Clara, CA', None, None, None, 'Beijing', 'Sunnyvale, California, USA', 'Seattle, WA', 'Texas, United States', None, 'AnHui', 'Bangkok', 'Shenzhen,China', None, 'Bangalore, India', 'Guangzhou', 'Oslo, Norway', None, 'Eindhoven, Netherlands', None, 'New York City, NY', None, 'Leuven, Belgium', 'Canada', 'San Jose, CA', 'San Antonio, TX', 'Darmstadt, Germany', 'Shanghai, China', 'Brno, Czech Republic', 'Gandhinagar, India', 'The 80s', 'Redmond, WA', None, None, 'Hangzhou or Shenzhen', None, None, 'Chicago, IL', 'New Jersey Institute of Technology, Newark, NJ, USA', None, 'Kharagpur', 'New York, NY', 'Switzerland', 'Stanford, CA', None, 'Barcelona', 'San Francisco, CA', 'Singapore', '2003 EBIII, NCSU, Raleigh, NC', 'Waterloo', 'E 117°9′12″，N 36°40′16″', None, 'Birmingham, UK', 'Bremen, Germany', None, 'Philadelphia, PA', 'San Francisco', 'Kharagpur', None, 'Perth, Australia', None, None, None, 'Bhubaneshwar, Odisha, India', 'Bangalore', 'Barcelona, Spain', 'TO THE LEFT OF THE A KEY', None, 'Massachusetts, United States', None, None, 'Buenos Aires, Argentina (FCEyN-UBA)', None, None, 'Seattle, WA', None, 'Osnabrück, Germany', 'UC Berkeley', None, None, 'IIT Roorkee', None, 'Imperial College London', 'Shanghai China', 'Wu Han', None, None, None, None, 'Danang, Vietnam', None, 'Los Angeles, CA', 'Plano, Texas', None, None, None, None, 'Ukraine', 'Austria', None, 'Oxford, UK', None, 'Netherlands', 'Tokyo, Japan', 'Tokyo, Japan', 'Austin, TX', 'France', 'SriCity', 'Earth', 'Philadelphia, PA', 'Beijing, China', 'Chile', 'Germany', 'Boulder, CO', 'Sydney', 'Redmond, WA', 'Karachi, Pakistan', None, None, 'Oslo', None, 'Oslo', 'Chicago, IL', 'Palo Alto, CA', 'Karachi, Pakistan', 'Philadelphia', 'hangzhou', 'Wuhan, China', 'Tübingen', None, 'Nantes (France)', 'Mumbai', 'Boston', 'Birmingham, UK', None, None, 'Netherlands', None, 'United States', None, 'UK', 'USA', None, 'Beijing China', 'Malaysia', None, 'UK', 'Redmond', None, None, 'Tokyo, Japan', None, None, 'Oslo, Norway', None, None, 'Switzerland', None, None, 'Chicago, IL', 'Blacksburg, VA', 'San Francisco', 'Princeton', 'Los Gatos, CA, USA', 'Leganés, Spain', 'Blacksburg, VA', None, None, None, None, 'UK', 'Munich, Germany', 'Georgia Tech', 'Singularity', 'Dalian, Liaoning, China', 'Bengaluru, India', 'Oslo', 'Toulouse, France', None, 'Redmond, WA', 'Bern, Switzerland', 'Chennai', 'New York City', None, None, 'Chennai, India', 'Stuttgart, Germany', None, None, None, 'Cambridge, MA USA', '中国广东广州天河', None, 'Beijing, China', 'San Francisco, CA', 'San Francisco Bay Area', 'Bangkok, Thailand', 'Oslo', None, 'Los Angeles, CA', None, None, None, 'Grand Rapids, MI, USA', None, 'Kenya', None, None, 'Hong Kong', None, 'Germany', 'Cambridge, UK', 'Nizhini Novgorod State University, Russia', 'Athens , Greece', 'Mountain View, CA', 'Mountain View, CA', None, 'Zion, The Matrix', None, 'Canada', 'Athens , Greece', 'Birmingham, UK', 'Montreal', None, 'Gandhinagar', 'Vancouver, Canada', 'Calle de Alan Turing, s/n, 28031 Madrid, Spain', None, 'Denmark', None, 'Amsterdam', None, None, 'Munich, Germany', None, None, 'Leinfelden-Echterdingen', 'Seattle, Washington', 'Charlotte, NC', 'San Francisco, CA', 'France', 'San Fernando City, La Union Philippines', None, 'Leipzig, Germany', None, 'Mumbai,India', 'Shangdong  China', None, 'Alexandria, VA', None, 'Ithaca, NY', 'Houston, Texas', 'Chapel Hill, NC', None, 'Indonesia', 'Planet Earth', 'Bath', None, 'Ulsan, Korea', None, None, 'Vancouver, BC', 'Germany', 'Brussels, Belgium', 'Seoul, Korea', 'Sweden', None, None, 'Denver', 'Madrid', 'Korea, UK', 'San Francisco, CA', 'New York', 'San Francisco', None, 'Paris', 'Berlin, Germany', 'China', 'Hamilton, New Zealand', None, 'United States', None, 'Bristol, UK', 'Washington DC', 'Bay Area, CA', 'Redmond, WA', 'Singapore', 'Amsterdam, The Netherlands', 'San Jose, US', 'Shanghai', 'New York', 'San Francisco, CA', None, 'Yerevan, Armenia', 'Redmond, WA', 'Redmond, USA', 'Washington DC', None, 'Beijing', 'Philadelphia, PA', 'Valencia, Spain', 'Japan, Tsukuba', None, None, 'Shenzhen', None, 'New Jersey Institute of Technology, Newark, NJ, USA', 'Seattle', 'Berlin, Germany', 'Austin, Texas', 'Austin, TX', 'Beijing, China', 'Pohang', 'Czech Republic, Europe', 'New York, NY', None, 'Paris', None, 'Brisbane, Australia', 'New York', 'San Jose, CA', 'Hamilton, ON', 'New York', None, None, 'Narashino, Chiba', None, 'China', None, None, None, 'London', 'Remote', 'Lausanne, Switzerland', 'SFBA', 'New Delhi', 'Oslo', 'Oslo, Norway', 'Boston', None, 'Argentina', None, 'Lugano, Switzerland', 'Los Angeles', 'New York', 'Canada', 'Beijing', None, 'Madison, WI', 'Saudi Arabia', 'Moscow, Russia', 'http://goo.gl/uhzyfC', None, 'Munich, Germany', 'Redmond, WA', 'Tokyo, Japan', None, None, None, 'San Francisco Bay Area', 'Birmingham, UK', 'Menlo Park, California', 'Brazil', 'Rochester, NY', None, 'Shanghai', 'Campinas, Brazil', 'Houston, Texas', None, 'Egypt', 'Santa Monica, CA', 'Australia', None, None, 'New York, NY', 'Birmingham, UK', None, None, 'Armonk, New York, U.S.', 'Planet Earth', 'Granada, Spain', 'Valencia, Spain', 'Moscow', None, 'Birmingham, UK', None, None, 'World Wide Web', 'Amsterdam, Netherlands', 'Atlanta, GA', 'Chicago', None, 'Champaign, IL', None, 'Shanghai,China', 'Yerevan, Armenia', 'Brussels, Belgium', None, None, None, 'Needham, MA', 'Buenos Aires, Argentina', 'Toronto, Canada', 'FInland', 'Dhaka,Bangladesh', None, 'shenzhen', 'India', None, 'Brisbane, Australia', 'tianjin', 'Birmingham, UK', None, None, 'Russian Federation', None, None, 'Hyderabad, India', 'São Paulo', None, 'Germany', 'London, United Kingdom', 'Novosibirsk, Russia', 'Agadir , Morocco', 'Los Angeles, California', 'The Netherlands', None, 'Uppsala, Sweden.', 'Philadelphia, PA', 'Medellin', None, 'Seoul, South Korea', None, None, 'Redmond, WA', 'Bandung, Indonesia', None, None, 'Vienna, Austria', None, 'Birmingham, UK', 'Beijing', None, None, 'Novi Sad, Serbia', 'Stara Zagora, Bulgaria', 'Germany', 'Sacramento, CA', None, 'Nizhini Novgorod State University, Russia', 'San Francisco', 'Hanover, NH', 'Waknaghat, India', None, None, None, 'Washington DC', 'Parrish, FL', 'Perth, Australia', None, 'Bangalore, India', 'Rogers, AR', 'Redmond, WA', None, 'Barcelona, Spain', None, 'Blacksburg', 'Kanpur, India', 'New York', 'UOIT, Oshawa', 'Oslo', None, 'Hong Kong', '哈林区危险区域', 'Beijing, China', 'Lagos, Nigeria.', 'Santiago, Chile', 'Singapore', None, None, ' Lucknow - Bengaluru', 'Durham NC', 'Seattle, WA', None, 'Bangalore', 'Hyderabad, India', 'Paris - France', 'Stuttgart, Germany', 'Toronto, Canada', 'Monterrey, Nuevo León, México', 'HangZhou', 'Oslo, Norway', None, 'Athens, Greece', 'Beijing, China', None, 'Spain', 'Guangzhou, China', 'Seattle, WA', 'College Park', 'Virginia, USA', 'Wuhan,Hubei', None, None, None, 'San Francisco', 'Sydney, Australia', None, 'Birmingham, AL', None, 'Osnabrück, Germany', 'Earth', None, 'Cambridge, MA', None, 'La Paz - Bolivia', None, None, None, None, 'The 80s', None, 'Bangalore, India', 'Ponta Delgada, Portugal', 'Brasil', 'Charlotte, NC', None, 'Palo Alto, CA', None, 'Europe', 'Amsterdam, Netherlands', 'Philadelphia, PA, USA', None, None, None, None, 'Santa Barbara, CA', None, 'Toronto, Canada', 'Zurich, Switzerland', 'Foo York', 'Kuala lumpur', 'San Francisco, CA', 'Jerusalem', 'WUHAN,China', 'New York, NY, USA', 'Massa, MS, Italy', 'Philadelphia, PA', 'Chicago, IL', 'Spain', None, 'Bangladesh', 'Irvine, US', 'Campinas, Brazil', None, None, 'Shanghai', 'United States', 'Philadelphia, PA', 'Tokyo, Japan', 'Granada, Spain', None, 'Jalandhar , Punjab', 'London, UK', 'London, UK', None, None, 'Earth', 'Birmingham, UK', 'India', None, None, 'Lawrence, Kansas', 'France', 'Philadelphia', None, None, 'Bainbridge Island, WA, U.S.A', 'Italy', 'Dělnická 43, Praha 7', 'Los Angeles, CA, USA', 'Palo Alto, CA', None, 'Munich, Germany', 'moscow', 'San Jose, CA', 'College Park', 'Barcelona, Spain', 'San Francisco', 'Provo, UT', 'Hyderabad, India', None, None, None, 'Tainan City, Taiwan', None, None, 'Mumbai, India', 'Chapel Hill, NC', 'Washington DC', 'Armonk, New York, U.S.', None, 'San Francisco, CA', None, None, None, 'Yorkshire, UK', None, None, None, 'San Francisco Bay Area', None, 'Paris', 'Vladivostok, Russia', 'Italy', 'West Lafayette', 'Beijing, China', 'Boston', 'Seattle, WA', 'Berlin, Germany', 'Switzerland', None, 'Toronto, Canada', 'Mountain View, CA', 'NYC, baby!', 'Jakarta', 'Cambridge, MA', None, 'Zurich, Switzerland', 'Shanghai', 'Oxford, United Kingdom', 'Wet coast, Canada', 'Salvador, Bahia. Brazil.', 'Warsaw, Poland', 'Orange County, Ca. ', 'Shanghai, China', 'Shanghai', 'shenzhen SZU CS ', 'MIT', 'Birmingham, UK', None, 'Cali, Colombia', None, 'Chicago, IL', 'Seattle, WA', 'Zürich, Switzerland.', None, 'London', None, 'Belgrade', None, 'Seattle, WA', 'Philippines', 'New York', 'Taiwan', 'Australia', 'Anywhere', 'Los Angeles', 'Edinburgh', 'Münster, Germany', 'Seattle, WA', None, None, 'Wuhan, China', 'Redmond, WA', 'Hangzhou', 'Gdańsk University of Technology', None, 'Paris (France)', 'Berkeley', None, 'Saarbrücken, Germany', None, 'Tucson, Arizona', 'Gainesville, FL', None, 'Belgrade', None, None, 'Redmond, WA', 'Palo Alto, CA', 'NYC', 'Raleigh, NC', 'Hong Kong', None, None, 'Jaipur, Rajasthan , INDIA', 'Charlotte, NC', 'Spain', 'Santiago - Chile', 'Taiwan', 'London, UK', 'Hamburg', 'Bhubhaneswar, India', 'Lexington, Virginia, USA', None, None, 'Corvallis High School, Corvallis OR', 'Hong Kong, Beijing', None, None, None, 'Enschede', 'USA', 'bayCA', 'Cambridge, MA', 'World', 'Cuiabá, MT', 'Boston, MA', 'Boston, MA', 'Washington, USA', None, None, None, 'Stony Brook, NY', None, 'Basque Country, Spain', None, None, 'Redmond, WA']

loc_3Code = ['SLV', 'AUT', 'NLD', 'DEU', 'JPN', 'USA', 'USA', 'USA', 'SWE', 'USA', 'CHN', 'USA', 'USA', 'TUR', 'POL', 'ESP', 'NGA', 'USA', 'USA', 'USA', 'DEU', 'USA', 'AUT', 'GBR', 'USA', 'USA', 'CHN', 'UMI', 'BRA', 'USA', 'SWE', 'USA', 'IOT', 'JPN', 'DEU', 'AUT', 'CHN', 'USA', 'USA', 'USA', 'IOT', 'USA', 'LKA', 'VIR', 'CHN', 'CHN', 'USA', 'JPN', 'JPN', 'USA', 'AUS', 'UMI', 'USA', 'CHN', 'USA', 'USA', 'FRA', 'GBR', 'USA', 'NGA', 'CHN', 'USA', 'USA', 'USA', 'USA', 'USA', 'JPN', 'CHN', 'USA', 'USA', 'GBR', 'CHN', 'GBR', 'AUT', 'USA', 'RUS', 'GBR', 'ISL', 'CAN', 'GBR', 'USA', 'DEU', 'USA', 'IOT', 'GBR', 'JPN', 'GBR', 'USA', 'USA', 'CHN', 'GBR', 'USA', 'GBR', 'NLD', 'HRV', 'USA', 'ZAF', 'DEU', 'CHL', 'TWN', 'BOL', 'USA', 'USA', 'USA', 'UMI', 'CHN', 'IOT', 'NOR', 'NLD', 'DEU', 'BEL', 'CAN', 'USA', 'DEU', 'CHN', 'CZE', 'IOT', 'USA', 'AIA', 'USA', 'DEU', 'CHE', 'USA', 'USA', 'SGP', 'FRA', 'GBR', 'DEU', 'JPN', 'AUS', 'IOT', 'ESP', 'UMI', 'USA', 'DEU', 'VNM', 'USA', 'AUT', 'GBR', 'NLD', 'JPN', 'JPN', 'FRA', 'JPN', 'CHN', 'CHL', 'DEU', 'CCK', 'USA', 'PAK', 'AIA', 'USA', 'PAK', 'CHN', 'GBR', 'NLD', 'UMI', 'GBR', 'USA', 'MYS', 'GBR', 'JPN', 'NOR', 'CHE', 'AIA', 'SLV', 'USA', 'ESP', 'SLV', 'GBR', 'DEU', 'CHN', 'IOT', 'FRA', 'USA', 'CHE', 'IOT', 'DEU', 'CHN', 'USA', 'THA', 'USA', 'USA', 'KEN', 'HKG', 'DEU', 'GBR', 'RUS', 'GRC', 'USA', 'USA', 'CAN', 'GRC', 'GBR', 'ESP', 'DNK', 'NLD', 'DEU', 'FRA', 'USA', 'FRA', 'DEU', 'IOT', 'SLV', 'DEU', 'FRA', 'IDN', 'PRK', 'DEU', 'BEL', 'PRK', 'SWE', 'GBR', 'USA', 'DEU', 'CHN', 'NZL', 'UMI', 'GBR', 'USA', 'USA', 'SGP', 'AUS', 'USA', 'ARM', 'USA', 'USA', 'JPN', 'ESP', 'USA', 'DEU', 'CHN', 'DEU', 'AUS', 'USA', 'BOL', 'CHN', 'CHE', 'NOR', 'ARG', 'CHE', 'CAN', 'MWI', 'SAU', 'RUS', 'DEU', 'USA', 'JPN', 'GBR', 'USA', 'BRA', 'DEU', 'BRA', 'EGY', 'USA', 'AUS', 'DEU', 'GBR', 'VIR', 'ESP', 'ESP', 'GBR', 'NLD', 'USA', 'AIA', 'CHN', 'ARM', 'BEL', 'USA', 'ARG', 'FIN', 'BGD', 'IOT', 'AUS', 'GBR', 'RUS', 'IOT', 'DEU', 'GBR', 'RUS', 'MAR', 'USA', 'JPN', 'USA', 'IDN', 'AUT', 'GBR', 'SRB', 'BGR', 'DEU', 'USA', 'RUS', 'SHN', 'IOT', 'AUS', 'IOT', 'ATA', 'USA', 'ESP', 'IOT', 'HKG', 'CHN', 'CHL', 'SGP', 'USA', 'IOT', 'DEU', 'MEX', 'NOR', 'GRC', 'CHN', 'ESP', 'CHN', 'USA', 'USA', 'AUS', 'ALA', 'DEU', 'USA', 'IOT', 'PRT', 'BRA', 'FRA', 'USA', 'NLD', 'USA', 'USA', 'CHE', 'USA', 'CHN', 'USA', 'ITA', 'JPN', 'AIA', 'ESP', 'BGD', 'AUS', 'BRA', 'UMI', 'JPN', 'JPN', 'ESP', 'GBR', 'GBR', 'GBR', 'IOT', 'FRA', 'ITA', 'USA', 'USA', 'DEU', 'USA', 'ESP', 'BTN', 'IOT', 'TWN', 'IOT', 'FRA', 'VIR', 'USA', 'GBR', 'RUS', 'ITA', 'CHN', 'USA', 'DEU', 'CHE', 'USA', 'USA', 'CHE', 'GBR', 'POL', 'CHN', 'JOR', 'GBR', 'COL', 'AIA', 'USA', 'USA', 'PHL', 'TWN', 'AUS', 'DEU', 'USA', 'CHN', 'USA', 'DEU', 'USA', 'USA', 'FRA', 'HKG', 'IOT', 'FRA', 'ESP', 'TWN', 'GBR', 'IOT', 'USA', 'USA', 'AZE', 'USA', 'MLT', 'USA', 'USA', 'USA', 'DEU', 'ESP', 'USA']

def adhocs(country_str):
    result = country_str.lower()

    if "http" in result: # who puts that !
        return None
    if len(result.split(" ")) > 3: # funny stuff instead of actual location
        return None

    result = result.replace("uk", "United Kingdom")
    result = result.replace("amsterdam", "Netherland")
    result = result.replace("california", "USA")
    # TODO: States to USA
    result = result.replace(" ca", "USA")
    result = result.replace(" ga", "USA")
    result = result.replace(" wa", "USA")
    result = result.replace(" ma", "USA")

    result = result.strip()
    result = result.replace(" ","%20")

    return result

"""
#---GET SEARCH KEYWORDS------------------------------------------------------------
search_pat="machine vision"

root=Tk()
def retrieve_input():
    global search_pat
    inputValue=textBox.get("1.0","end-1c")
    root.destroy()
    search_pat = inputValue

textBox=Text(root, height=2, width=10)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Commit", 
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

root.mainloop()


#---GET REPO AND THEN USER LOCATOIN-----------------------------------------------------
if search_pat=="":
    print("Nothing to search!")
    sys.exit()

git_user = json.load(open("../github_cred.json"))
user=git_user["user"]
passw=git_user["pass"]

repo_api="https://api.github.com/search/repositories?q="+search_pat.replace(" ","+")+"&per_page=1"
response = requests.get(repo_api, auth=HTTPBasicAuth(user, passw))
json_data = json.loads(response.text)

# Decide how many results we can get
result_cnt = json_data["total_count"]
perpage=100
page_cnt = round(result_cnt/perpage)
# github limit to show 1000 only !
if page_cnt*perpage > 1000:
    page_cnt = round(1000/perpage) #10 pages w/ 100 per_page

locs=[]
for page in range(1,page_cnt+1):
    print("Page "+ str(page))
    repo_api="https://api.github.com/search/repositories?q="+search_pat.replace(" ","+")+"&page="+str(page)+"&per_page="+str(perpage)
    json_data = requests.get(repo_api, auth=HTTPBasicAuth(user, passw)).json()
    #json_data = json.loads(response.text)

    for item in json_data["items"]:
        user_api= item["owner"]["url"]
        user_data = requests.get(user_api, auth=HTTPBasicAuth(user, passw)).json()
        #user_data = json.loads(response.text)
        if "location" in user_data.keys():
            locs.append(user_data["location"])

#print(locs)

#---CONVERT TO COUNTRY CODE------------------------------------------------------------
not_found=0.0
loc_3Code=[]

for id,loc in enumerate(locs):
    if loc is None:
        continue
    if loc == "None":
        continue
    #country is the last item
    loc1 = loc.split(",")[-1]
    loc1 = adhocs(loc1)

    if loc1 is None:
        continue

    # get country code
    country_api="https://restcountries.eu/rest/v2/name/"+loc1
    country_data = requests.get(country_api).json()
    #country_data = json.loads(response.text)
    
    #if found and returned a list - choose the first item
    if isinstance(country_data, list): 
        if "alpha3Code" in country_data[0].keys():
            loc_3Code.append(country_data[0]["alpha3Code"])
    else:
        not_found = not_found +1

"""
print(loc_3Code)
print(str(len(locs))+" #Data Collected! "+str(len(loc_3Code))+" #Data Plotting!"+" Not founds="+str( float(100* not_found)/float(len(locs)))+"%")
#---COUNT--------------------------------------------------------------------------------
loc_3Code_dic = {i:loc_3Code.count(i) for i in loc_3Code}

keys=[]
vals=[]
for key,val in loc_3Code_dic.items():
    keys.append(key)
    vals.append(val)
#---PLOT--------------------------------------------------------------------------------
_loc="iso_alpha"
_pop="Population"
fig = px.scatter_geo(pd.DataFrame.from_dict({_loc:keys, _pop:vals}), locations=_loc, size=_pop,
                     #color="continent", #hover_name="country",
                     projection="natural earth")
pio.renderers.default = 'browser'
#pio.show(fig)
pio.write_html(fig, file='index.html', auto_open=True)

