from PIL import Image, ImageFont, ImageDraw
import sys
import os

W, H = (32, 32)

# draw_letter_img draws and saves an image
def draw_letter_img(msg):
  img = Image.new(mode="RGB", size=(W, H), color=(255, 255, 255))

  # Set directory
#  os.chdir("\PythonDrawLetterImages\Fonts")
#  print("Change dir")

  font = "Fonts/AGENCYB.ttf"

  # import font
  im_font = ImageFont.truetype(font, size=32)
  
  # make created image editable
  im_draw = ImageDraw.Draw(img)
  
  # compute size of rendered text
  w, h = im_draw.textsize(msg, font=im_font)
  # draw text in the center based on the size of rendered text
  # note the offset of the height-- this may depend on font
  im_draw.text(((W-w)/2,((H-h)/2)-6), msg, font=im_font, fill="black")
  
  # save file as msg.jpg (so if msg is hello you get hello.jpg)
  file = f"{msg}.jpg"
  img.save(file)
  print(f"Drew {file}.")
  

draw_letter_img("A")
draw_letter_img("B")

if len(sys.argv) < 2:
  print("Draw a custom image: python3 main.py <letter to draw>")
else:
  draw_letter_img(sys.argv[1])
