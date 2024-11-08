import os 

## Configuration
class MyConfig:
    pass 

MY_CONFIG = MyConfig ()

## Crawl settings
MY_CONFIG.CRAWL_URL_BASE = 'https://thealliance.ai/'
# MY_CONFIG.CRAWL_URL_BASE = 'https://thealliance.ai/our-work'
MY_CONFIG.CRAWL_MAX_DOWNLOADS = 10
MY_CONFIG.CRAWL_MAX_DEPTH = 2
MY_CONFIG.CRAWL_MIME_TYPE = 'text/html'

## Input Data - configure this to the folder we want to process
MY_CONFIG.INPUT_DIR = "input"
MY_CONFIG.OUTPUT_DIR = "output"
MY_CONFIG.OUTPUT_DIR_FINAL = os.path.join(MY_CONFIG.OUTPUT_DIR , "output_final")
### -------------------------------
