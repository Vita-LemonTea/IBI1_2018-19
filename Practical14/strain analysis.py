# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import library
import pandas as pd
#open and read the file
file = open('Final_Fluview_Practical_dataset.xlsx')
df = pd.read_excel('Final_Fluview_Practical_dataset.xlsx')

# df.info()
# print (df.head(5))
df.describe()
for column in df:
    print(column)
    print(df[column].unique())
    print('')

#slice some columns from the full data
df_regress = df[['Virus Strain',
                 'Age',
                 'Gender',
                 'Hospitalized?',
                 'Swine Contact?',
                 'Attended Agricultural Event?']]

#check rows with missing values
df_regress[df_regress.isna().any(axis=1)]
#remove rows with missing valus
df_regress = df_regress.dropna()
#display the set of values that appear across each column 
for column in df_regress:
    print(column, df_regress[column].unique())

df_regress['Virus Strain'] = df_regress['Virus Strain'].map({'Influenza A H1N1v':0, 'Influenza A H1N2v':1, 'Influenza A H3N2v':0, 'Influenza A H7N2':0})
df_regress['Age'] = df_regress['Age'].map({'<18 Years':0, '>=18 Years':1})
df_regress['Gender'] = df_regress['Gender'].map({'Female':0, 'Male':1, 'female':0, 'male':1})
df_regress['Hospitalized?'] = df_regress['Hospitalized?'].map({'No':0, 'Yes':1, 'no':0, 'yes':1})
df_regress['Swine Contact?'] = df_regress['Swine Contact?'].map({'No':0, 'Yes':1, 'no':0, 'yes':1})
df_regress['Attended Agricultural Event?'] = df_regress['Attended Agricultural Event?'].map({'No':0, 'Yes':1, 'no':0, 'yes':1})



import statsmodels.api as sm
import statsmodels.formula.api as smf

endog = df_regress['Virus Strain']
exog = df_regress[['Age',
                   'Gender',
                   'Hospitalized?',
                   'Swine Contact?',
                   'Attended Agricultural Event?']]
                           
exog = sm.add_constant(exog)

logit = smf.Logit(endog, exog)
result = logit.fit()
result.summary()

import numpy as np
print('Odds ratios:')
print(np.exp(result.params))
print(result.summary())





















