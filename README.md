# pyinstafest
instafest.app ripoff for the few youtube music users out there

## Why?

End of year FOMO every time my friends post their Spotify wrapped, and this year, output from instafest.app

## How?

I'm stubborn and like writing Python

## Installation/configuration

1. Export the json from [Google Takeout](https://takeout.google.com) - you ONLY need YouTube/YouTube music!
    1. Save the file as __yourname__.json
2. Git clone this repo
3. Copy the export from step 1 into __takeout/__
    1. Relative path should be __takeout/yourname.json__ 
4. Download a cool font or two and save the .ttf file(s) in __font/__
    1. Relative path should be __font/fontname.ttf__
    2. Note, I saved the below medium YouTube font to __font/med.ttf__ and Old Figaro to __font/cursive.ttf__
    2. Update the font config in __pyinstafest.py__ (lines 15-19) if your font filenames are different!
5. __python3 pyinstafest.py takeout/yourname.json__
    1. Images will output to **img/output_unixtimestamp.png**

## Images

![Demo output](/img/sample.png "This is a sample output file")

## Fonts links (external)

* [Old Figaro Font](https://www.dafont.com/old-figaro-cursive.font)
* [YouTube Font](https://www.dafontfree.io/youtube-logo-font/)


## Notes

* I did not test this thoroughly
* It works on my machine though
* Oh yeah, I realized that I use the bullet point character "•" which isn't supported by all fonts so...things might get weird if you use custom fonts
* I might fix that later idk
* Lastly, if there are bands/artists you don't want, simply add them to the __filteredArtists__ list
