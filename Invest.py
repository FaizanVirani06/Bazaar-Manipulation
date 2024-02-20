import requests
import time

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

readBZ = open("BazaarItems.txt", "r")
bzList = readBZ.readlines()

for i in bzList:
  i = i.replace("\n", "")

def getManip(itemName):
  try:
    appendRepeats = open("Repeats2.txt", "a")
    readRepeats = open("Repeats2.txt", "r")
    repeatsList = readRepeats.readlines()
    itemInfo = itemName.split(" ")
  
    try:
      bzRealData['products'][itemInfo[0]]['buy_summary'][0]['pricePerUnit']
      bzRealData['products'][itemInfo[0]]['sell_summary'][0]['pricePerUnit']
    except:
      return 0
  
    for i in repeatsList:
      i = i.replace("\n", "")
      if i == itemInfo[0]:
        return 0
    itemInfo[1] = itemInfo[1].replace("\n", "")
    currentSell = bzRealData['products'][itemInfo[0]]['sell_summary'][0]['pricePerUnit']
  
    math = (float(itemInfo[1])/float(currentSell))
    description = str("Average: " + itemInfo[1] + "\nBuy Order: " + str("{:.1f}".format(currentSell)) + "\nInstant Buy: " + str(bzRealData['products'][itemInfo[0]]['buy_summary'][0]['pricePerUnit']) + "\nProfit Percentage: " + str("{:.1f}".format(math)) + "%")
    if (float(currentSell) <= float(itemInfo[1]) * 0.8 and float(itemInfo[1]) > 100000 and float(bzRealData['products'][itemInfo[0]]['quick_status']['sellVolume']) > 50):
      if float(currentSell) <= float(itemInfo[1]) * 0.5 and float(itemInfo[1]) > 100000:
        data = {
          "content" : "<@&976303712278568960>",
          "username" : "BZ Investor"
        }
        data["embeds"] = [
          {
            "description" : description,
            "title" : itemInfo[0]
          }
        ]
        requests.post('https://discord.com/api/webhooks/976304365130358814/qUFCNIsaOhrq2e4ij3G4Ke_NVWUz3mOUmUtPft7Hr1U-c3s0LgjKYJIBHpav8PUWjz9s', json = data)
      else:
        data = {
          "content" : "<@&976303625901076530>",
          "username" : "BZ Investor"
        }
        data["embeds"] = [
          {
            "description" : description,
            "title" : itemInfo[0]
          }
        ]
        requests.post('https://discord.com/api/webhooks/976302340007149678/V67JNPhKwmQ59TMeY8eIIaNlLHYQN6PZxcUwxaAAb67LhnIkPKH-byX4TKKVUTDFsWG2', json = data)
      appendRepeats.write(itemInfo[0] + "\n")
    print(itemInfo[0])
  except:
    print("An error occurred")

count = 0
while 1:
  start = time.time()
  bzReal = requests.get("https://api.hypixel.net/skyblock/bazaar")
  bzRealData = bzReal.json()
  for i in range(len(bzList)):
    ranTrue = False
    while ranTrue == False:
      try:
        getManip(bzList[i])
        ranTrue = True
      except:
        ranTrue = False
  end = time.time()
  time_lapsed = end - start
  time_convert(time_lapsed)
    
  count += 1
  data = {
    "content" : "Speed",
    "username" : "BZ Investor"
  }
  data["embeds"] = [
    {
        "description" : "Time lapsed: " + str(time_lapsed) + " seconds.",
        "title" : "Total BZ Runthrough Time"
    }
  ]
  requests.post("https://discord.com/api/webhooks/976582142383521872/qFdxfC_Vxu-YIZ3Rmeq6bNePvy2C4PLEJvCO9NHeXWJx4puk7XBpxZcCGSx62rDHevbf", json = data)
  if count % 9000 == 0:
    d = open("Repeats2.txt", "w")
    d.close()
    count = 0