from datetime import datetime
from dataclasses import dataclass

@dataclass
class Utils:
    
    
    
    def time_structured_funds(start_year: int):
        years = [x for x in range(start_year,datetime.now().year + 1)]
        months = [x for x in range(1,13)]
        months_current_year = [x for x in range(1,datetime.now().month)]
        months_years = []
        for i in years:
            if(i == datetime.now().year):
                for j in months_current_year:
                    months_years.append(f"{i}{str(j).zfill(2)}")

            else:
                for j in months:
                     months_years.append(f"{i}{str(j).zfill(2)}")
    
        print(months_years)



