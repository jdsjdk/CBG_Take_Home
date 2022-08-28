'''
Author: Jess Summerhill
Project: This is a take home quiz for a job interview with CBG.
Date: 8-26-2022
'''


from cgi import print_arguments
import sys 
import pandas as pd
from pandas import DataFrame as pd_df
from typing import List as lst
from pathlib import Path as fp

class CleanDupsCVS:
    
    # generic constructor
    def __init__(self) -> None:
        pass     

    def main() -> int:
        
         # get the in path, return the csv files list
        def get_path_files() -> lst[str]:
            
            csv_list = []
            in_path = fp().cwd()  / "in/"
            files = in_path.rglob("*.csv")
            
            for file in files: 
                csv_list.append(in_path / file.name)
            
            return csv_list
        
        '''
        Take in all of the CSV file locations
        Put them in a DataFrame list
        Clean up the data in each DataFrame
        Return the new cleaned up DataFrames.
        '''
        def clean_up_data(data_list: lst[str]) -> lst[pd_df]:
            
            dfclean_list = []
            df_list = [pd.read_csv(f) for f in data_list]
            
            # print(f"Before: \n {df_list[1]} \n") 
            
            for idx, idf in enumerate(df_list):
                match idx:
                    case 0:
                        # Follow instructions for the 'ballotmapper.csv' file
                        dfclean_list.append("Hello")
                        
                    case 1:
                        # Follow instructions for the 'choices.csv' file
                        dfclean_list.append(idf.drop_duplicates(subset=['ContestID']))
                        #pass
                    case 2:
                        # Follow instructions for the 'contests.csv' file
                        dfclean_list.append(idf.drop_duplicates(subset=['ContestName']))
                        
            # print(f"\n After: \n {dfclean_list[1]}")
            
            return dfclean_list
        
                
        path_csvs = get_path_files()
        clean_up_data(path_csvs)
        
        sys.exit(0)        

    if __name__ == "__main__":
        main()
                
clean_dup = CleanDupsCVS()