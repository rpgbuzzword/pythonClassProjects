import requests
import bs4

billboard_url="https://www.billboard.com/charts/hot-100/"
billboard_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}
class BillboardScraper:
    def __init__(self):
        self.date = ""
        self.billboardArtists = []
        self.billboardSongs = []


    def get_Date(self):
        date = input("What date are we time travelling to? Type your answer in the format YYYY-MM-DD:")
        self.date = date

    def timeTravel(self, date):
        response = requests.get(url=f"{billboard_url}{date}", headers=billboard_headers)

        soup = bs4.BeautifulSoup(response.text, "html.parser")
        song_titles = []
        
        #We append the first title on its own line, because the #1 song has a unique CSS class
        song_titles.append(soup.find(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet").getText().strip())
        
        for item in soup.findAll(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"):
            song_titles.append(item.getText().strip())

        song_artists = []
        #Same here, append the #1 song artist independently since it uses a unique CSS class
        song_artists.append(soup.find(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet").getText().strip())

        for item in soup.findAll(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"):
            song_artists.append(item.getText().strip())

        self.billboardArtists = song_artists
        self.billboardSongs = song_titles