import pyqrcode
import png
import urllib
from pyqrcode import QRCode
import urllib.request
address = "https://www.cars.bg/offer/61c43af83ad4816cde07d543"
url = pyqrcode.create(address)
url.png('Porshe.png', scale=8)
