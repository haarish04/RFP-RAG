import pandas as pd
from typing import IO
from fastapi import UploadFile
import io

async def load_csv_file(file: UploadFile) -> list[dict]:
   df = await load_dataframe(file, file.filename)
   if "Question" not in df.columns or "Answer" not in df.columns:
       raise ValueError("File must have fields 'question' and 'answer'")
   df = df.dropna(subset=["Question", "Answer"])
   return df[["Question", "Answer"]].to_dict(orient="records")


async def load_questions_file(file: UploadFile) -> list[dict]:
   """For querying — expects only 'question'"""
   df = await load_dataframe(file, file.filename)
   if "Question" not in df.columns:
       raise ValueError("File must have field 'question'")
   df = df.dropna(subset=["Question"])
   return df[["Question"]].to_dict(orient="records")


async def load_dataframe(file: UploadFile, filename: str) -> pd.DataFrame:
   ext = filename.split('.')[-1].lower()

   content = await file.read()

   if ext == 'csv':
       df = pd.read_csv(io.BytesIO(content))
   elif ext in ['xls', 'xlsx']:
       df = pd.read_excel(io.BytesIO(content))
   await file.seek(0)    
   return df
