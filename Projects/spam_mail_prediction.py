import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score

raw_email_data = pd.read_csv('../Datasets/mail_data.csv')
mail_data = raw_email_data.where(pd.notnull(raw_email_data), "")

# label encoding: ham = 1 & spam = 0
mail_data.loc[mail_data["Category"] == "spam", "Category", ] = 0
mail_data.loc[mail_data["Category"] == "ham", "Category", ] = 1

X = mail_data["Message"]
Y = mail_data["Category"]

# Splitting the data into train & test data

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 3)

print("X_train:", X.shape)
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("Y_train:", Y_train.shape)
print("Y_test:", Y_test.shape)

# transform the text data into feature vector so it can be given as input LogisticRegression model

feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)

X_train_feature = feature_extraction.fit_transform(X_train)
X_test_feature = feature_extraction.transform(X_test)

Y_train = Y_train.astype("int")
Y_test = Y_test.astype("int")


model = LogisticRegression()
model.fit(X_train_feature, Y_train)
Y_pred = model.predict(X_test_feature)

test_accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy score", test_accuracy)

test_mail = ["SIX chances to win CASH! From 100 to 20,000 pounds txt> CSH11 and send to 87575. Cost 150p/day, 6days, 16+ TsandCs apply Reply HL 4 info"]
test_mail = feature_extraction.transform(test_mail)
prediction =model.predict(test_mail)
print("prediction", prediction)

if prediction[0] == 0:
    print("Spam")
else:
    print("Ham")

stop  = True