# https://create.withcode.uk/

# This version of the dice game can be used with the GPIO Simulator. You can practise with the python code and getting this to work at home. When you are happy with the code and the basics of it working you can then explore the outline python code for the CrowPi kits. 

# import modules
import RPi.GPIO as GPIO
import time
import random

print ("Are you ready to start playing this game?") #welcome message
input("Hit enter to continue!") #start the game with hitting enter


# setup pins
GPIO.setmode(GPIO.BOARD)
# setup our outputs for the simulated LEDS. We want six of them so alongside each other would be best on the GPIO simulator e.g. 27,29,31,33,35 and 37
GPIO.setup(27, GPIO.OUT) #show light if 1 rolled
GPIO.setup(29, GPIO.OUT) #show light if 2 rolled
GPIO.setup(31, GPIO.OUT) #show light if 3 rolled
GPIO.setup(33, GPIO.OUT) #show light if 4 rolled
GPIO.setup(35, GPIO.OUT) #show light if 5 rolled
GPIO.setup(37, GPIO.OUT) #show light if 6 rolled

GPIO.setup(5, GPIO.IN) #pin can be toggled on and off

# set the remaining ones

# set one pin as input e.g. GPIO.setup(5, GPIO.IN)

# generate our random seed e.g. random.seed()
random.seed()

dual = 0 #variable for 7 or 11 for final game stats
double = 0 #variable for doubles for final game stats
games = 0  #variable for number of times played for final game stats

# our main game loop. this can either be a for loop set to repeat a number of times or a while loop

