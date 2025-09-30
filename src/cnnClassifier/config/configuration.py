from cnnClassifier.constant import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig, PrepareModelConfig

class Configuration_Manager:
    def __init__(
        self, 
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])
        
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir, 
            source_URL = config.source_URL,
            local_data_files = config.local_data_files,
            unzip_dir = config.unzip_dir
        )
        
        return data_ingestion_config
    
    
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])
        
        
    def get_prepare_base_model_config(self) -> PrepareModelConfig:
        config = self.config.prepare_base_model
        params = self.params
        
        create_directories([config.root_dir])
        
        prepare_model_config = PrepareModelConfig(
            root_dir = config.root_dir,
            base_model_path = config.base_model_path,
            updated_base_model_path = config.updated_base_model_path,
            params_image_size = params.IMAGE_SIZE,
            params_include_top = params.INCLUDE_TOP,
            params_learning_rate = params.LEARNING_RATE,
            params_classes = params.CLASSES,
            params_weights = params.WEIGHTS
        )
        
        return prepare_model_config