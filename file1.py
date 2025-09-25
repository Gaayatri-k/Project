import os
import pandas as pd
Filename="students.csv"
if not os.path.exists(Filename):
    data=pd.DataFrame(columns=[])