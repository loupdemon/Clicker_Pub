from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def click_adsense_ads(driver):
    try:
        wait = WebDriverWait(driver, 20)
        adsense_ads = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ads-fr")))
        if adsense_ads:
            random_ad = random.choice(adsense_ads)
            random_ad.click()
            time.sleep(8)  # Attendre pendant 8 secondes sur la page de l'annonce
    except TimeoutException:
        print("Les annonces AdSense n'ont pas été trouvées.")

# Initialize le navigateur Chrome en mode incognito
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

# Ouvre Google en mode incognito
driver.get("https://www.google.com")

# Accepte les conditions de Google en cliquant sur le bouton "J'accepte" s'il est présent
try:
    accept_button = driver.find_element(By.ID, "L2AGLb")
    accept_button.click()
except:
    pass

# Effectue la recherche sur Google
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("elmesmar")
search_box.send_keys(Keys.RETURN)

# Attends que les résultats se chargent
time.sleep(2)

# Clique sur le premier résultat
results = driver.find_elements(By.CSS_SELECTOR, "div.g")
if results:
    first_result = results[0]
    link = first_result.find_element(By.CSS_SELECTOR, "a")

    # Scroll down to make the link visible
    driver.execute_script("arguments[0].scrollIntoView();", link)
    driver.execute_script("window.scrollBy(0, -150)")  # Scrolling a bit up
    time.sleep(1)
    link.click()

# Attends 7 secondes pour le chargement complet de la page
time.sleep(7)

# Clique sur le bouton avec l'ID "cookieChoiceDismiss" s'il est présent
cookie_dismiss_button = driver.find_element(By.ID, "cookieChoiceDismiss")
if cookie_dismiss_button:
    cookie_dismiss_button.click()

# Define the text of the button you want to find
target_texts = ["Ouvrir", "Acheter", "Votre texte spécifique"]
found_target = False

# Vitesse de défilement souhaitée
scroll_speed = 40

# Nombre total de pixels à faire défiler
scroll_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")

# Code pour rechercher les éléments de texte spécifiques pendant le défilement
for i in range(0, scroll_height, scroll_speed):
    if found_target:
        break  # Arrêtez de défiler si une cible a été trouvée

    driver.execute_script(f"window.scrollTo(0, {i});")
    time.sleep(0.1)  # Ralentir la vitesse de défilement pour voir tout le contenu

    page_source = driver.page_source

    for text in target_texts:
        if text in page_source:
            # Marquez que nous avons trouvé une cible
            found_target = True

            # Vous pouvez effectuer des actions supplémentaires sur l'élément ici
            print(f"Texte cible trouvé : {text}")

# Clique sur les annonces AdSense
click_adsense_ads(driver)

# Reste du code pour vérifier et cliquer sur les éléments AdSense

# Wait for 8 seconds on the opened page
time.sleep(8)

# Simulate further navigation on the page by waiting for some seconds
time.sleep(10)

# Close the browser
driver.quit()

