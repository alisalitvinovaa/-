from PIL import Image, ImageDraw, ImageFont
from colorama import Fore, Style

print("Генератор мемов запущен!")
e=input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний: ")
top_text=""
bottom_text=""

if e=="1":
   bottom_text=input("Введите нижний текст мема ")
elif e=="2":
    top_text = input("Введите верхний текст мема ")
    bottom_text = input("Введите нижний текст мема ")
else:
    print(f"{Fore.RED}Введено неправильное число{Style.RESET_ALL}")
    quit()
print(f'{Fore.GREEN} {top_text} \n{bottom_text} {Style.RESET_ALL}')
list=['котик_в_шапочке.jpg','котик_на_спине.jpg','котик_в_ванной.jpg','кот_в_очках.png','кот_в_ресторане.png']
print("\nсписок мемчиков ")
for i in range(0, len(list)):
    print(f'{i}.{list[i]}')
r=int(input("Выберите картинку "))
if 0<=r<=len(list)-1:
    print( f"Ваш выбор: {list[r]}")
else:
    print(f"{Fore.RED}Введено неправильное число{Style.RESET_ALL}")
    quit()


f="/Library/Fonts/Arial.ttf"
im=Image.open(list[r])
wight, height= im.size
draw=ImageDraw.Draw(im)
font=ImageFont.truetype(f, size=70)

text=draw.textbbox((0,0),top_text, font)
text2=draw.textbbox((0,0),bottom_text, font)

draw.text(((wight - text[2])/2,5), top_text, font=font, fill="white", stroke_width=4, stroke_fill="black")
draw.text(((wight - text2[2])/2,(height - text2[3])-10), bottom_text, font=font, fill="white", stroke_width=4, stroke_fill="black")
im.save("new.memchik.jpg")
im.show()