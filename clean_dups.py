'''
Author: Jess Summerhill
Project: This is a take home quiz for a job interview with CBG.
Date: 8-26-2022
'''

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
                csv_list.append(file.name)
            
            return csv_list
        
                
        get_path_files()
        
        sys.exit(0)        

    if __name__ == "__main__":
        main()
                
clean_dup = CleanDupsCVS()