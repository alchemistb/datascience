# **********************************************************************
# THIS IS THE IBM DATA SCIENCE PYTHON COURSE FINAL PROJECT  ON 9/20/18 *
# **********************************************************************



from IPython.display import Image as IPythonImage
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests
import re 

# Helper function to superimpose text on image

def display_cover(top,bottom ):
    """This function
    """
    #import requests

    name='album_art_raw.png'
    # Now let's make get an album cover.
    # https://picsum.photos/ is a free service that offers random images.
    # Let's get a random image:
    album_art_raw = requests.get('https://picsum.photos/500/500/?random')
    # and save it as 'album_art_raw.png'
    with open(name,'wb') as album_art_raw_file:
       album_art_raw_file.write(album_art_raw.content)
    # Now that we have our raw image, let's open it
    # and write our band and album name on it
    img = Image.open("album_art_raw.png")
    draw = ImageDraw.Draw(img)

    # We'll choose a font for our band and album title,
    # run "% ls /usr/share/fonts/truetype/dejavu" in a cell to see what else is available,
    # or download your own .ttf fonts!
    band_name_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18) #25pt font
    album_name_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 15) # 20pt font

    # the x,y coordinates for where our album name and band name text will start
    # counted from the top left of the picture (in pixels)
    band_x, band_y = 50, 50
    album_x, album_y = 50, 400

    # Our text should be visible on any image. A good way
    # of accomplishing that is to use white text with a
    # black border. We'll use the technique shown here to draw the border:
    # https://mail.python.org/pipermail/image-sig/2009-May/005681.html
    outline_color ="black"

    draw.text((band_x-1, band_y-1), top, font=band_name_font, fill=outline_color)
    draw.text((band_x+1, band_y-1), top, font=band_name_font, fill=outline_color)
    draw.text((band_x-1, band_y+1), top, font=band_name_font, fill=outline_color)
    draw.text((band_x+1, band_y+1), top, font=band_name_font, fill=outline_color)

    draw.text((album_x-1, album_y-1), bottom , font=album_name_font, fill=outline_color)
    draw.text((album_x+1, album_y-1), bottom , font=album_name_font, fill=outline_color)
    draw.text((album_x-1, album_y+1), bottom , font=album_name_font, fill=outline_color)
    draw.text((album_x+1, album_y+1), bottom , font=album_name_font, fill=outline_color)

    draw.text((band_x,band_y),top,(255,255,255),font=band_name_font)
    draw.text((album_x, album_y),bottom,(255,255,255),font=album_name_font)

    return img

# Learn how to use the function display_cover


img=display_cover(top='top',bottom='bottom')
img.save('sample-out.png')
IPythonImage(filename='sample-out.png')

img=display_cover(top='Python',bottom='Data Science')
img.save('Py-sample-out.png')
IPythonImage(filename='Py-sample-out.png')


# Part 2: Loading a random page from Wikipedia
# Use the function get from the requests library to download the Wikipedia page using the wikipedia_link as an argument. 

# Assign the object to the variable raw_random_wikipedia_page.

wikipedia_link='https://en.wikipedia.org/wiki/Special:Random'

box = []
for items in raw_random_wikipedia_page:
    box.append(items)
    page = box

# Use the data attribute text to extract the XML as a text file a string and assign the result variable page:

print(page)


# Part 3: Extacting the Title of the Article

# Capture the data that has <title>Some-title-Wikipedia</title> in 'page' output.

pattern = r'>.*<'
found = re.findall(pattern, str(page))
string = found[0:1]

for thing in found:
    if 'title' in thing:
        target = thing[50:200]
        find = re.search(r'<title.*?>(.+)<.*title>',str(target)).group(0)
        print(find)

# Get rid of the term 'Wikipedia' from the title output, and assign to band_title.

if "Wikip', b'edia" in find:
    band_title = find.replace("Wikip', b'edia", "")
    print('band_title')
    print(band_title)
else:
    if 'Wikipedia' in find:
        band_title = find.replace('Wikipedia', '')
        print('band_title')
        print(band_title)

# Get rid of the term 'Wikipedia' from the title output, and assign to album_title.

if "Wikip', b'edia" in find:
    album_title = find.replace("Wikip', b'edia", "")
    print('album_title')
    print(album_title)
else:
    if 'Wikipedia' in find:
        album_title = find.replace('Wikipedia', '')
        print('album_title')
        print(album_title)


# Display album and band name

print("Your band: ", band_title)
print("Your album: ", album_title)



# Part 4: Displaying the Album Cover
# Use the function display_cover to superimpose the band and album title over a random image, assign the result to the variable album_cover


band = band_title
album = album_title
img=display_cover(top=band,bottom=album)

# Use the method save to save the image as sample-out.png:
img.save('sample-out.png')

# Use the function **IPythonImage** to display the image 
IPythonImage(filename='sample-out.png')

