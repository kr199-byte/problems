#import dependencies

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split



#using pandas to store the database.

data=pd.read_csv('mnist_test.csv')


    '''KNOW MORE ABOUT PROVIDED DATA'''
#view the column heads
print(data.head())

#extracting data from the dataset and viewing them up close
a=data.iloc[3,1:].values

#reshape the extracted data into a reasonable shape

a=a.reshape(28,28).astype('uint8')
plt.imshow(a)


    ''' CLASSIFICATION USING GIVEN DATA '''

#preparing the data
#seperate the data values and labels
df_x=data.iloc[:,1:]  #included everything except label to a variable df_x
df_y=data.iloc[:,0]   #included every label to df_y
print(df_x)
print(df_y)

#creating  test size and train sizes/batches
x_train,x_test,y_train,y_test=train_test_split(df_x,df_y,test_size=0.3,random_state=4)

#check data
y_train.head()

#call RandomForestClassifier
rf=RandomForestClassifier(n_estimators=100)

#fit the model
rf.fit(x_train,y_train)

#create predictor 

pred=rf.predict(x_test)

print(pred)



    '''PREDICTION ACCURACY'''

s=y_test.values

#calculate the number of correctly predicted values
count=0
for i in range(len(pred)):
    if pred[i]==s[i]:
        count+=1

print('Count',count)

#total value given for prediction
print(len(pred))

#accuracy value
a=(count/len(pred))*100
print('Percentage',a)
