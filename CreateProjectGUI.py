from labelbox import Client
from LabelboxConstants import API_KEY
import wx
import os

def create_project_in_labelbox(proj_name, data_name, files):
    '''
    Inputs:
    proj_name - String representing the name of the project
    data_name - String representing the name of the dataset
    files - List of strings representing a list of filenames
    
    Returns:
    Nothing. Instead, this function creates the given project in Labelbox.
    '''
    client = Client(API_KEY)
    project = client.create_project(name = proj_name)
    dataset = client.create_dataset(name = data_name, projects = project)
    
    task = dataset.create_data_rows(files)
    task.wait_till_done()
    
    
class Interface(wx.Frame):
    def __init__(self, parent, title):
        super(Interface, self).__init__(parent, title=title, size=(500, 500))

        # Show the window on screen
        self.filepaths = []
        self.setup()
        self.Show()

    def setup(self):
        '''
        Sets up the window for the user to input data
        '''
        #Create the text boxes for our project name and dataset name
        self.project_text = wx.StaticText(self, label = 'Project Name', pos = wx.Point(5,15))
        self.dataset_text = wx.StaticText(self, label = 'Dataset Name', pos = wx.Point(5,45))
        self.textbox_project = wx.TextCtrl(self, pos = wx.Point(100,10), size = wx.Size(150,25))
        self.textbox_dataset = wx.TextCtrl(self, pos = wx.Point(100,40), size = wx.Size(150,25))
        
        #Create the buttons and windows to upload, delete, and view files
        self.upload_button = wx.Button(self, label = 'Upload Files', pos = wx.Point(5,75))
        self.delete_button = wx.Button(self, label = 'Delete Selected Files', pos = wx.Point(100,75))
        self.delete_all_button = wx.Button(self, label = 'Delete All Files', pos = wx.Point(250,75))
        self.file_list = wx.ListCtrl(self, style=wx.LC_REPORT|wx.BORDER_SUNKEN, pos = wx.Point(5,100), size = wx.Size(450,300))
        self.file_list.InsertColumn(0, 'Filename')
        self.upload_button.Bind(wx.EVT_BUTTON, self.upload_files)
        self.delete_button.Bind(wx.EVT_BUTTON, self.delete_files)
        self.delete_all_button.Bind(wx.EVT_BUTTON, self.delete_all)
        
        #Lastly, set up our "Create Project" button
        self.create_project_button = wx.Button(self, label = 'Create Project', size = wx.Size(200,50), pos = wx.Point(150,400))
        self.create_project_button.Bind(wx.EVT_BUTTON, self.create_project)
    
    def upload_files(self, event):
        wildcard = "PNG files (*.png)|*.png|JPG files (*.jpg)|*.jpg|JPEG files (*.jpeg)|*.jpg"
        with wx.FileDialog(self, 'Open Photos', wildcard = wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            pathnames = fileDialog.GetPaths()
            self.update_display([os.path.abspath(path) for path in pathnames])
    
    def delete_files(self, event):
        length = self.file_list.GetItemCount()
        if length == 0:
            resp = wx.MessageBox('There are no files to delete', 'Error',
                                     wx.OK)
            return
        selected = []
        for i in range(length):
            if not self.file_list.IsSelected(i):
                selected.append(self.file_list.GetItemText(i))
        if len(selected) == length:
            resp = wx.MessageBox('You haven\'t selected any files to delete', 'Error',
                                     wx.OK)
            return
        
        self.clear()
        self.update_display(selected)
    
    def delete_all(self, event):
        if self.file_list.GetItemCount() == 0:
            resp = wx.MessageBox('There are no files to delete', 'Error',
                                     wx.OK)
            return
        self.clear()
    
    def clear(self):
        self.filepaths = []
        self.file_list.DeleteAllItems()
    
    def update_display(self, paths):
        for index, path in enumerate(paths):
            self.filepaths.append(path)
            self.file_list.InsertItem(index, path)
    
    def create_project(self, event):
        self.project = self.textbox_project.GetValue()
        self.dataset = self.textbox_dataset.GetValue()
        
        if self.project and self.dataset and self.filepaths:
            try:
                create_project_in_labelbox(self.project, self.dataset, self.filepaths)
                resp = wx.MessageBox('Your project was successfully created in Labelbox! Log in to set up your ontology!', 'Success!', wx.OK)
                self.Destroy()
            except:
                resp = wx.MessageBox('Hmm, an error was encountered while setting up your project. Try again.', 'Error', wx.OK)
        else:
            resp = wx.MessageBox('You must input a project name, a dataset name, and at least one file to upload.', 'Error',
                                     wx.OK)

if __name__ == '__main__':
    # Create the application object
    app = wx.App()
    Interface(None, title='Labelbox Project Creator')
    app.MainLoop()