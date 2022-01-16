from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from persona import Persona

def getPersona(name):
	FIREFOX_BINARY = FirefoxBinary('/opt/firefox/firefox')

	PROFILE = webdriver.FirefoxProfile()
	PROFILE.set_preference("browser.cache.disk.enable", False)
	PROFILE.set_preference("browser.cache.memory.enable", False)
	PROFILE.set_preference("browser.cache.offline.enable", False)
	PROFILE.set_preference("network.http.use-cache", False)
	PROFILE.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0")

	FIREFOX_OPTS = Options()
	FIREFOX_OPTS.headless = True
	GECKODRIVER_LOG = '/geckodriver.log'
	ff_opt = {
			'firefox_binary':FIREFOX_BINARY,
			'firefox_profile':PROFILE,
			'options':FIREFOX_OPTS,
			'service_log_path':GECKODRIVER_LOG
	}
	    
	driver = webdriver.Firefox(**ff_opt)

	driver.get("https://facebook.com")
	element = driver.find_element(By.ID, "email")
	element.send_keys("chris12q_d965m@xeoty.com")
	element = driver.find_element(By.ID, "pass")
	element.send_keys("XfpwX6DPMQJZzSd")
	element = driver.find_element(By.NAME, "login")
	element.click()
	try:
	    search = "https://www.facebook.com/search/top/?q="
	    nombre = name
	    nombre = nombre.replace(" ","%20")
	    driver.get(search+nombre)
	    element = WebDriverWait(driver,10).until(
		EC.presence_of_element_located((By.CSS_SELECTOR,"div[role = 'article']"))
	    )
	    
	    results = element.find_elements_by_css_selector("div[role = 'article']")
	    results.pop(len(results)-1)
	    links = []
	    nombres = []
	    for result in results:
		data = result.find_element(By.CSS_SELECTOR,"a[role = 'link']")
		links.append(data.get_attribute("href"))
		nombres.append(data.text)

	    # for link in links:
	    link=links[0]
	    persona = Persona()
	    persona.nombre = nombres[0]
	    persona.add_link = links[0]
	    print(link)
	    if(link.startswith("https://www.facebook.com/profile.php")):
		link += "&sk=about"
	    else:
		link += "/about"

	    detalles = ["_work_and_education","_places","_contact_and_basic_info","_family_and_relationships"]
	    for index_detalle, detalle in enumerate(detalles):
		driver.get(link + detalle)
		contenedor = WebDriverWait(driver,10).until(
		                EC.presence_of_element_located((By.CSS_SELECTOR,"div[class = 'buofh1pr']"))
		            )
		secciones = contenedor.find_elements_by_css_selector("div[class='tu1s4ah4']")
		secciones.append(contenedor.find_element_by_css_selector("div[class='']"))

		for index_seccion, seccion in enumerate(secciones):
		    elementos = seccion.find_elements_by_css_selector("a[role='link']")
		    data = []
		    for e in elementos:
		        if(e.text.startswith("No")):
		            pass
		        else:
		            data.append(e.text)
		    if(len(data) == 0):
		        elementos = seccion.find_elements_by_css_selector("span[dir='auto']")
		        elementos.pop(0)
		        for e in elementos:
		            if(e.text.startswith("No")):
		                pass
		            else:
		                s = e.text.split()[2:]
		                data.append(' '.join([str(x) for x in s]))

		    for e in data:
		        if(index_detalle == 0):
		            if(index_seccion == 0):
		                persona.add_trabajo(e)
		            elif(index_seccion == 1):
		                persona.add_universidad(e)
		            elif(index_seccion == 2):
		                persona.add_colegio(e)
		        elif(index_detalle == 1):
		            if(index_seccion == 0):
		                persona.add_ubicacion(e)
		        elif(index_detalle == 2):
		            if(index_seccion == 0):
		                persona.add_contacto(e)
		            elif(index_seccion == 1):
		                persona.add_link(e)
		        elif(index_detalle == 3):
		            if(index_seccion == 0):
		                persona.add_relacion(e)
		            elif(index_seccion == 1):
		                persona.add_familiar(e)
		    
	    print(persona.toJSON())
	except:
	    print("XD")
