import PySimpleGUI as sg # import of module PySimpleGUI
import random # import of module random
import webbrowser # import of module webbrowser

Name={"Nicholas M James"} # var attrib name
BusinessName={"LILLY PAD LLC"} # var attrib business name
BusinessOwner={"Nicholas M James Sole MBR"} # var attrib business owner
SchoolName={"University of Advancing Technology"} # var attrib school name
CourseName={"CSC235 Python Programming"} # var attrib course name
SchoolId={"njames86877"} # var attrib school id
# Assignment 5-1 Final Project

dict = { # dictionary creation
    "pictures" : ["frog", "fly", "obstacle"], # value attrib for pictures
    "direction" : ["Up", "Down", "Left", "Right"],# value attrib for directions
    "text" : ["Greetings", "Congratulations", "Obstacle Hit", "Play Again", "Thanks for Playing", "Title"] # value attrib for text to user
}

frgamevar = { # second dictionary creation
    "self": ["frog","fly", "obstacle"], # value attrib for objects
    "width": [20], # value for width of console
    "height":[5], # value for height for console
    "frog":["position"],# value for frog position
    "fly":["position"], # value for fly position
    "obstacle":["position"],# value for obstacle
    "direction":["Up","Down","Left","Right"], # value for direction
    "action":[1, 2, 3, 4], # value for
    "playagain": [1, 2], # value attrib for play again options
    "randint": [random] # value attrib for random int
}

frogPic='lovedfrogprince.jpg' # attrib file name for frog picture
flyPic='fly.jpg' # attrib file name for fly picture
obstaclePic='rubixobstacle.jpg' # attrib file name for obstacle 

sg.theme('') # PySimpleGUI theme selector

layout = [ # PySimpleGUI layout attrib var
[sg.Button('Up'), sg.Button('Down'), sg.Button('Left'), sg.Button('Right')], # PySimpleGUI button function attrib var
[sg.Button('Quiet Title'), sg.Button('Filing'),sg.Button('Submit'), sg.Button('US Code 18 U.S.C. 2520b'), sg.Button('US Code 18 U.S.C. 2521'), sg.Button('US Code 18 U.S.C. 3663'), sg.Button('Exit')], # PySimpleGUI button function attrib var
[sg.Button('Greetings'), sg.Button('Congratulations'), sg.Button('Obstacle Hit'), sg.Button('Try Again'), sg.Button('Thanks')], # PySimpleGUI button function attrib var
[sg.Text(size=(86,), auto_size_text=(), key='-OUTPUT-')] # PySimpleGUI text output in GUI
]

window = sg.Window("LILLY PAD LLC - NICHOLAS M JAMES SOLE MBR", layout) #PySimpleGUI window with title and layout function



