import pandas as pd 

# Open data file
weather_df = pd.read_csv("weather_data.csv")

print ("Reading data file. Here's the head.")
print (weather_df.head())

print ("Saving data file to html")
weather_df.to_html(buf="weather_data.html", index=False)
print ("Done.")