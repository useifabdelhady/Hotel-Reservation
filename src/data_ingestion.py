import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config):
        self.config = config["data_ingestion"]
        self.raw_file_name = self.config["raw_file_name"]
        self.train_test_ratio = self.config["train_ratio"]

        # Create artifacts/raw directory if it doesn't exist
        os.makedirs(RAW_DIR, exist_ok=True)
        
        # Set the path to the local raw.csv file
        self.local_raw_file_path = os.path.join(RAW_DIR, self.raw_file_name)

        logger.info(f"Data Ingestion started with local file: {self.local_raw_file_path}")

    def validate_local_data(self):
        """Validate that the local raw.csv file exists"""
        try:
            if not os.path.exists(self.local_raw_file_path):
                raise FileNotFoundError(f"Raw data file not found at {self.local_raw_file_path}")
            
            # Verify the file is readable
            pd.read_csv(self.local_raw_file_path, nrows=1)
            logger.info(f"Local raw data file validated at {self.local_raw_file_path}")
            
        except Exception as e:
            logger.error(f"Error validating local data file: {e}")
            raise CustomException("Failed to validate local raw data file", e)
        
    def split_data(self):
        try:
            logger.info("Starting the splitting process")
            data = pd.read_csv(self.local_raw_file_path)
            
            logger.info(f"Loaded data with shape: {data.shape}")
            
            train_data, test_data = train_test_split(
                data, 
                test_size=1-self.train_test_ratio, 
                random_state=42
            )

            # Save train and test data to the same artifacts/raw folder
            train_file_path = os.path.join(RAW_DIR, "train.csv")
            test_file_path = os.path.join(RAW_DIR, "test.csv")
            
            train_data.to_csv(train_file_path, index=False)
            test_data.to_csv(test_file_path, index=False)

            logger.info(f"Train data saved to {train_file_path} with shape: {train_data.shape}")
            logger.info(f"Test data saved to {test_file_path} with shape: {test_data.shape}")
        
        except Exception as e:
            logger.error("Error while splitting data")
            raise CustomException("Failed to split data into training and test sets", e)
        
    def run(self):
        try:
            logger.info("Starting local data ingestion process")

            # Validate that local raw data exists
            self.validate_local_data()
            
            # Split the local data into train and test sets
            self.split_data()

            logger.info("Local data ingestion completed successfully")
        
        except CustomException as ce:
            logger.error(f"CustomException: {str(ce)}")
            raise ce
        
        except Exception as e:
            logger.error(f"Unexpected error during data ingestion: {e}")
            raise CustomException("Data ingestion failed", e)
        
        finally:
            logger.info("Data ingestion process finished")

if __name__ == "__main__":
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()