while True: # loop statment 
    event, values = window.read() # multi var for window
    print(event, values) # print statement for var 
    if event == sg.WIN_CLOSED or event == 'Exit': # if statement for user input var   
        break # break loop
    if event == 'Greetings': # if statment for event greetings
         messageGreeting = 'Welcome to the Pond, Ribbet Ribbet' # var attrib for greeting
         window['-OUTPUT-'].update(messageGreeting) # update function for window with messageGreeting 
         print(messageGreeting) # print statment for greeting 
    if event == 'Congratulations': # if statement for event congratulations
        messageCongratulations = "You have successfully eaten the fly" # var attrib for congratulations 
        window['-OUTPUT-'].update(messageCongratulations) # update function for window with congratulations
        print(messageCongratulations) # print for congratulations
    if event == 'Obstacle Hit': # if statment for event obstacle
        messageObstacleHit = "Try Again" # var attrib for obstacle
        window['-OUTPUT-'].update(messageObstacleHit) # update function for window with obstacle hit
        print(messageObstacleHit) # print statment for obstacle hit
    if event == 'Try Again': # if statment for event try again
        messagePlayAgain = "Trying again" # var attrib for Play again
        window['-OUTPUT-'].update(messagePlayAgain) # update function for window with try again
        print(messagePlayAgain) # print statment for message Playagain
    if event == 'Thanks': # if statment for event thanks
        messageThanks = f"Thanks You {Name}" # var attrib for Thanks
        window['-OUTPUT-'].update(messageThanks) # update function for window with Thanks
        print(messageThanks) # print statment for message thanks
        
    if event == 'Assignment Title': # if statment for event assignment title
        messageTitle = Name, SchoolName, SchoolId # var attrib for assignment title
        window['-OUTPUT-'].update(messageTitle) # update function for window with messageTitle
        print(messageTitle) # print statment for messageTitle

    if event == 'Quiet Title': # if statment for event quiet title
        quietTitle = Name, BusinessName, BusinessOwner, SchoolId # var attrib for message title
        window['-OUTPUT-'].update(quietTitle) # update function for window with quiet title
        print(quietTitle) # print message for message 
    
    if event == 'US Code 18 U.S.C. 2521':  # if statment for event 18 US Code 18 U.S.C 2521
        messageusCode2521 = {'18 U.S.C. 2521'} # var attrib for assignment title
        Reasons = 'Human Rights Violations, Cyberbullying, Use of Deepfakes, Gaslighting, Impersonation, Defamation, Harassment, Loss of Reputation, Coercion, Loss of Autonomy, Lack of Response from Local Authorities Aware of Threats,  Malicious Prosecution'
        window['-OUTPUT-'].update(messageusCode2521) # update function for window with US Code 18 U.S.C. 2521
        webbrowser.open("https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title18-section2521&num=0&edition=prelim")
        print(messageusCode2521,"Reasons:",Reasons) # print statement for reasons and US Code 18 U.S.C. 2521
        print("https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title18-section2521&num=0&edition=prelim") # open link webpage function to US Code 18 U.S.C. 2521

    if event == 'US Code 18 U.S.C. 2520b':  # if statment for event US Code 18 U.S.C. 2520b
        messageusCode2520 = {'18 U.S.C. 2520c'} # var attrib for assignment title
        window['-OUTPUT-'].update(messageusCode2520) # update function for window with US Code 18 U.S.C. 2520b
        webbrowser.open('https://uscode.house.gov/view.xhtml?req=granuleid:USC-2000-title18-section2520&num=0&edition=2000') # var for open link webpage function to US Code 18 U.S.C 2520b
        print(messageusCode2520) # print statment for US Code 18 U.S.C. 
        print("https://uscode.house.gov/view.xhtml?req=granuleid:USC-2000-title18-section2520&num=0&edition=2000") # print function in console for US Code 18 U.S.C. 2520b
    
    if event == 'US Code 18 U.S.C. 3663':  # if statment for event US Code 18 U.S.C. 3663
        messageusCode3663 = {'18 U.S.C. 3663'} # var attrib for assignment title
        window['-OUTPUT-'].update(messageusCode3663) # update function for window with US U.S.C. 3663
        webbrowser.open("https://uscode.house.gov/view.xhtml?hl=false&edition=prelim&req=granuleid%3AUSC-prelim-title18-section3663&num=0&saved=%7CZ3JhbnVsZWlkOlVTQy1wcmVsaW0tdGl0bGUxOC1zZWN0aW9uMzY2M0E%3D%7C%7C%7C0%7Cfalse%7Cprelim")
        print(messageusCode3663) # print message for US Code 18 U.S.C. 3663
        print("https://uscode.house.gov/view.xhtml?hl=false&edition=prelim&req=granuleid%3AUSC-prelim-title18-section3663&num=0&saved=%7CZ3JhbnVsZWlkOlVTQy1wcmVsaW0tdGl0bGUxOC1zZWN0aW9uMzY2M0E%3D%7C%7C%7C0%7Cfalse%7Cprelim") # print statement for US Code 18 U.S.C. 3663
    
    if event == "Filing":  # if statment for event Filing
        messageFiling = {'18 U.S.C. 3663', '18 U.S.C. 2520c', '18 U.S.C. 2521'} # var attrib for Filing
        window['-OUTPUT-'].update(messageFiling) # update function for window with Filing
        print("On Behalf Of", Name, BusinessName, BusinessOwner) # print statement for messageFiling
    
    if event == 'Submit': # if statment for event Submit
        window['-OUTPUT-'].update("Submission of Filing Successful") # update function for window with Submit
        print("Submission of Filing Successful") # Print statement in console for submit

    if event == ['Down','Up','Left','Right']: # if statment for event Button Up, Down, Left, Right 
        window['-OUTPUT-'].update("") # update function for window with event Up, Down, Left, Right
        print(event) 
        
class Frog:
    def __init__(self,width,height, position): # def of object
        self.width # var attrib for width
        self.height # var attrib for height
        self.position # var attrib for position

    def printinfo(self): # def of printinfo
        print(f"{self.width},{self.height},{self}") # print statement of object

print(Name, SchoolName, CourseName, SchoolId) # print statement in console for Name, SchoolName, CourseName, SchoolId
print("On Behalf Of", Name,"(c)2024",BusinessName,"(R)", BusinessOwner, "cite US Code", messageusCode2521, messageusCode2520, "and File", messageusCode3663) # print statement in console for Name US Code 18 U.S.C. 3663, 2521, 2520b
print("On Behalf Of", Name), messageusCode2520 # print statement in console for US Code 18 U.S.C. 2520
exit( )



# [sg.Graph.draw_image('-IMAGE-')] ### PySimpleGUI graph function attrib for later incorporation of images
# sg.Image('Picture Down',image_filename="E:\University Of Advancing Technology\UAT-CSC235-Week5\Assignments\Final Project\down.jpg", key='-IMAGE-')], ### PySimpleGUI image_path function attrib for later use of images
# [sg.Image('Picture Left',image_filename="E:\University Of Advancing Technology\UAT-CSC235-Week5\Assignments\Final Project\left.jpg", key='-IMAGE-'), sg.Image('Picture Right', image_filename="E:\University Of Advancing Technology\UAT-CSC235-Week5\Assignments\Final Project\right.jpg", key='-IMAGE-')] ### PySimpleGUI image_path function attrib

# x1, y1 = 100, 350
# sg.Graph.draw_image(filename='up.gif', location=(0, 100)),
# sg.Graph.draw_image(filename='down.gif', location=(0, 100)),
# # left = sg.Graph(draw_image(filename='left.gif', location=(0, 100))),
# # right = sg.Graph(draw_image(filename='right.gif', location=(0, 100))),
# sg.Graph.draw_image(filename='lovedfrogprince.jpg', location=(0, 100))
# # fly = sg.Graph(draw_image(filename='fly.jpg', location=(0, 100))),
# # obstacle = sg.Graph(draw_image(filename='rubixobstacle.jpg', location=(0, 100)))

# print("Did you")
# print("How much did you receive from me")
# print("How much did you give back to me")
# print("Would you do it again")
# print("Come back soon")

# ifwereYouHonestAboutCommunicatingDirectly = print('$9,270,860.00' + "crypto" + Owner, Business, SchoolId)