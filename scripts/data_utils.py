import gdown
import os
import pandas as pd
import pickle

def load_dataframe_from_pickle(file_id, output):
  """
  Loads a DataFrame from a pickle file in Google Drive.
  
  Args:
  - file_id (str): The ID of the file in Google Drive.
  - output (str): Name of the local file to save.
  
  Returns:
  - pd.DataFrame: The DataFrame loaded from the pickle file, or None if an error occurred.
  """
  # Define the full URL for the pickle file
  url = f'https://drive.google.com/uc?id={file_id}'
  
  # Download the file if it doesn't exist locally
  if not os.path.isfile(output):
      print(f"File not found locally. Downloading {output}...")
      try:
          # Download the file
          gdown.download(url, output, quiet=False)
      except Exception as e:
          print(f"Error downloading the file: {e}")
          return None
  else:
      print(f"File {output} already exists. Skipping download.")
  
  # Load the pickle file
  try:
      with open(output, 'rb') as f:
          df = pickle.load(f)
      return df
  except Exception as e:
      print(f"Error loading the pickle file: {e}")
      return None

def load_demographic_data():
  """
  Loads demographic_data from g_drive
  """
  file_id = '1noQW_s9RvEhhrQvxZckXpzbbel975zFm'
  output = 'demographic_data.pkl'
  return load_dataframe_from_pickle(file_id, output)