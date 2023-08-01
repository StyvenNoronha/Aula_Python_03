from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep



ROOT_FOLDER = Path(__file__).parent
CHROMESRIVER_EXEC = ROOT_FOLDER / 'drive' / 'chromedriver.exe'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  

    chrome_service = Service(
        executable_path=CHROMESRIVER_EXEC,
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10
# Example
# options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

# Como antes
    browser.get('https://www.google.com')


# Espere para encontrar o input
    procura = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.NAME, 'q'))
    )
    procura.send_keys('styven noronha')
    procura.send_keys(Keys.ENTER)

    resultado = browser.find_element(By.ID,'search')
    LINKS = resultado.find_elements(By.TAG_NAME, 'a')
    LINKS[1].click()  



    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)
