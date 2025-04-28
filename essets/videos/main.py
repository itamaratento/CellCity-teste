from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Inicialize o ChromeDriver automaticamente usando o WebDriver Manager
driver = webdriver.Chrome(ChromeDriverManager().install())

# A partir daqui, o restante do código segue normalmente
driver.get('https://www.google.com')

# Aguardar o carregamento da página
input("Pressione Enter para fechar o navegador...")

# Fechar o navegador
driver.quit()
