from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FIREFOX_BINARY = FirefoxBinary('/usr/bin/firefox')

PROFILE = webdriver.FirefoxProfile()
PROFILE.set_preference("browser.cache.disk.enable", False)
PROFILE.set_preference("browser.cache.memory.enable", False)
PROFILE.set_preference("browser.cache.offline.enable", False)
PROFILE.set_preference("network.http.use-cache", False)
PROFILE.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0")

FIREFOX_OPTS = Options()
FIREFOX_OPTS.headless = True
ff_opt = {
    'firefox_binary':FIREFOX_BINARY,
    'firefox_profile':PROFILE,
    'options':FIREFOX_OPTS,
    'executable_path':'/usr/bin/geckodriver'
}
    
driver = webdriver.Firefox(**ff_opt)

driver.get("https://www.linkedin.com/")

element = driver.find_element(By.CSS_SELECTOR, "input[autocomplete='username']")
usuario = 'a34299720@gmail.com'
element.send_keys(usuario)

element = driver.find_element(By.CSS_SELECTOR, "input[autocomplete='current-password']")
contrasenia = 'aaaaeeee'
element.send_keys(contrasenia)

element = driver.find_element(By.CSS_SELECTOR, "button[class='sign-in-form__submit-button']")
element.click()

url='https://www.linkedin.com/in/joaquin-aragon-4661841ab/'
driver.get(url)
element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"img[class='pv-top-card-profile-picture__image pv-top-card-profile-picture__image--show ember-view']"))
    )
print(element.get_attribute("src"))
