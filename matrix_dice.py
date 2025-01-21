# This is a sample outline solution to the first assignment. All of the code can be found within the various teaching materials.
# Dont forget that code within Python needs to be indented correctly otherwise the code will not work.
# This outline solution replicates a simple one dice throw.
# Please check the assignment requirements as to how you can extend the base functionality of this game.

# Import all required modules 
import re
import time
import RPi.GPIO as GPIO
import random
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

# configure both button and buzzer pins
button_pin = 26
buzzer_pin = 18

# set board mode to GPIO.BOARD and setWarnings to False
#e.g. GPIO.setmode(GPIO.BCM)
#e.g. GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# setup button pin asBu input and buzzer pin as output
#e.g. GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#e.g. GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer_pin, GPIO.OUT)

#Generate a Random Seed
random.seed()

dual = 0 #variable for 7 or 11 for final game stats
double = 0 #variable for doubles for final game stats
games = 0  #variable for number of times played for final game stats

def main(cascaded, block_orientation, rotate):
    
    # create matrix device
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=cascaded or 1, block_orientation=block_orientation, rotate=rotate or 0)
    # debugging purpose
    print("[-] Matrix initialized")
    while True :
        #Our outer If statement to see if we have pressed the button OR you can modify this to clap your hands instead of pressing the button
        #To get this to work you will need to explore the sample python scripts within the CrowPi folder on the Pi desktop. i.e. open up the sound or vibration sensor example.
    
            #short delay of 0.5 seconds
            time.sleep(1)

        
            # Roll dice by generating a random number between 1 and 6 and store the number in a variable called result
            result1 = random.randint(1, 6)

            # print our number for debugging purposes to see if it works
            print (result1)
            
            # depending on our random number generated we now need to display the output to the 8x8 matrix
            # to complete this section of code you will need to explore Topic 5
            if result1==1:
                msg = "1"
                print("[-] Printing: %s" % msg)
                show_message(device, msg, fill="blue", font=proportional(CP437_FONT), scroll_delay=0.1)

            if result1==2:
                msg = "2"
                print("[-] Printing: %s" % msg)
                show_message(device, msg, fill="blue", font=proportional(CP437_FONT), scroll_delay=0.1)
                            
            if result1==3:
                msg = "3"
                print("[-] Printing: %s" % msg)
                show_message(device, msg, fill="blue", font=proportional(CP437_FONT), scroll_delay=0.1)    
                
            if result1==4:
                msg = "4"
                print("[-] Printing: %s" % msg)
                show_message(device, msg, fill="blue", font=proportional(CP437_FONT), scroll_delay=0.1)
                
            if result1==5:
                msg = "5"
                print("[-] Printing: %s" % msg)
                show_message(device, msg, fill="blue", font=proportional(CP437_FONT), scroll_delay=0.1)             
                                
            if result1==6:
                msg = "6"
                print("[-] Printing: %s" % msg)
                show_message(device, msg, fill="blue", font=proportional(CP437_FONT), scroll_delay=0.1)
                
                
            # and so on for the 6 sides to the dice
            
            # what about a second dice throw?
            print ("throwing our second dice")

            result2 = random.randint(1, 6)

            print (result2)
            
            # once you have thrown two dice you can then store values to see if you have scored a 7, 11 and a double (i.e both dice are the same number)
            if result2==1:
                msg = "1"
                print("[-] Printing: %s" % msg)
                show_message(device, msg, fill="blue", font=proportional(CP437_FONT), scroll_delay=0.1)
                games = games + 1

            if result2==2:
                msg = "2"
                print("[-] Printing: %s" % msg)
                show_message(device, msg, fill="blue", font=proportional(CP437_FONT), scroll_delay=0.1)
                games = games + 1
                            
            if result2==3:
                msg = "3"
                print("[-] Printing: %s" % msg)
                show_message(device, msg, fill="blue", font=proportional(CP437_FONT), scroll_delay=0.1)
                games = games + 1
                
            if result2==4:
                msg = "4"
                print("[-] Printing: %s" % msg)
                show_message(device, msg, fill="blue", font=proportional(CP437_FONT), scroll_delay=0.1)
                games = games + 1
                
            if result2==5:
                msg = "5"
                print("[-] Printing: %s" % msg)
                show_message(device, msg, fill="blue", font=proportional(CP437_FONT), scroll_delay=0.1)
                games = games + 1
                                
            if result2==6:
                msg = "6"
                print("[-] Printing: %s" % msg)
                show_message(device, msg, fill="blue", font=proportional(CP437_FONT), scroll_delay=0.1)
                games = games + 1


            if result1+result2==7:
                msg = "7"
                print("[-] Printing: %s" % msg)
                show_message(device, msg, fill="blue", font=proportional(CP437_FONT), scroll_delay=0.1)
                dual = dual + 1

            if result1+result2==11:
                msg = "11"
                print("[-] Printing: %s" % msg)
                show_message(device, msg, fill="blue", font=proportional(CP437_FONT), scroll_delay=0.1)
                dual = dual + 1
                

            # if you scored a double sound the buzzer 
            if result1==1 and result2==1:
                GPIO.output(buzzer_pin, GPIO.HIGH)
                GPIO.output(buzzer_pin, GPIO.LOW)
                double = double + 1

            if result1==2 and result2==2:
                GPIO.output(buzzer_pin, GPIO.HIGH)
                GPIO.output(buzzer_pin, GPIO.LOW)
                double = double + 1

            if result1==3 and result2==3:
                GPIO.output(buzzer_pin, GPIO.HIGH)
                GPIO.output(buzzer_pin, GPIO.LOW)
                double = double + 1

            if result1==4 and result2==4:
                GPIO.output(buzzer_pin, GPIO.HIGH)
                GPIO.output(buzzer_pin, GPIO.LOW)
                double = double + 1

            if result1==5 and result2==5:
                GPIO.output(buzzer_pin, GPIO.HIGH)
                GPIO.output(buzzer_pin, GPIO.LOW)
                double = double + 1

            if result1==6 and result2==6:
                GPIO.output(buzzer_pin, GPIO.HIGH)
                GPIO.output(buzzer_pin, GPIO.LOW)
                double = double + 1


            time.sleep(3)

            # once you have played the game a few times exit the game and display a short summary. this can be done using the debug print option rather than using the 8x8 matrix LED but its up to you!!


print("~~~ THE GAME HAS ENDED ~~~")

# we might want to use this opportunity
print ("thanks for playing")
print ("          ")
print ("game stats")

# output number of 7,11 and doubles
# additional print statements under game stats to output the number of 7's, 11's and doubles.
print ("You rolled a 7 and 11 this many times")
print (dual) #print the number of toal 7 and 11s that where achived in the game
print ("          ")
print ("You rolled a double this many times")
print (double) #print the number of toal doubles that where achived in the game
print ("          ")
# output games played
print ("You played the game this many times")
print (games) #print the number of times the game was played
            
                
# no need to change the code below - do not modify
if __name__ == "__main__":
    
    # cascaded = Number of cascaded MAX7219 LED matrices, default=1
    # block_orientation = choices 0, 90, -90, Corrects block orientation when wired vertically, default=0
    # rotate = choices 0, 1, 2, 3, Rotate display 0=0°, 1=90°, 2=180°, 3=270°, default=0
   
    try:
        main(cascaded=1, block_orientation=90, rotate=0)
    except KeyboardInterrupt:
        pass
