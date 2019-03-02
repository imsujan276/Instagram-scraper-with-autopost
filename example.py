import time
import instagram_scraper as insta
import json
from subprocess import call

insta_profiles = ['billgates', 'elonmusk']
number_last_photos = 3

def scraper():
 #call('instagram-scraper ' + insta_profiles + ' -m ' + number_last_photos + ' -u 0 -p 0 -t none --media-metadata', shell=True)
    imgScraper = insta.InstagramScraper(usernames=[insta_profiles[x]], login_user="yourusername", login_pass="yourpassword", maximum=number_last_photos, media_metadata=True, latest=True,media_types=['image'])
    imgScraper.scrape()
    # Take last json image data and post in instagram images,  tags and decription
    with open(insta_profiles[x] + '/' + insta_profiles[x] + '.json', 'r') as j:
        json_data = json.load(j)
        newstr = (json_data[0]["display_url"])
        imgUrl = newstr.split('?')[0].split('/')[-1]
        imgTags = (json_data[0]["tags"])
       # imgDescription = (json_data[0]["description"])
        #Execute Instagram users with instapy. Excecute list insta_profiles
        call('instapy -u yourusername -p yourpassword -f ./' + insta_profiles[x] + '/' + imgUrl +' -t "#model #models #Modeling #modelo #modellife #modelling #modelagency #Modelos #modelphotography #modelsearch #ModelStatus #modelingagency #modelfitness #ModelsWanted #modelshoot #modella #modelmanagement #modelscout #modeltest #modelindonesia #modele #modelife #modelmayhem #modelgirl #modell #modelslife #modelkids #modelcall #modelpose #ModelBehavior"', shell=True)
        time.sleep(5)
        # Account number 2
        call('instapy -u yourusername -p yourpassword -f ./' + insta_profiles[x] + '/' + imgUrl +' -t "#model #models #Modeling #modelo #modellife #modelling #modelagency #Modelos #modelphotography #modelsearch #ModelStatus #modelingagency #modelfitness #ModelsWanted #modelshoot #modella #modelmanagement #modelscout #modeltest #modelindonesia #modele #modelife #modelmayhem #modelgirl #modell #modelslife #modelkids #modelcall #modelpose #ModelBehavior"', shell=True)
        print(imgUrl)

    print ("scraped " + str(number_last_photos) + " from " + insta_profiles[x])
def main():
    scraper()

for x in range(len(insta_profiles)):
    main()
    time.sleep(1000)

