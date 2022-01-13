# InstagramScraper
That software is designed to extract the latest most viral posts from different locations in order to obtain quantitative data for analysis and to use in marketing plans.
Despite being designed to obtain data from hotels and analyze the competition as well as potential triggers of giveaway chains on Instagram, it can be used in any other sector.

PRE REQUIREMENTS:
- Install "Google Chrome" since it is the browser used in the software.
- Download "Chromedriver": https://chromedriver.chromium.org/downloads

PACKAGES:
- selenium
- pathlib
- WriteExcel
- datetime
- xlswriter
- time
- os

INSTRUCTIONS FOR USE:
- Save chromedriver in the software folder.

- Enter a username and password in the "ACCOUNT.txt" file (It is recommended to use an account exclusively created for this software).

- Enter the locations to scrape in the "LOCATIONS.txt" file, to do this, search for the locations on instagram from the web browser and copy their link (example of two locations in the file).

<img width="1728" alt="Captura de pantalla 2022-01-13 a las 14 40 50" src="https://user-images.githubusercontent.com/90764257/149351583-1c6f9221-cb29-437e-abf9-18d358f79053.png">
<img width="1728" alt="Captura de pantalla 2022-01-13 a las 14 41 28" src="https://user-images.githubusercontent.com/90764257/149351613-aae2e246-6299-43fd-b4f7-9f4bfef673d9.png">


- Run "Main.py".

OUTPUT:
Excel document with columns: "user", "likes of the viralized publication", "followers" and "followed"
