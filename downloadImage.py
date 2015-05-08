"""
downloadImage.py has access to the gilt api with a specified api key.
It gets access to the sales information of gilt and download the photos
of sale items to local folder. User can specify the parameters and choose 
certain sale items. Specifications can be found on gilt API documentation
https://dev.gilt.com/documentation/appendix.html
"""

from gilt.rest import GiltApiClient
from defClothes import *
import urllib

# Create client using api_key
client = GiltApiClient(api_key = '4bc9ea982749056525a630ff9eb6deda9f737c2a94492963f29e32f077ed766f')

# Get Active Sales info, go to men store, need to check what sales there are
i = 0
startIndex = 5071 # Each time update data, we want to start at the right index

readsales = open("inputs/saleName.dat", "r")
downloaded_sales = []
while 1:


  line = readsales.readline()
  if len(line) == 0: break

  downloaded_sales.append(line[:-1])

readsales.close()

outfile = open("inputs/gilt2.dat", "w")
salefile = open("inputs/saleName2.dat", "w")

for sale in client.sales.active('men'):
  product_urls = sale.products
  if not product_urls:
    continue

  if sale.name in downloaded_sales:
    # print "pass"
    continue
  else:
    print 'First %d products (of %d) of sale "%s"' % (len(product_urls), len(sale.products), sale.name)

    try:
      salefile.write(sale.name)
      salefile.write("\n")
    except:
      continue

    for url in product_urls:
      try:
        product = client.products.get(url=url)
        name = product.name.split()
        category = name[len(name)-1].lower()
        for item in article_list:
          if category in item:
            startIndex += 1
            print category
            outfile.write(str(startIndex) + " " + category + " " + product.name + "," + sale.name)

            outfile.write("\n")
            for image in product.image_urls.image_list("300x400"):
              # print image.url
              urllib.urlretrieve(image.url, "img/lg-" + str(startIndex) + ".jpg")
              break
      except:
        continue

outfile.close()
salefile.close()



