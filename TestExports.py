##############
#Created by Josh Kowal, 3 Jan. 2020

#This is a helper function to export your project. 
#Check your downloads folder for the JSON output.
##############

from labelbox import Client
from LabelboxConstants import API_KEY
import webbrowser

def project_to_json(project_name, platform):
    '''
    Fetches project_name's labels and saves them to your downloads folder
    platform is the type of platform (Windows, Mac, Linux) on which your computer runs
    '''
    client = Client(API_KEY)
    condition = False
    for project in client.get_projects():
        #print(project.name, project.uid)
        if project.name == project_name:
            #We have identified the correct project
            print('Found', project_name)
            condition = True
            break
    
    if not condition:
        raise ValueError('You do not have ' + project_name + 'in your Labelbox project list. Please check the name carefully.')

    url = project.export_labels()
    
    if comp_type == 'Mac':
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s' #For Mac users
    elif comp_type == 'Windows:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' #For Windows users
    else:
        chrome_path = '/usr/bin/google-chrome %s' #For Linux users
    
    webbrowser.get(chrome_path).open(url)