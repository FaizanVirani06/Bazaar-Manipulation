import requests
import time
import sys


def getAverage(itemName):
  response = requests.get("https://sky.coflnet.com/api/bazaar/" + itemName + "/history/day")
  try:
    bzItemData = response.json()
    
    totalBuy = 0
    totalSell = 0
    divideBy = 0
    sellFail = 0
    buyFail = 0
    
    for buy in bzItemData:
      try:
        totalBuy = totalBuy + buy['buy']
        divideBy += 1
      except:
        buyFail += 1
    
    for sell in bzItemData:
      try:
        totalSell = totalSell + sell['sell']
        divideBy += 1
      except:
        sellFail += 1

    try:
      average = (totalBuy + totalSell) / divideBy
      print("Average of " + itemName + " over the past 24h: " + str("{:.1f}".format(average)))
      return average
    except:
      print("An error has occurred calculating the average of " + itemName + ". There were " + str(sellFail) + " sell fails and " + str(buyFail) + " buy fails.", sys.exc_info()[0])
  except:
    print("An error occured grabbing the average of " + itemName + str(response.status_code()))

response = requests.get("https://sky.coflnet.com/api/items/bazaar/tags")
bzItems = response.json()
while True:
  count = 0
  f = open("BazaarItems.txt", "w")
  f.close()
  itemList = []
  for i in range(len(bzItems)):
    start = time.time()
    ranTrue = False
    while ranTrue == False:
      try:
        try:
          a = float(getAverage(bzItems[i]))
          try:
              b = str("{:.1f}".format(a))
          except:
              b = a
              print("Couldn't shorten")
        except:
          b = "None"
        itemList.append(bzItems[i] + " " + b)
        ranTrue = True
      except:
        print("API call quota reached (100/minute)! Retrying.")
        ranTrue = False
  f = open("BazaarItems.txt", "w")
  f.close()

  f = open("BazaarItems.txt", "a")
  for i in itemList:
    f.write(i + "\n")
  f.close()
  time.sleep(21600)