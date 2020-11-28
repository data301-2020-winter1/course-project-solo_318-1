import pandas as pd
import numpy as np
def load_and_process(url_or_path_to_csv_file):

    df1 = (pd.read_csv(r'\Users\john\Desktop\course-project-solo_318-1\Analysis\listings(2).csv')
           .drop(df.index[5000:19343],0,inplace=False)
          .rename(columns={"id": "Property_id"})
          .rename(columns={"name": "Property_name"})
          .reset_index(drop=True) )

    df2 = (
            df1
            .sort_values("Property_id", ascending=True)
            .drop(columns=['neighbourhood_group'])
            .drop(columns=['longitude', 'latitude'])
            .dropna()
     
           )

    return df2