import my_oled
import time

state = 0
while True: 
    print(state)
    #pass

    if state >= 4: 
        state = 0
    my_oled.oled.fill(0)


    if state == 0: 
        my_oled.print_text("test", 0, 0)
    if state == 1: 
        my_oled.print_text("something else", 0, 50)
    if state == 2: 
        my_oled.oled.line(0,64,128,0,1)

    if state ==3: 
        my_oled.graphics.fill_rect(64,32,64,32,1)
        
    state = state + 1
    my_oled.oled.show()
    time.sleep(1)



