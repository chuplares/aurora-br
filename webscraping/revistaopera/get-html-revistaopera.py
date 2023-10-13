from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)


# Navigate to the target URL
driver.get('https://revistaopera.com.br/?s')
final_html = driver.page_source
with open('final_page_revistaopera_page_first.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

i = 2
for i in range(2, 208):

    driver.get('https://revistaopera.com.br/page/' + str(i) + '/?s')

    # Save the final HTML content to a file
    final_html = driver.page_source
    with open('final_page_revistaopera_page_' + str(i) + '.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Saved page " + str(i))
    # Close the browser
    i = i + 1
driver.quit()
