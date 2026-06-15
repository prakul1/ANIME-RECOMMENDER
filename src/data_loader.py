import pandas as pd

class AnimeDataLoader:
    def __init__(self,original_csv:str,processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        df = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines='skip', skipinitialspace=True)
        df.columns = df.columns.str.strip().str.lower()
        required_col = {
            'name','genres','sypnopsis'
        }
        missing = required_col - set(df.columns)
        if missing:
            print(f"Available columns: {set(df.columns)}")
            print(f"Missing columns: {missing}")
            raise ValueError ("Missing column in csv file")
        
        # Drop rows where required columns are NaN
        df = df.dropna(subset=list(required_col))
        
        df['combined_info'] = (
            "title :" + df['name'] + ".. Overview:" + df['sypnopsis'] + "Genres:" + df['genres']
        )

        df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')

        return self.processed_csv
