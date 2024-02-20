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
    appendRepeats = open("Repeats.txt", "a")
    readRepeats = open("Repeats.txt", "r")
    repeatsList = readRepeats.readlines()
    itemInfo = itemName.split(" ")
    try:
      j = float(itemInfo[1])
    except:
      return 0
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
    currentSell = bzRealData['products'][itemInfo[0]]['buy_summary'][0]['pricePerUnit']
  
    math = ((float(currentSell)/float(itemInfo[1]))*100)-100
    description = str("Average: " + str(itemInfo[1]) + "\nSell Offer: " + str("{:.1f}".format(currentSell)) + "\nInstant Sell: " + str(bzRealData['products'][itemInfo[0]]['sell_summary'][0]['pricePerUnit']) + "\nProfit Percentage (Sell offer): " + str("{:.1f}".format(math)) + "%")
    if float(currentSell) > (float(itemInfo[1]) * 3.5):
      if float(currentSell) > (float(itemInfo[1]) * 10):
        data = {
          "content" : "<@&976279672281247775>",
          "username" : "BZ Logger"
        }
        data["embeds"] = [
          {
            "description" : description,
            "title" : itemInfo[0]
          }
        ]
        requests.post('https://discord.com/api/webhooks/976100292024217601/gp3-Fno4cVEGZ-G4A9vI1J63XL07MW5DleVm3RBY_25LVz_dyN0OoeHA0tVO0bB7zKB4', json = data)
      else:
        data = {
          "content" : "<@&976279629323194459>",
          "username" : "BZ Logger"
        }
        data["embeds"] = [
          {
            "description" : description,
            "title" : itemInfo[0]
          }
        ]
        requests.post('https://discord.com/api/webhooks/976148398577168444/Sj1jJnQgzHQW5WIOONsnn1lVN0QID1MQ_64aRA9PtsNyRSmJr5uPtRXCTzG2vElvd0Lf', json = data)
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
    "username" : "BZ Logger"
  }
  data["embeds"] = [
    {
        "description" : "Time lapsed: " + str(time_lapsed) + " seconds.",
        "title" : "Total BZ Runthrough Time"
    }
  ]
  requests.post("https://discord.com/api/webhooks/976316263150276608/Pjgz19uO1RmMqLc8WwIvb9UesKulu21sQ-RBQpeeH5Qp7kveCZORu5Xf-KI_Cl-0voHw", json = data)
  if count % 15000 == 0:
    d = open("Repeats.txt", "w")
    d.close()
    count = 0