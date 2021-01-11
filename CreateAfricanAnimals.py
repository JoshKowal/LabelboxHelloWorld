import CreateProject
from CreateProject import create_project_with_dataset

proj_name = 'African Animals'
data_name = 'Animals Subset'
filepath = '<your_path_here>/AfricanAnimalsSubset/*/*.jpg'

create_project_with_dataset(proj_name, data_name, filepath)