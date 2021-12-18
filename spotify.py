#import pandas package
import pandas as pd
from pandas.core.dtypes.missing import notna

# read spotify csv
df = pd.read_csv(r"C:\Users\andrew\Desktop\Spotify_Genre\spotify_genre.csv")

#drop empty columns
#df.drop(df.columns[[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]], axis = 1, inplace = True)

#print data frame
#print(df.loc[49,"Genre"])

# create empty dataframe for genre count
genres = []

# read each row of the genre column
#for index, row in df.iterrows():
    
    #if notna(row["Genre"]):

        # split each genre
        #list = row["Genre"].split(",")
        
        # if the split genre is already in the dataframe add to count else add new col
       # for x in list:
           # if not(x in genres):
                #genres.append(x)      

#genre_count = pd.DataFrame(columns = genres)
#genre_count.loc[1] = 0


# read each row of the genre column
for index, row in df.iterrows():
    
    if notna(row["Genre"]):

        # split each genre
        list = row["Genre"].split(",")
        
        # if the split genre is already in the dataframe add to count else add new col
        for x in list:
            print(x)
            for column in df:
                if((x == column) and (column != "Genre") and (column != "Song ID")):
                    df.at[index, column] = 1
                    print(index , column , df.at[index, column])
                elif((x != column) and (column != "Genre") and (column != "Song ID") and not(column in list)):
                    df.at[index, column] = 0     
                    
df.to_csv("is_genre.csv")
print("CSV Created")             
       
# sort genre by most frequent

# add genre columns to old df

# loop over genre column and set specific genre's to true if there

# export new csv to merge in R


