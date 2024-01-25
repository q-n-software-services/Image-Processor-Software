import pyautogui as pt
from time import sleep
import pyperclip
import random
import turtle
count = 0
sleep(5)
coord_list = [(0, 0)]
check = False
while count < 112:
    check = False
    position1 = pt.locate("plus4.png", 'test.jpg', confidence=.7)
    x = position1[0]
    y = position1[1]
    position1 = None
    print(count, " : ", x, y)
    pt.moveTo(x, y, duration=.0001)
    for i in range(len(coord_list)):
        if x == coord_list[i][0] and y == coord_list[i][1]:
            check = True
    if check == False:
        coord_list.append((x, y))
    count = count + 1
    x = None
    y = None


print(coord_list)
''' pt.tripleClick()

    pt.moveRel(35, -27)
    sleep(.1)
    pt.moveRel(0, -12)

    pt.click()

    pt.moveRel(12, 15)

    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("message recieved:\t\t" + whatsapp_message)'''



# posts
'''

def post_response(message):
    global x, y
    position = pt.locateOnScreen("smily_paperclip.jpg", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x+200, y+20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)

# processes response

def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't ask me any Questions"
    else:
        if random_no == 0:
            return "Thats cool"
        elif random_no == 1:
            return "Please call if its urgent, I won't reply on WhatsApp"
        else:
            return "I want to eat something"



# check for new messages


def check_for_new_messages():
    pt.moveTo(x+50, y-70, duration=.5)
    while True:
        # continuously checks for green dot and new messages

        position = pt.locateOnScreen("green_circle.jpg", confidence=.7)
        if position is not None:
            pt.moveTo(position)
            pt.moveRel(-100, 0)
            pt.click()
            sleep(.5)

        else:
            print("No new messages found")
            continue

        #if pt.pixelMatchesColor(int(x+50), int(y-70), (255, 255, 255), tolerance=10):
         #   print("is white")
        processed_message = process_response(get_message())

        post_response(processed_message)

        pt.moveTo(1330, 94)
        pt.click()
        pt.moveTo(1243, 229)
        pt.click()

        #else:
        #    print("No new messages yet...")

        sleep(5)


check_for_new_messages()
'''





