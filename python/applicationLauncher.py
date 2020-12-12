import os
#importing os library


applications=[["firefox","browser","internet"],["wmplayer","windows media player","player","media player"],["notepad","editor","text editor","writer"]]
#application list used to store name of applications
#we can add more application names in this list as required


word=["not","not launch","not run","not open","not execute","do not launch","do not run","do not open","do not execute"]
#word store prefix text which are used in case "not to launch the application"


flag=0
while (True):
    #while infinite loop 
    if flag==1:
        print("application not launched enter another input")       #print this statement when user is saying not to launch the application
    flag=0

    user_input=input("Please enter the name of application to launch or enter exit if you want to quit\n")
    #asking user to input the text


    if ("exit" in user_input or "quit" in user_input ) and not("not exit" in user_input or "not quit" in user_input) and not(" do not exit" in user_input or " do not quit" in user_input):
        break
    #if statement used in case user want to exit the application

    
    for names in applications:
        #loop to check the appliation name in user entered text


        for text in names:
            #loop to check the possible names user can enter for an application


            if text in user_input:
                #if check the condition in the application name is in the text


                flag=0
                #flag will be equal to 1 in case user input not or negative statement like "do not launch notepad"

                
                for prefix in word:
                    #loop to check negative statements possibility

                    
                    if prefix + " " + text in user_input:
                        flag=1
                        #flag will be set 1 in case user dont want to launch the aplication

                        
                if flag==0:
                    os.system(names[0])
                    break
                #if flag will be 0 launch the application and break the inner loop
				 
