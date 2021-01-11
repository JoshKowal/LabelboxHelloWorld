##############
#Created by Josh Kowal, 3 Jan. 2020

#This is a helper function to create a project with a dataset. 
#Make sure the data is in your current directory.
##############

from labelbox import Client
from LabelboxConstants import API_KEY
import glob

def create_project_with_dataset(proj_name, data_name, filepath):
    '''
    Inputs:
    proj_name - The name of the new project
    data_name - The name of the new dataset
    filepath - The file path to the dataset
    
    Returns:
    Nothing. Instead, it prints the below message if the operation was a success.
    '''
    client = Client(API_KEY)
    project = client.create_project(name = proj_name)
    dataset = client.create_dataset(name = data_name, projects = project)
    
    rows = glob.glob(filepath)
    task = dataset.create_data_rows(rows)
    task.wait_till_done()
    print('Check for project and photos!')