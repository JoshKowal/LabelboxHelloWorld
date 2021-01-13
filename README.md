# LabelboxHelloWorld

This repository reflects the first real labelling project I did with Labelbox. Follow the below steps to create your project.
Note: You must create a Labelbox account before you do this project. Creating an account is free and easy to do.

## Initial Setup Steps:

1. Make sure you've ran ``pip3 install labelbox`` or ``pip install labelbox`` on your computer or in a virtual environment.
2. Navigate to where you cloned the repository.
3. Create an API Key in Labelbox by navigating to ``LabelboxConstants.py`` and follow the link. Replace ``<your_api_key_here>`` with your API key.
4. In ``CreateAfricananimals.py``, find the ``filepath`` variable and replace ``<your_path_here>`` with the path leading to the ``AfricanAnimalsSubset`` folder.

## To Create Your Project:

1. Run ``CreateAfricananimals.py``
2. Make sure you see the message, "Check for project and photos!"
3. Log into Labelbox and verify your project is there.
4. To finish setting up your project, click on the project you created. Next, click "Next" for both circles 1 and 2, and you can configure your ontology.
5. You're ready to start labelling!

## To Export Your Labels:

1. In ``GetExports.py``, uncomment whichever line calls ``project_to_json`` with the name of your platform.
2. Run ``GetExports.py``.
3. Check your downloads folder for the output JSON file.

## To Use the GUI (``CreateProjectGUI.py``)

1. Run ``python3 CreateProjectGUI.py`` in your local terminal.
2. Fill in a project name, dataset name, and attach multiple image files.
3. Press the "Create Project" button. Your project should be there when you log on to Labelbox.
4. Create your ontology on Labelbox, as above, and you can start labelling after!

*Note: This GUI currently only supports project creation for projects with image files. Video and text files are not yet supported as of 12 January 2021.
