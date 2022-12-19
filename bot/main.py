import os
import discord
import random
import json
import difflib

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

containerFileList = ["SantasGift2021.json", "SantasBigGift2021,json", "SantasMegaGift2021.json", "SantasGift2022,json", "SantasBigGift2022.json", "SantasMegaGift2022.json"] #list of container data .json file names
containerDataList = [] #container data
containerNameList = [] #container names
for filename in containerFileList:
    f = open(filename, "r", encoding="utf-8")
    data = json.load(f)
    containerDataList.append(data)
    containerNameList.append(data["name"])
    f.close()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
@client.event
async def on_message(message):
    if message.author == client.user: #ignore messages from itself
        return
    if '!collection'.lower() in message.content.lower() and message.content[0] == "!":
        content = message.content.split(" ")
        if len(content) == 5 and content[1].isdigit() and content[2].isdigit() and content[3].isdigit() and content[4].isdigit():
            runs = 100000
            n = int(content[1])
            k = int(content[2])
            d = int(content[3])
            c = int(content[4])
            if n > 100:
                await message.channel.send("There can not be more than 100 items in a collection.")
            elif n <= 0:
                await message.channel.send("There must be at least one item in a collection.")
            elif k > n:
                await message.channel.send("There can not be more items currently owned than there are total items in a collection.")
            elif k < 0:
                await message.channel.send("There can not be less than 0 items owned.")
            elif d < 0:
                await message.channel.send("There can not be less than 0 duplicates owned.")
            elif c <= 0:
                await message.channel.send("The conversion cost of duplicates to an item must be 1 or higher.")
            else:
                totalcontainers = 0
                array = []
                for i in range(runs):
                    collection = (n - k) * [-1] + (k) * [1]
                    containers = 0
                    dupes = d
                    empties = n - k
                    while(empties != 0):
                        containers += 1
                        index = int(n * random.random())
                        if collection[index] == 1:
                            dupes += 1
                        else:
                            collection[index] = 1
                            empties -= 1
                        if dupes / c >= empties:
                            break
                    totalcontainers += containers
                    array.append(containers)
                array.sort(reverse=True)
                collectionmessage = "```"
                collectionmessage += "\nOn average, you will need to open " + str(totalcontainers / runs) + " containers."
                collectionmessage += "\nYou can reasonably expect to open between " + str(array[int(0.9985 * runs)]) + " and " + str(array[int(0.0015 * runs)]) + " containers to complete the collection."
                collectionmessage += "\nAt 0.15 percentile:  " + str(array[int(0.0015 * runs)])
                collectionmessage += "\nAt 2.5 percentile:   " + str(array[int(0.025 * runs)])
                collectionmessage += "\nAt 16 percentile:    " + str(array[int(0.16 * runs)])
                collectionmessage += "\nAt the median:       " + str(array[int(0.5 * runs)])
                collectionmessage += "\nAt 84 percentile:    " + str(array[int(0.84 * runs)])
                collectionmessage += "\nAt 97.5 percentile:  " + str(array[int(0.975 * runs)])
                collectionmessage += "\nAt 99.85 percentile: " + str(array[int(0.9985 * runs)]) + "```"
                await message.channel.send(collectionmessage)
        else:
            await message.channel.send("Please use the format: !collection [total number of collection items] [current number of collection items owned] [current number of duplicates owned] [number of duplicates need to purchase one collection item]")
    if '!help'.lower() in message.content.lower() and message.content[0] == "!":
        await message.channel.send("Use !open [container name]. Always assumes no unique items are currently owned and will not account for duplicates and pity successes when opening one container after another. Available containers: " + ", ".join(sorted(containerNameList)))
    if '!open'.lower() in message.content.lower() and message.content[0] == "!":
        containerData = containerDataList[containerNameList.index(difflib.get_close_matches(message.content.lower().partition(' ')[2], containerNameList, n=1, cutoff=0)[0])] #finds closest container name to input
        
        embeded = discord.Embed(title=containerData["name"] + " Container",color=discord.Color.from_str(containerData["color"]))
        
        dropPool = containerData["drops"]
        roll = random.random() * 100
        dropIndex = -1 # current drop
        lastRate = 100

        if "rate" in dropPool[0].keys(): # the current drop pool has manual rates
            while roll >= 0:
                dropIndex += 1
                roll -= dropPool[dropIndex]["rate"] / 100 * lastRate
                tempRate = dropPool[dropIndex]["rate"] / 100 * lastRate
        else: # the current drop pool has evenly distributed rates
            dropIndex = roll // lastRate * len(dropPool)
            tempRate = lastRate / len(dropPool)

        while "drops" in dropPool[dropIndex].keys():
            dropPool = dropPool[dropIndex]["drops"]
            lastRate = tempRate
            roll += lastRate
            dropIndex = -1

            if "rate" in dropPool[0].keys(): # the current drop pool has manual rates
                while roll >= 0:
                    dropIndex += 1
                    roll -= dropPool[dropIndex]["rate"] / 100 * lastRate
                    tempRate = dropPool[dropIndex]["rate"] / 100 * lastRate
            else: # the current drop pool has evenly distributed rates
                dropIndex = int(roll // (lastRate / len(dropPool)))
                tempRate = lastRate / len(dropPool)
        drop = dropPool[dropIndex]

        embeded.description = drop["name"]
        if "link" in drop.keys():
            embeded.set_image(url=drop["link"])

        await message.channel.send(embed=embeded)

client.run(TOKEN)