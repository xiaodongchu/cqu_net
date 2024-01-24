from shutil import copyfile, rmtree
from os import path
from webdriver_manager.chrome import ChromeDriverManager

from config import chrome_driver_path

base_dir = path.dirname(__file__) + "\\"
driver_path = ChromeDriverManager().install()
copyfile(driver_path, chrome_driver_path)
rmtree(path.expanduser('~')+"/.wdm")
