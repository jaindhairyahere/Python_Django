import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',	'RESTapi.settings')

import django
django.setup()


if __name__ == "__main__":

    from bs4 import BeautifulSoup
    import requests
    import numpy as np 
    import pandas as pd
    from bs4 import BeautifulSoup
    import requests
    import sqlite3
    import sqlite3 as db
    from quantify_capital_assignment.models import Movie

    url1 = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc"
    url2 = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt"
    url3 = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=101&ref_=adv_nxt"
    url4 = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=151&ref_=adv_nxt"
    url5 = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=201&ref_=adv_nxt"
    urls = [url1, url2, url3, url4, url5]

    title = []
    rating = []
    release_date = []
    description = []
    duration = []

    for url in urls:
        response = requests.get(url)

        soup = BeautifulSoup(response.text, features='html.parser')
        name_release_class = soup.find_all('h3', {'class': 'lister-item-header'})
        rating_class = soup.find_all('div',{'class':'ratings-bar'})
        desc_class = soup.find_all('p', {'class': 'text-muted'})
        time_class = soup.find_all('span',{'class':'runtime'})

        for name_release_objects in name_release_class:
            for name in name_release_objects.find_all('a'):
                title.append(name.text)
            for release in name_release_objects.find_all('span',{'class':'lister-item-year text-muted unbold'}):
                release_date.append(release.text)
        for rating_object in rating_class:
            for rate in rating_object.find_all('strong'):
                rating.append(rate.text)
        for desc in desc_class:
            desc_text = desc.text.lstrip()
            description.append(desc_text)
        for time in time_class:
            duration.append(time.text)

    title = np.array(title)
    rating = np.array(rating)
    release_date = np.array(release_date)
    description = np.array(description[1::2])
    
    # allMovies = list(zip(title, rating, release_date, description, duration))
    # for MovieObject in allMovies:
    #     Movie.objects.get_or_create(title=MovieObject[0], rating=MovieObject[1], release_date=MovieObject[2],description=MovieObject[3], duration=MovieObject[4])
    # print(pd.DataFrame(allMovies))
   
    print(len(rating))
    my_db = pd.DataFrame()
    my_db['title']= title
    my_db['rating']= 8 * len(rating)
    my_db['rating']= rating
    my_db['release_date']= release_date
    my_db['duration'] = duration
    my_db['description']=description
    my_db['id']=[i for i in range(1,251)]
    conn = db.connect('db.sqlite3')
    c = conn.cursor()
    conn.commit()
    my_db.to_sql('quantify_capital_assignment_movie',conn,if_exists='replace',index=False)
    conn.commit()        
    conn.close()    
    print("Successfully Populated the Model")
