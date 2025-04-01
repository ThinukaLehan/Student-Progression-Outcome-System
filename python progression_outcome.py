# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w2052786
# Date: 10/12/2023

#Importing Modules
from graphics import *

#Initiating some variables, lists and dictioneries
credits = [0, 20, 40, 60, 80, 100, 120]
creditlevel = {'pass': 0, 'defer': 0, 'fail':0}
temp_inputlist = ["level", 0, 0, 0]
inputlist = []
user = " "
progress = 0
trailer = 0
exclude = 0
retriever = 0

#Getting Inputs from User
def get_inputs():
    print("")
    while True:
        for level in creditlevel:
            while True:
                try:
                    credit_input = int(input(f"Please enter your credits at {level} :"))
                    if credit_input in credits:
                        creditlevel[level] = credit_input
                        break
                    else:
                        print("Out of Range")
                        continue
                except ValueError:
                    print("Integer Required")
        total = creditlevel['pass'] + creditlevel['defer'] + creditlevel['fail']
        if total != 120:
            print("Total incorrect")
        else:
            break

#Checking the Progression outcome
def outcome():
    global progress
    global trailer
    global exclude
    global retriever
    global temp_inputlist
    if creditlevel['pass'] == 120:
        progress += + 1
        temp_inputlist[0] = "Progress"
        print("Progress")
    elif creditlevel['pass'] == 100:
        trailer += 1
        temp_inputlist[0] = "Progress (Module Trailer)"
        print("Progress (module trailer)")
    elif creditlevel['pass'] + creditlevel['defer'] <= 40:
        exclude += 1
        temp_inputlist[0] = "Exclude"
        print("Exclude")
    else:
        retriever += 1
        temp_inputlist[0] = "Module Retriever"
        print("Module Retriever")

#Saving the Inputs into lists.
def saveinputs():
    temp_inputlist[1] = creditlevel['pass']
    temp_inputlist[2] = creditlevel['defer']
    temp_inputlist[3] = creditlevel['fail']
    inputlist.append(temp_inputlist.copy())

#Printing the saved Inputs
def printinputs():
    print("="*65,"\n\nPart 2:")
    for j in range (len(inputlist)):
        print(str(inputlist[j][0]) + " - " + str(inputlist[j][1]) + ", " + str(inputlist[j][2]) + ", " + str(inputlist[j][3]))
    print("")

#Checking the User
def usertype():
    global user
    user = input(("Are you a Student or Staff Member (student/staff) :"))
    user = user.lower()
    print("="*65)

#Creating the Histrogram
def histogram():
    win = GraphWin("Histogram", 450, 500)
    win.setBackground('Mint Cream')
    win.setCoords(0, -5, 45, 45)
    title = Text(Point(22.5,43), "Histogram Results")
    title.setSize(14)
    title.draw(win)
    ln = Line(Point(3,0), Point(42,0))
    ln.draw(win)
    xlabels = ['Progress','Trailer','Retriever','Excluded']
    colours = ["green", "yellow", "orange", "red"]
    yvalues = [progress, trailer, retriever, exclude]
    xpoint = [9, 18, 27, 36]
    x_left = [5, 14, 23, 32]
    x_right = [13, 22, 31, 40]
    tot_values = yvalues[0] + yvalues[1] + yvalues[2] + yvalues[3]
    for i in range(4):
        rec = Rectangle(Point(x_left[i],0), Point(x_right[i], yvalues[i]))
        rec.setFill(colours[i])
        lable = Text(Point(xpoint[i],-1),xlabels[i])
        lable.setSize(11)
        value = Text(Point(xpoint[i], yvalues[i]+1), yvalues[i])
        rec.draw(win)
        value.draw(win)
        lable.draw(win)
    totvalues = Text(Point(22.5, -4), str(tot_values) + " outcomes in Total")
    totvalues.draw(win)
    try:
        win.getMouse()
    except GraphicsError:
        win.close()

#Writting the output in the text file.
def write_textfile():
    file = open('CWText.txt', 'w')
    file.write("Part 3:" + "\n")
    for j in range (len(inputlist)):
        file.write(str(inputlist[j][0]) + " - " + str(inputlist[j][1]) + ", " + str(inputlist[j][2]) + ", " + str(inputlist[j][3]) + "\n")
    file.close()

#Reading the textfile
def read_textfile():
    file = open('CWText.txt','r')
    for data in file:
        print(data, end='')
    file.close()
    print("\n" + "="*65)

#Main Program
usertype()
if user == 'student':
    get_inputs()
    outcome()
    print("Thank You!")
elif user == 'staff':
    re_enter = 'y'
    get_inputs()
    outcome()
    saveinputs()
    while True:
        print("-"*65)
        re_enter = str(input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results :"))
        re_enter = re_enter.lower()
        if re_enter == 'y':
            get_inputs()
            outcome()
            saveinputs()
        elif re_enter == 'q':
            histogram()
            printinputs()
            write_textfile()
            read_textfile()
            print("Thank You!")
            break
        else:
            print("Please Enter 'y' or 'q'")
else:
    print("Invalid User Type\nPlease Try Again...")