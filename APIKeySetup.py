import requests
import os
from appJar import gui

app = gui("Regulations-BOINC")


def sendErrorMessage(errorCode, errorMessage=0):
    '''
    Sends an error message to the user.
    :param errorCode: Error code to be displayed.
    :param errorMessage: An integer, either 0 or 1, specifying which message should be displayed after the error; 0 for "Please try again later" and 1 for "Are you connected to the internet?. Defaults to 0"
    :return:
    '''

    app.startSubWindow("errorWindow", "Error")

    app.top = True
    app.resizable = False
    app.font = {'size': 18, 'family': 'Gill Sans'}

    app.padding = (10, 8)
    app.guiPadding = (10, 30)

    app.addLabel("errorCode", "Error: " + str(errorCode))
    if errorMessage == 0:
        app.addLabel("errorMessage", "Please try again later.")
    else:
        app.addLabel("errorMessage", "Are you connected to the internet?")

    def exit(buttonName):
        app.hideSubWindow("errorWindow")

    app.addButton("   Okay   ", exit)

    app.stopSubWindow()
    app.showSubWindow("errorWindow")


def sendInvalidKeyMessage():
    '''
    Sends a message informing the user that the key they entered is invalid, and providing them with
    a link to help them get one.
    :return:
    '''

    app.startSubWindow("invalidKeyWindow", "Error")

    app.top = True
    app.resizable = False
    app.font = {'size': 18, 'family': 'Gill Sans'}

    app.padding = (50, 2)

    app.addLabel("errorCode", "Invalid API Key!")
    app.addLabel("errorMessage", "Please visit:")
    app.link("regulations.gov", "https://regulationsgov.github.io/developers/")
    app.addLabel("errorMessageTwo", "for an API Key.")

    def exit(buttonName):
        app.hideSubWindow("invalidKeyWindow")

    app.addButton("   Okay   ", exit)

    app.stopSubWindow()

    app.showSubWindow("invalidKeyWindow")


def sendSuccessMessage():
    '''
    Final message, to be displayed if/when everything finishes correctly.
    :return:
    '''

    app.startSubWindow("successWindow", "Error")

    app.top = True
    app.resizable = False
    app.font = {'size': 18, 'family': 'Gill Sans'}

    app.padding = (50, 2)

    app.addLabel("successMessage", "Successfully stored API Key!")

    def exit(buttonName):
        app.hideSubWindow("successWindow")
        app.stop()

    app.addNamedButton("   Okay   ", "doneButton", exit)

    app.stopSubWindow()

    app.showSubWindow("successWindow")


def writeAPIKey(key):
    '''
    Writes the user's API Key to ~/.env/regulationskey.txt
    :param key: APIKey to be written to the file.
    :return:
    '''


    fileDirectory = os.getenv("HOME") + "/.env"

    if not os.path.exists(fileDirectory):
        os.makedirs(fileDirectory)

    f = open(fileDirectory + "/regulationskey.txt", "w")
    f.write(key)
    f.close()



#Below code builds the main window
submitName = "   Submit   "
cancelName = "   Cancel   "

app.top = True
app.resizable = False
app.font = {'size':18, 'family':'Gill Sans'}

app.padding = (10,8)
app.guiPadding = (10,30)

app.addLabel("header","Please enter your regulations.gov API Key.")

app.addLabelEntry("APIKey")


# Called when a button is pressed
def press(buttonName):

    if buttonName == cancelName:
        app.stop()
    elif buttonName == submitName:
        apiKey = app.getEntry("APIKey")

        try:
            r = requests.get("https://api.data.gov/regulations/v3/documents.json?api_key=" + apiKey)
        except requests.ConnectionError:
            sendErrorMessage("Could not connect to server!", 1)
            return

        # Anything 300 & above is an error, but 429 is the error for a key that's run out of requests
        # and 403 is the error for an invalid key
        if r.status_code > 299 and r.status_code != 429:

            if r.status_code == 403:

                sendInvalidKeyMessage()

            else:

                sendErrorMessage(r.status_code)

        else:

            writeAPIKey(apiKey)
            
            sendSuccessMessage()



app.addButtons([submitName, cancelName], press)

app.go()
