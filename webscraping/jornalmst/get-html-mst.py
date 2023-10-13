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
i = 1
for i in range(1, 65):

    driver.get('https://mst.org.br/conteudo/noticias/page/' + str(i) + '/')

    # Save the final HTML content to a file
    final_html = driver.page_source
    with open('final_page_mst_page_' + str(i) + '.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Saved page " + str(i))
    # Close the browser
    i = i + 1
driver.quit()
