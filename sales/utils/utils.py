import yaml
import os

def read_yaml_file(file_path):
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise(e)


""" def write_yaml_file(file_path,data):
    os.makedirs(os.path.dirname(file_path),exist_ok=True)
    with open(file_path,'w') as yaml_file:
        if data is not None:
         yaml.dump(data,yaml_file) """

def write_yaml_file(file_path:str,data:dict=None):
    """ 
    It will create yaml file
    file_path : str
    data : dict
    
    """
    
    os.makedirs(os.path.dirname(file_path),exist_ok=True)
    with open(file_path,'w') as yaml_file:
        if data is not None:
            yaml.dump(data,yaml_file)