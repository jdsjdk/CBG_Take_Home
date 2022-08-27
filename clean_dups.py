'''
Author: Jess Summerhill
Project: This is a take home quiz for a job interview with CBG.
Date: 8-26-2022
'''

from cgi import test
import sys
import pandas as pd
from typing import List
from pathlib import Path as fp

class CleanDupsCVS:
    
    # generic constructor
    def __init__(self) -> None:
        pass     

    def main() -> None:
        
         # get the in path, return the files list
        def get_path_files() -> List[str]:
            
            csv_list = []
            in_path = fp().cwd()  / "in/"
            files = in_path.rglob("*.csv")
            
            for file in files: 
                csv_list.append(in_path / file.name)
            
            return csv_list
        
        #Take in all of the CSV data, and then clean it all up
        def clean_up_data(data_list: List[str]) -> None:
            df1 = pd.read_csv(data_list[2])
            print(df1)  #Stopping Tests for now.  Finish up tomorrow.
            pass
        
                
        path_csvs = get_path_files()
        clean_up_data(path_csvs)
        
        
        sys.exit(0)        

    if __name__ == "__main__":
        main()
                
clean_dup = CleanDupsCVS()