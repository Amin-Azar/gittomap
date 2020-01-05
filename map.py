import json
import plotly.express as px
import plotly.io as pio
import pandas as pd
import requests
from tkinter import *

#locs=["San Francisco, CA","Grenoble, France - Lavras, Brazil - São Carlos, Brazil","Brisbane, Australia","Bengaluru, India","Saarland University","Oslo, Norway","Los Angeles, California","Amsterdam","Birmingham, UK","None","None","None","Taiwan","None","2003 EBIII, NCSU, Raleigh, NC","None","None","France","Tokyo, Japan","Virginia, USA","Chennai","Stuttgart, Germany","Tokyo, Japan","Beijing, China","None","Cambridge, UK","Korea, UK","None","France","Bath"]

def adhocs(country_str):
    result = country_str.lower()
    result = result.replace("uk", "United Kingdom")
    result = result.replace("amsterdam", "Netherland")
    result = result.replace("california", "USA")
    result = result.replace(" ca", "USA")

    result = result.strip()
    result = result.replace(" ","%20")
    return result

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
repo_api="https://api.github.com/search/repositories?q="+search_pat.replace(" ","+")+"&per_page=100"
response = requests.get(repo_api)
json_data = json.loads(response.text)

locs=[]
for item in json_data["items"]:
    user_api= item["owner"]["url"]
    response = requests.get(user_api)
    user_data = json.loads(response.text)
    locs.append(user_data["location"])
#---CONVERT TO COUNTRY CODE------------------------------------------------------------
not_found=0.0
loc_3Code=[]

for loc in locs:
    if loc is None:
        continue
    if loc == "None":
        continue
    #country is the last item
    loc1 = loc.split(",")[-1]
    loc1 = adhocs(loc1)

    # get country code
    country_api="https://restcountries.eu/rest/v2/name/"+loc1
    response = requests.get(country_api)
    country_data = json.loads(response.text)
    
    #if found and returned a list - choose the first item
    if isinstance(country_data, list): 
        if "alpha3Code" in country_data[0].keys():
            loc_3Code.append(country_data[0]["alpha3Code"])
    else:
        not_found = not_found +1

print(locs)
print(loc_3Code)
print(str(len(locs))+" #Data Collected! "+str(len(locs))+" #Data Plotting!"+" Not founds="+str( float(100* not_found)/float(len(locs)))+"%")
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
pio.show(fig)


