import selenium
from selenium import webdriver

#function that opens up a web browser with three urls
def open_browser():
    url = 'https://www.youtube.com/results?search_query=the+walking+dead+negan+scenes+2'
    url2 = 'https://www.youtube.com/@metallica/videos'
    url3 = 'https://stackoverflow.com/questions/59601378/open-tabs-using-python-script'

    # while true loop to open and close the web browser
    while True:
        driver = webdriver.Edge()

        driver.get(url)
        driver.get(url2)
        driver.get(url3)

        driver.close()

#calling the open_browser() function
open_browser()
