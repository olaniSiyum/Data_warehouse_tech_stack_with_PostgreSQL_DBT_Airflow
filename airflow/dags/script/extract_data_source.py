import pandas as pd

def get_data(**kwargs):
    # Define the path to your CSV file
    csv_path = '/home/olani/Downloads/20181024_d1_0830_0900.csv'

    # Read the CSV file using pandas
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_path,header=None, names=['data'])
        
        # You can perform additional data preprocessing steps here if needed
         # Split the single column into multiple columns based on semicolon separator
        df = df['data'].str.split(';', expand=True)
        
        # Optional: Assign meaningful column names to the new columns
        #df.columns = ['Attribute_1', 'Attribute_2', 'Attribute_3', 'Attribute_4', 'Attribute_5',
         #             'Attribute_6', 'Attribute_7', 'Attribute_8', 'Attribute_9', 'Attribute_10']
        
        # Perform any additional preprocessing steps here
        
        # Return the preprocessed DataFrame
        return df
        
        # Return the DataFrame
        return df
        
    except Exception as e:
        # Handle exceptions if any
        print(f"An error occurred while reading the CSV file: {e}")
        return None