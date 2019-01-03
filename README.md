# Overview
Pets are our best friends. They are loyal to their owners and offer the best companion, bringing pleasure to our life. However, a lot of pets are abandoned by unresponsible owners, suffering hunger and bitterness. In this project, we analyze pets' data from PetFinder.my to predict the pet adoption speed to help pets at a shelter to find their responsible owners. This project is performed by Yiming Huang, Ruxin Shen, and Kai Kang. The data scientist, Jingyi Yu from Yelp will give industry perspective to improve the quality of this project.

# Data Socure
Original data is from PetFinder.my. The modified version is from Kaggle competition.

# Pipeline

## 1 Data Cleaning
### Feature Engineering
#### Delete four features
Name, RescureID, PetID, Description, but we can explore the Description in the future
#### Feature Age
Include Age >= 192 for cats (2 enties) and Age >= 211 for dogs (4 enties), where 192 and 211 are average lifespan for cats and dogs in month, respectively; also, age can be treated as cluster in the future
#### Feature Breed
Delete five rows where Breed1 == 0, but Breed2 != 0
#### Feature VideoAmt and PhotoAmt
Can be treated as binary classes in the future

## 2 Potential Models
Logistic Regression
K Nearest Neighborhood
Naive Bayes
Support Vector Machine
Decision Tree
Neural Network
## 3 Hyperparatemer Tuning
In this section, we attemp to select the best parameter for each model.
## 4 Best Model
In this sectuon, we attemp to select the best model.

# Schedule
### 2019-01-04 Deadline for Data Cleaning
### 2019-01-06 Potential Models
### 2019-01-07 Hyperparameter Tuning
### 2019-0-20 Best Model