# loop 5 times
for i in range(5):
  
    GPIO.output(27, GPIO.LOW) #turn off this light
    GPIO.output(29, GPIO.LOW) #turn off this light
    GPIO.output(31, GPIO.LOW) #turn off this light
    GPIO.output(33, GPIO.LOW) #turn off this light
    GPIO.output(35, GPIO.LOW) #turn off this light
    GPIO.output(37, GPIO.LOW) #turn off this light
  
    if GPIO.input(5) == GPIO.HIGH: #if pin 5 is toggled on print on if not print off
        print("Pin 5 is on")
    else:
        print("Pin 5 is off")

    # generate random number between 1 and 6 and store this number in a variable called result. if throwing 2 dice call this result1
    result1 = random.randint(1, 6)
    
    # print our result1 so we can check if our random number worked
    print (result1) #print the result1 for a number from 1 - 6 at random

    # we now need to check the random number generated stored in our result1 variable and to produce a suitable output. e.g. for the dice simulator we need to light one of the virtual LED's.
    if result1==1: #if the number stored in the variable is equal to 1 then print you rolled a 1 and turn the light for number 1 on
      print ("you rolled a 1")
      GPIO.output(27, GPIO.HIGH)

    # we need to repeat this another 5 times over and check result for 2,3,4,5 and 6
    if result1==2: #if the number stored in the variable is equal to 2 then print you rolled a 2 and turn the light for number 2 on
      print ("you rolled a 2")
      GPIO.output(29, GPIO.HIGH)

    if result1==3: #if the number stored in the variable is equal to 3 then print you rolled a 3 and turn the light for number 3 on
      print ("you rolled a 3")
      GPIO.output(31, GPIO.HIGH)

    if result1==4: #if the number stored in the variable is equal to 4 then print you rolled a 4 and turn the light for number 4 on
      print ("you rolled a 4")
      GPIO.output(33, GPIO.HIGH)

    if result1==5: #if the number stored in the variable is equal to 5 then print you rolled a 5 and turn the light for number 5 on
      print ("you rolled a 5")
      GPIO.output(35, GPIO.HIGH)

    if result1==6: #if the number stored in the variable is equal to 6 then print you rolled a 6 and turn the light for number 6 on
      print ("you rolled a 6")
      GPIO.output(37, GPIO.HIGH)
      
    #input("Hit enter to continue!")

    # introduce a slight 3 second pause
    time.sleep(3)
  
    # we need to reset our previous 6 LEDs to OFF for the second dice throw so set these to GPIO.LOW
    # e.g. GPIO.output(27, GPIO.LOW)
    GPIO.output(27, GPIO.LOW) #turn off this light
    GPIO.output(29, GPIO.LOW) #turn off this light
    GPIO.output(31, GPIO.LOW) #turn off this light
    GPIO.output(33, GPIO.LOW) #turn off this light
    GPIO.output(35, GPIO.LOW) #turn off this light 
    GPIO.output(37, GPIO.LOW) #turn off this light
  
    #output statement to state we are throwing our second dice
    #print "throwing our second dice"
    print ("throwing our second dice")
        
    # now generate our second random number but this time store this in a new variable called result2
    result2 = random.randint(1, 6)
    
    # repeat the same process using an if statement to check the random number generated against result2
    
    # print our result2 so we can check if our random number worked
    print (result2) #print the result2 for a number from 1 - 6 at random
    
    # we now need to check the random number generated stored in our result2 variable and to produce a suitable output. e.g. for the dice simulator we need to light one of the virtual LED's.
    if result2==1: #if the number stored in the variable is equal to 1 then print you rolled a 1 and turn the light for number 1 on also add 1 to the variable games for the final stats
      print ("you rolled a 1")
      GPIO.output(27, GPIO.HIGH)
      games = games + 1

    if result2==2: #if the number stored in the variable is equal to 2 then print you rolled a 2 and turn the light for number 2 on also add 1 to the variable games for the final stats
      print ("you rolled a 2")
      GPIO.output(29, GPIO.HIGH)
      games = games + 1

    if result2==3: #if the number stored in the variable is equal to 3 then print you rolled a 3 and turn the light for number 3 on also add 1 to the variable games for the final stats
      print ("you rolled a 3")
      GPIO.output(31, GPIO.HIGH)
      games = games + 1

    if result2==4: #if the number stored in the variable is equal to 4 then print you rolled a 4 and turn the light for number 4 on also add 1 to the variable games for the final stats
      print ("you rolled a 4")
      GPIO.output(33, GPIO.HIGH)
      games = games + 1

    if result2==5: #if the number stored in the variable is equal to 5 then print you rolled a 5 and turn the light for number 5 on also add 1 to the variable games for the final stats
      print ("you rolled a 5")
      GPIO.output(35, GPIO.HIGH)
      games = games + 1

    if result2==6: #if the number stored in the variable is equal to 6 then print you rolled a 6 and turn the light for number 6 on also add 1 to the variable games for the final stats
      print ("you rolled a 6")
      GPIO.output(37, GPIO.HIGH)
      games = games + 1
      
    
    # in the for loop after we have rolled two dice, perform a check for a 7,11 and a double (i.e. both dice have the same number). This can be done using further if statements. e.g. if result1 + result 2 == 7
    # we need to store the number of 7, 11's and doubles so these need to be stored within new variables at the start of our code and these need to be incremented
    if result1+result2==7: #if the variable result1 from die 1 and result2 from die 2 equal 7 when added together output you rolled a 7 which is a dual and also add 1 to the variable dual for the final stats
      print ("you rolled a 7 which is a dual")
      dual = dual + 1
      
    if result1+result2==11: #if the variable result1 from die 1 and result2 from die 2 equal 11 when added together output you rolled a 11 which is a dual and also add 1 to the variable dual for the final stats
      print ("you rolled a 11 which is a dual")
      dual = dual + 1
      
      
    if result1==1 and result2==1: #if the variable result1 and result2 equal 1 output you rolled 2 which is a double and also add 1 to the variable double for the final stats
      print ("you rolled 2 which is a double")
      double = double + 1

    if result1==2 and result2==2: #if the variable result1 and result2 equal 2 output you rolled 4 which is a double and also add 1 to the variable double for the final stats
      print ("you rolled 4 which is a double")
      double = double + 1

    if result1==3 and result2==3: #if the variable result1 and result2 equal 3 output you rolled 6 which is a double and also add 1 to the variable double for the final stats
      print ("you rolled 6 which is a double")
      double = double + 1

    if result1==4 and result2==4: #if the variable result1 and result2 equal 4 output you rolled 8 which is a double and also add 1 to the variable double for the final stats
      print ("you rolled 8 which is a double")
      double = double + 1

    if result1==5 and result2==5: #if the variable result1 and result2 equal 5 output you rolled 10 which is a double and also add 1 to the variable double for the final stats
      print ("you rolled 10 which is a double")
      double = double + 1

    if result1==6 and result2==6: #if the variable result1 and result2 equal 6 output you rolled 12 which is a double and also add 1 to the variable double for the final stats
      print ("you rolled 12 which is a double")
      double = double + 1
      
    #input("Hit enter to continue!")
      
    # introduce a slight 3 second pause
    time.sleep(3)
 
# when we have played the game 5 times we will exit our for loop and display the output
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


# extended functionality
#------------------------
# in the for loop after we have rolled two dice, perform a check for a 7,11 and a double (i.e. both dice have the same number). This can be done using further if statements. e.g. if result1 + result 2 == 7
# we need to store the number of 7, 11's and doubles so these need to be stored within new variables at the start of our code and these need to be incremented
# additional print statements under game stats to output the number of 7's, 11's and doubles.
# we might also want to swap out the for loop for a while loop and make use of try and except or alternatively the game will only play when our input pin 5 is used and this is enabled by clicking on pin 5 in the GPIO simulator.

