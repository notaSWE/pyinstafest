from datetime import date
from datetime import timedelta
from PIL import Image, ImageDraw, ImageFont
import json, random, sys, time

try:
    username = sys.argv[1].split("takeout/")[1].split(".")[0]
    filePath = sys.argv[1]
except:
    print("Usage: python3 pyinstafest.py takeout/yourname.json")
    quit()

# Initial config
banner = "PRESENTED BY NOTASWE"
try:
    bannerFont = ImageFont.truetype('font/med.ttf', 60)
    headlinerFont = ImageFont.truetype('font/med.ttf', 160)
    userFont = ImageFont.truetype('font/cursive.ttf', 140)
    supportFontLg = ImageFont.truetype('font/med.ttf', 80)
    supportFontSm = ImageFont.truetype('font/med.ttf', 50)
except:
    print("Remember to download/add fonts to font/ directory!")
    quit()

bg = Image.open("img/youtube.png")
imWidth = list(bg.size)[0]
imHeight = list(bg.size)[1]
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
months = ['', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
supportCounter = 0

# Dynamically get festival dates (yesterday, today, tomorrow)
festDates = {}
yesterday = date.today() - timedelta(days = 1)
today = date.today()
tomorrow = date.today() + timedelta(days = 1)
festDates[days[date.weekday(yesterday)]] = f"{months[yesterday.month]} {yesterday.day}"
festDates[days[date.weekday(today)]] = f"{months[today.month]} {today.day}"
festDates[days[date.weekday(tomorrow)]] = f"{months[tomorrow.month]} {tomorrow.day}"

# Parse history and keep track of plays per artist
with open(filePath) as ytHistory:
    jsonHist = json.load(ytHistory)

mostListenedTo = {}
filteredArtists = ['Original Soundtrack']

for item in jsonHist:
    if item['header'] == 'YouTube Music':
        metadata = item['subtitles']
        metadata = metadata[0]
        artist = metadata['name']
        if artist.split(' - Topic')[0] not in filteredArtists and artist in mostListenedTo:
            mostListenedTo[artist] += 1
        else:
            mostListenedTo[artist] = 1

# Get top 3 artists and add to headliners list; remainder to support list
try:
    headliners = []
    for k, _v in sorted(mostListenedTo.items(), key=lambda x: x[1], reverse=True)[:3]:
        headliners.append(k.split(' - Topic')[0])
    support = []
    for k, _v in sorted(mostListenedTo.items(), key=lambda x: x[1], reverse=True)[3:]:
        support.append(k.split(' - Topic')[0])
    # Randomly shuffle support list; off by default
    # random.shuffle(support)
except:
    print("This script assumes you have at least ~30 different artists in your YouTube Music history!")
    quit()

# Function to draw supporting artists underheath lower y value of current headliner
def draw_support(lowestPoint, support):
    # Draw first supporting acts with large font; use of bullet point character is dumb, might fix later
    firstMain = f"{support[0]} • "
    support.pop(0)
    while len(firstMain) <= 42:
        if support and len(firstMain) + len(f"{support[0]} •") <= 42:
            firstMain += f"{support[0]} • "
            support.pop(0)
        else:
            break
    if firstMain[-1] == " ":
        firstMain = firstMain[:-3]

    supportWidth = list(supportFontLg.getsize(firstMain))[0]
    supportCoords = ((imWidth - supportWidth) / 2, lowestPoint - 15)
    printCoords = supportCoords
    firstMain = firstMain.split(" • ")
    for idx, _val in enumerate(firstMain):
        draw_text.text(printCoords, firstMain[idx], font=supportFontLg, fill=(255, 255, 255))
        printCoords = (printCoords[0] + list(supportFontLg.getsize(firstMain[idx]))[0], supportCoords[1])
        if idx != len(firstMain) - 1:
            draw_text.text(printCoords, " • ", font=supportFontLg, fill=(236, 116, 92))
            printCoords = (printCoords[0] + list(supportFontLg.getsize(" • "))[0], supportCoords[1])

    # Draw second supporting acts with small font
    secondMain = f"{support[0]} • "
    support.pop(0)
    while len(secondMain) <= 66:
        if support and len(secondMain) + len(f"{support[0]} •") <= 66:
            secondMain += f"{support[0]} • "
            support.pop(0)
        else:
            break
    if secondMain[-1] == " ":
        secondMain = secondMain[:-3]

    supportWidth = list(supportFontSm.getsize(secondMain))[0]
    supportCoords = ((imWidth - supportWidth) / 2, lowestPoint + 56)
    printCoords = supportCoords
    secondMain = secondMain.split(" • ")
    for idx, _val in enumerate(secondMain):
        draw_text.text(printCoords, secondMain[idx], font=supportFontSm, fill=(255, 255, 255))
        printCoords = (printCoords[0] + list(supportFontSm.getsize(secondMain[idx]))[0], supportCoords[1])
        if idx != len(secondMain) - 1:
            draw_text.text(printCoords, " • ", font=supportFontSm, fill=(236, 116, 92))
            printCoords = (printCoords[0] + list(supportFontSm.getsize(" • "))[0], supportCoords[1])

    # Draw third supporting acts with small font
    thirdMain = f"{support[0]} • "
    support.pop(0)
    while len(thirdMain) <= 66:
        if support and len(thirdMain) + len(f"{support[0]} •") <= 66:
            thirdMain += f"{support[0]} • "
            support.pop(0)
        else:
            break
    if thirdMain[-1] == " ":
        thirdMain = thirdMain[:-3]

    supportWidth = list(supportFontSm.getsize(thirdMain))[0]
    supportCoords = ((imWidth - supportWidth) / 2, lowestPoint + 100)
    printCoords = supportCoords
    thirdMain = thirdMain.split(" • ")
    for idx, _val in enumerate(thirdMain):
        draw_text.text(printCoords, thirdMain[idx], font=supportFontSm, fill=(255, 255, 255))
        printCoords = (printCoords[0] + list(supportFontSm.getsize(thirdMain[idx]))[0], supportCoords[1])
        if idx != len(thirdMain) - 1:
            draw_text.text(printCoords, " • ", font=supportFontSm, fill=(236, 116, 92))
            printCoords = (printCoords[0] + list(supportFontSm.getsize(" • "))[0], supportCoords[1])

# Draw username - note, will truncate after 20th character for proper spacing
yOffset = 20
festname = f"{username[:20]}fest"
draw_username = ImageDraw.Draw(bg)
unameWidth = list(userFont.getsize(festname))[0]
draw_username.text((((imWidth - unameWidth) / 2), yOffset), festname, font=userFont, fill=(255, 255, 255))

# Draw Presented By section
yOffset = 180
draw_present = ImageDraw.Draw(bg)
presentWidth = list(bannerFont.getsize(banner))[0]
draw_present.text((((imWidth - presentWidth) / 2), yOffset), banner, font=bannerFont, fill=(236, 116, 92))

# Prepare to draw headliners
yOffset = 300
dayOffset = 50
dateOffset = 1280
yOffsetHeadliner = None
bottomOfHeadliner = None

# Draw headliners and dates
for i in range(len(headliners)):
    currWidth = list(headlinerFont.getsize(headliners[i]))[0]
    currHeight = list(headlinerFont.getsize(headliners[i]))[1]
    if i == 0:
        yOffsetHeadliner = currHeight / 2
    draw_text = ImageDraw.Draw(bg)
    dayCoords = (dayOffset, yOffset + yOffsetHeadliner)
    dateCoords = (dateOffset, yOffset + yOffsetHeadliner)
    artistCoords = (((imWidth - currWidth) / 2), yOffset)
    draw_text.text(dayCoords, list(festDates.keys())[i], font=bannerFont,  fill=(236, 116, 92))
    draw_text.text(artistCoords, headliners[i], font=headlinerFont, fill=(255, 255, 255))
    draw_text.text(dateCoords, list(festDates.values())[i], font=bannerFont,  fill=(236, 116, 92))

    # Store lower y value of current headliner and pass into draw_support function as a starting point
    bottomOfHeadliner = artistCoords[1] + currHeight
    draw_support(bottomOfHeadliner, support)
    supportCounter += 1
    yOffset += 310

bg.save(f"img/output_{int(time.time())}.png")
