import numpy as np
import pandas as pd


def performPreprocessing(dataFrame):
    print("Performing Preprocessing")
    #dataFrame = pd.read_csv(filename)
    dataFrame = dataFrame.copy(deep=True)
    dataFrame["Gender"] = dataFrame["Gender"].fillna(dataFrame["Gender"].value_counts().index[0])
    #dataFrame["Gender"]
    dataFrame["Left - right handed"] = dataFrame["Left - right handed"].fillna(dataFrame["Left - right handed"].value_counts().index[0])
    #dataFrame["Left - right handed"]
    dataFrame["Only child"] = dataFrame["Only child"].fillna(dataFrame["Only child"].value_counts().index[0])
    #dataFrame["Only child"]
    dataFrame["Village - town"] = dataFrame["Village - town"].fillna(dataFrame["Village - town"].value_counts().index[0])
    #dataFrame["Village - town"]
    dataFrame["House - block of flats"] = dataFrame["House - block of flats"].fillna(dataFrame["House - block of flats"].value_counts().index[0])
    #dataFrame["House - block of flats"]
    
    print("Handling Categorized Data")
    categorical_variables = ['Gender','Left - right handed','Only child','Village - town','House - block of flats']

    dataFrame = pd.get_dummies(dataFrame, columns=categorical_variables)

    for i in dataFrame["Smoking"]:
        if i=="never smoked":    
            dataFrame["Smoking"].replace(i,1,inplace=True)
        elif i=="current smoker":
            dataFrame["Smoking"].replace(i,2,inplace=True)
        elif i=="tried smoking":
            dataFrame["Smoking"].replace(i,3,inplace=True)
        elif i=="former smoker":
            dataFrame["Smoking"].replace(i,4,inplace=True)
    
    dataFrame["Smoking"].fillna(round(dataFrame["Smoking"].mean()), inplace=True)
    
    for i in dataFrame["Alcohol"]:
        if i=="never":    
            dataFrame["Alcohol"].replace(i,1,inplace=True)
        elif i=="social drinker":
            dataFrame["Alcohol"].replace(i,2,inplace=True)
        elif i=="drink a lot":
            dataFrame["Alcohol"].replace(i,3,inplace=True)

    dataFrame["Alcohol"].fillna(round(dataFrame["Alcohol"].mean()), inplace=True)

    for i in dataFrame["Punctuality"]:
        if i=="i am often running late":    
            dataFrame["Punctuality"].replace(i,1,inplace=True)
        elif i=="i am always on time":
            dataFrame["Punctuality"].replace(i,2,inplace=True)
        elif i=="i am often early":
            dataFrame["Punctuality"].replace(i,3,inplace=True)

    dataFrame["Punctuality"].fillna(round(dataFrame["Punctuality"].mean()), inplace=True)

    for i in dataFrame["Lying"]:
        if i=="never":    
            dataFrame["Lying"].replace(i,1,inplace=True)
        elif i=="only to avoid hurting someone":
            dataFrame["Lying"].replace(i,2,inplace=True)
        elif i=="sometimes":
            dataFrame["Lying"].replace(i,3,inplace=True)
        elif i=="everytime it suits me":
            dataFrame["Lying"].replace(i,4,inplace=True)

    dataFrame["Lying"].fillna(round(dataFrame["Lying"].mean()), inplace=True)

    for i in dataFrame["Internet usage"]:
        if i=="no time at all":    
            dataFrame["Internet usage"].replace(i,1,inplace=True)
        elif i=="less than an hour a day":
            dataFrame["Internet usage"].replace(i,2,inplace=True)
        elif i=="few hours a day":
            dataFrame["Internet usage"].replace(i,3,inplace=True)
        elif i=="most of the day":
            dataFrame["Internet usage"].replace(i,4,inplace=True)

    dataFrame["Internet usage"].fillna(round(dataFrame["Internet usage"].mean()), inplace=True)

    for i in dataFrame["Education"]:
        if i == "currently a primary school pupil":
            dataFrame["Education"].replace(i, 1.0, inplace=True)
        elif i == "primary school":
            dataFrame["Education"].replace(i, 2.0, inplace=True)
        elif i == "secondary school":
            dataFrame["Education"].replace(i, 3.0, inplace=True)
        elif i == "college/bachelor degree":
            dataFrame["Education"].replace(i, 4.0, inplace=True)
        elif i == "masters degree":
            dataFrame["Education"].replace(i, 5.0, inplace=True)
        elif i == "doctorate degree":
            dataFrame["Education"].replace(i, 6.0, inplace=True)
        
    dataFrame["Education"].fillna(round(dataFrame["Education"].mean()), inplace=True)
    
    # Fill rest of the missing values with the mean
    print("Fill missing values")
    dataFrame=dataFrame.fillna(round(dataFrame.mean()))
    
    #Categorize Age
    for i in dataFrame["Age"]:
        if (15 <= i < 19):
            dataFrame["Age"].replace(i, 1.0, inplace=True)
        elif (19 <= i < 23):
            dataFrame["Age"].replace(i, 2.0, inplace=True)
        elif (23 <= i < 27):
            dataFrame["Age"].replace(i, 3.0, inplace=True)
        elif (27 <= i < 31):
            dataFrame["Age"].replace(i, 4.0, inplace=True)
        
    for i in dataFrame["Number of siblings"]:
        if i == 0:
            dataFrame["Number of siblings"].replace(i, 0.0, inplace=True)
        elif i == 1:
            dataFrame["Number of siblings"].replace(i, 1.0, inplace=True)
        elif i == 2:
            dataFrame["Number of siblings"].replace(i, 2.0, inplace=True)
        elif i == 3:
            dataFrame["Number of siblings"].replace(i, 3.0, inplace=True)
        elif i == 4:
            dataFrame["Number of siblings"].replace(i, 4.0, inplace=True)
        elif i > 4:
            dataFrame["Number of siblings"].replace(i, 5.0, inplace=True)
        
    for i in dataFrame["Height"]:
        if (62 <= i < 90):
            dataFrame["Height"].replace(i, 0.0, inplace=True)
        elif (90 <= i < 118):
            dataFrame["Height"].replace(i, 1.0, inplace=True)
        elif (118 <= i < 146):
            dataFrame["Height"].replace(i, 2.0, inplace=True)
        elif (146 <= i < 174):
            dataFrame["Height"].replace(i, 3.0, inplace=True)
        elif (174 <= i < 202):
            dataFrame["Height"].replace(i, 4.0, inplace=True)
        elif (i >=202 ):
            dataFrame["Height"].replace(i, 5.0, inplace=True)
        
    for i in dataFrame["Weight"]:
        if (41 <= i < 65):
            dataFrame["Weight"].replace(i, 0.0, inplace=True)
        elif (65 <= i < 89):
            dataFrame["Weight"].replace(i, 1.0, inplace=True)
        elif (89 <= i < 113):
            dataFrame["Weight"].replace(i, 2.0, inplace=True)
        elif (113 <= i < 137):
            dataFrame["Weight"].replace(i, 3.0, inplace=True)
        elif (137 <= i < 161):
            dataFrame["Weight"].replace(i, 4.0, inplace=True)
        elif (i >=161 ):
            dataFrame["Weight"].replace(i, 5.0, inplace=True)
     
    print("Return Preprocessed dataframe")
    return dataFrame
        
    
        