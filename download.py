# Import modules
import pandas as pandas 
import urllib.request

# ------------------------------------------------ #
def url_to_jpg(i, url, file_path):
    filename = 'fehler-{}.txt' .format(i)
    full_path = '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(url, full_path)

    print('{} saved.'.format(filename))
    
    return None
# ------------------------------------------------ #

# Set Constants
FILENAME = 'links.csv'
FILE_PATH = './images/'

# Read List of URLs as Pandas DataFrame
urls = pandas.read_csv(FILENAME)

# 
for i, url in enumerate(urls.values):
    url_to_jpg(i, url[0], FILE_PATH)