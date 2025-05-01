import sqlite3
import pandas as pd
# Connect to existing database or create if it doesn't exist
conn = sqlite3.connect('C:\\Users\\Durga\\Downloads\\sqlite\\pythonlearnDb.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

cursor.execute("SELECT * from landing_employee;")
l_rows = cursor.fetchall()
landing_df= pd.DataFrame(l_rows, columns=[column[0] for column in cursor.description])
print(landing_df)

cursor.execute("SELECT * from dal_employee;")
d_rows = cursor.fetchall()
dal_df= pd.DataFrame(d_rows, columns=[column[0] for column in cursor.description])
print(dal_df)

merged_df= pd.merge(landing_df, dal_df, how='left', left_on='landing_id', right_on='emp_id', suffixes=('_landing', '_dal'))
print(merged_df)

assert merged_df['emp_name_landing'].equals(merged_df['emp_name_dal']), "Data mismatch found!"
print("Data validation successful!")

conn.close()



        