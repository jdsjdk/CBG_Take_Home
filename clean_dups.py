'''
Author: Jess Summerhill
Project: This is a take home quiz for a job interview with CBG.
Date: 8-26-2022
'''



import sys 
import pandas as pd
from pathlib import Path as fp
from pandas import DataFrame as pd_df

class CleanDupsCVS:
    
    # generic constructor
    def __init__(self) -> None:
        pass     

    def main() -> int:
        
         # get the in path, return the csv files list
        def get_path_files() -> list[str]():
            
            csv_list = list[str]()
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
        def clean_up_data(data_list: list[str]()) -> list[pd_df]():
            
            dfclean_list = list[pd_df]()
            df_list = [pd.read_csv(f) for f in data_list] 
            
            for idx, idf in enumerate(df_list):
                match idx:
                    case 0:
                        # Follow instructions for the 'ballotmapper.csv' file
                        # Keep only valid 'ContestID' and 'ChoiceID'
                        dfclean_list.append(idf.drop_duplicates( subset=['ContestID', 'ChoiceID']))
                        
                    case 1:
                        # Follow instructions for the 'choices.csv' file
                        dfclean_list.append(idf.drop_duplicates(subset=['ContestID']))
                        
                    case 2:
                        # Follow instructions for the 'contests.csv' file
                        dfclean_list.append(idf.drop_duplicates(subset=['ContestName']))
            
            return dfclean_list
        
        #Take the cleaned data, and output it to a spreadsheet
        def df_to_excel_fout(df_list :  list[pd_df]()) -> None: 
            
            #Create a list of sheets
            sheet_list = ["Ballot Mapper", "Choices", "Contests"]
            
            # Make the file name
            fname = "Cleaned_Ballots.xlsx"
            
            #make the parent directory, and give it a file name.
            path =fp("out/")
            path.mkdir(parents=True, exist_ok=True)
            fpath = path / fname
            
            # Create a new spreadsheet
            write_file = pd.ExcelWriter(fpath, engine = "xlsxwriter")
            
            for i, dfs in enumerate(df_list):
                dfs.to_excel(write_file, sheet_name=sheet_list[i])
            
            write_file.save()
        
                
        path_csvs = get_path_files()
        df_cleaned = clean_up_data(path_csvs)
        df_to_excel_fout(df_cleaned)
        
        sys.exit(0)        

    if __name__ == "__main__":
        main()
                
clean_dup = CleanDupsCVS()