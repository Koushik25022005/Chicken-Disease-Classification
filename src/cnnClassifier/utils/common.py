import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import pathlib
import joblib
from typeguard import typechecked
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
import unittest


@typechecked
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file and returns
    
    Args:
    path_to_yaml (str): path like input
    
    Raises:
    ValueError: If the file does not exist or is not a yaml file.
    e : empty file error
    
    Returns:
    ConfigBox: ConfigBox type"""
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    
    
    
@typechecked
def create_directories(path_to_directories: list, verbose=True):
    """ creates list of directories
    
    Args:
    path_to_directories (list): list of path of directorries
    ignore_log (bool, optional): ignore if mulitple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created Directory: {path}")
            
            
            
@ typechecked
def save_json(path: Path, data: dict):
    """Saves json data
    
    Args:
    Path (Path): path to json file
    data (dict): data to be saved in json file"""
    
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"json file saved at: {path}")
    
    
    
@typechecked
def load_bin(path: Path) -> Any:
    """ loads binary file
    
    Args:
    path (Path): path to binary file
    
    Returns:
    Any: object stored in file"""
    
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@typechecked
def save_bin(data: Any, path: Path):
    """Saves binary filw
    
    Args:
    data (Any): data to be saved as binary
    path (Path): path to binary file
    """
    
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@typechecked
def get_size(path: Path) -> Any:
    """get size in kB
    
    Args:
    path (Path): path of the file
    
    Returns:
    str: size in kB"""
    
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"{size_in_kb} KB"

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()
        
        
def encodeImageIntBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())