from dotenv import load_dotenv
import os
from pathlib import Path
from src.paths import PARENT_DIR

# Ensure PARENT_DIR is a Path object, not a string
parent_dir_path = Path(PARENT_DIR)

# Load environment variables from .env file
# Make sure the path is constructed correctly
dotenv_path = parent_dir_path / '.env'
load_dotenv(dotenv_path)

# Access API key with error handling
HOPSWORKS_API_KEY= os.getenv('HOPSWORKS_API_KEY')
HOPSWORKS_PROJECT_NAME = "taxi_demand_jithis"

FEATURE_GROUP_NAME = 'time_series_hourly_feature_group'
FEATURE_GROUP_VERSION = 1