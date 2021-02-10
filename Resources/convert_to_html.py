import pandas as pd 

# Open data file
Tesla_df = pd.read_csv("./Tesla-orig.csv")

print ("Reading data file. Here's the head.")
print (Tesla_df.head())

#print ("Saving data file to html")
#Tesla_df.to_html(buf="Tesla-orig.html", index=False)
#print ("Done.")