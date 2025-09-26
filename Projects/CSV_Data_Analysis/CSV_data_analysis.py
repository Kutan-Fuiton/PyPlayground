# Initially started with this table:
# Name	    Math	 Science	English
# Alice	    85	     92	        78
# Bob	    90	     88	        95
# Charlie	75	     80	        72


import pandas as pd

df = pd.read_csv('student_marks.csv')
print(df.head())