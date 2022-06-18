from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os
from urllib.parse import urljoin


# tif files results into a programme system error
def StartSearch():
    search = input("Search for\n")
    params = {"q": search,'ia':'images'}
    dir_name = search.replace(" ", "_").lower()

    headers = {"User-agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/60.0.3112.90 Safari/537.36'}


    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    r = requests.get("https://www.bing.com/images/search",params= params)
    soup = BeautifulSoup(r.text, "html.parser")
    p = open("./test_results1.html","w+",encoding='utf-8')
    p.write(str(soup))
    p.close()
    links = soup.findAll("a", {"class": "iusc"})

    print("Image results:", len(links))


    for item in links:
        try:
            link = item.attrs["href"]
            img_obj = requests.get(urljoin('https://www.bing.com/',link))
            print("Getting", link)
            title = item.attrs["href"].split("/")[-1]
            print("tittle:",title)
            img = Image.open(BytesIO(img_obj.content))
            try:
                img.save("./" + dir_name + "/" + title, img.format)
                print("saved")
            except:
                print("Bad naming of - " + title)
                better_name = title.split('?')[0]
                try:
                    img.save("./" + dir_name + "/" + better_name, img.format)
                    print("saved")
                except:
                    print("Could not save image.(format unrecognised or .tif file)")

        except:
            try:
                link = item.attrs["href"]
                img_obj = requests.get(urljoin('https://www.bing.com',link),headers= headers)
                #print("Getting", item.attrs["href"])
                title = item.attrs["href"].split("/")[-1]
                #print("tittle:", title)

                try:
                    img = Image.open(BytesIO(img_obj.content))
                    img.save('./'+ dir_name + '/'+title ,img.format)
                    print("saved")
                except:
                    print("Bad naming:",title)
                    betterName = title.split('?')[0]
                    try:
                        img.save("./" + dir_name + "/" + betterName, img.format)
                        print("Title - ",betterName)
                        print("Exemption2")
                    except:
                        print("Image format unrecognised.(or .tif file)")
            except requests.exceptions.SSLError:
                print("Getting", item.attrs["href"])
                print("Site not secure")
            except requests.exceptions.ConnectionError:
                print("Target machine actively denied connection")




    StartSearch()


StartSearch()
# Issues
# The programcannot save tif files..It resuls in a type error and a systemerror where the .tif encoder returns an error set.