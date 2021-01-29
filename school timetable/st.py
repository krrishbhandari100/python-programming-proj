import webbrowser
import datetime
import numpy as np
import pandas as pd
import json

classes = {
    "Computer": "https://meetingsapac31.webex.com/meet/pr1568096520",
     "English": "https://meetingsapac31.webex.com/meet/pr1564185680",
     "Hindi": "https://meetingsapac31.webex.com/meet/pr1569999888",
     "SST": "https://meetingsapac31.webex.com/meet/saiyamkasat",
    "Physics": "https://meetingsapac31.webex.com/meet/pr1569647124",
     "Biology": "https://meetingsapac31.webex.com/join/pr1568497995",
     "Chemistry": "https://meetingsapac31.webex.com/meet/pr1565412085",
     "Maths": "https://meetingsapac31.webex.com/meet/pr1566181695",
}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_today = days[int(datetime.datetime.now().weekday())]

time_table = pd.read_excel("time table.xls")
df = pd.DataFrame(data=time_table).to_json()
parsed = json.loads(df)
school_periods = parsed[day_today]
print(parsed)