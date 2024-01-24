from shutil import copyfile, rmtree
from os import path
from webdriver_manager.chrome import ChromeDriverManager

base_dir = path.dirname(__file__) + "\\"
driver_path = ChromeDriverManager().install()
copyfile(driver_path, base_dir + "chromedriver.exe")
rmtree(path.expanduser('~')+"/.wdm")
