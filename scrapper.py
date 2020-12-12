import time
import sys
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def getTop50 (mapUrl: str) :
    driver = webdriver.Chrome("C:\\Work\\Python\\webscraping\\lib\\chromedriver_87.0.4280.88.exe")

    driver.get(mapUrl)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    bestPlayer = soup.find('tr', class_='beatmap-scoreboard-table__body-row beatmap-scoreboard-table__body-row--highlightable beatmap-scoreboard-table__body-row--first')

    while (bestPlayer == None):
        # Sleep for 0.5 seconds and try parsing the updated html again
        time.sleep(0.5)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        bestPlayer = soup.find('tr', class_='beatmap-scoreboard-table__body-row beatmap-scoreboard-table__body-row--highlightable beatmap-scoreboard-table__body-row--first')

    score = bestPlayer.findAll('a')
    print(score[0].contents[0], score[2].contents[0], score[3].contents[0], score[5].contents[0])

    topPlayerList = soup.findAll('tr', class_='beatmap-scoreboard-table__body-row beatmap-scoreboard-table__body-row--highlightable')

    for topPlayer in topPlayerList:
        score = topPlayer.findAll('a')
        print(score[0].contents[0], score[2].contents[0], score[3].contents[0], score[5].contents[0])

    driver.close()

if __name__ == "__main__" :
    getTop50("https://osu.ppy.sh/beatmapsets/320118#osu/714001")