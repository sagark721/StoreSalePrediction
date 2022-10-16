import yaml

def read_yaml_file(file_path):

    with open(file_path,'rb') as yaml_file:
        return yaml.safe_load(yaml_file)
