
# PRODUCT RECOMMENDER
#### Demo: https://youtu.be/23Q5lcyPAOY
#### Heroku: https://inter-medical.herokuapp.com/

The idea of this project was to respond to genetic tests that are more and more widely available on the market, 
thanks to which we could find the genomes where the mutation occurred and on this basis determine which diseases the patient suffers from.
These diseases are written in the form of a dictionary where the key will be the name of the disease and the value will be the possibility of the disease.

Having information about the patient and the possibility of diseases, 
our system would like to recommend the best medical products that can help the patient. 
In this case, an additional recommendation system is built-in for each product, 
which calculates the most valuable opinion due not only to the customer's rating but also the amount of purchase, 
so we can recommend the best product for a given disease. 
The program calculates the results of the fitting, acting quite precisely for longer lists of products and possible diseases in the patient.

I was not able to submit in this project the full version with the visualization of the report on url, 
the variables from the report are displayed in the bootstrap template with a flash, 
such a working recommendation system in the cloud could save reports in the database 
and get the variables data into webservices which could be something like this:
#### Desire Output: https://inter-medical.herokuapp.com/
project.py program only prints output of products for patient disorders match


#### Tech:
Python, Pandas, Numpy, Pytest

In full presentation version: 
MongoDB, Flask, Heroku

#### Input: 
1) patient data template from csv file with name, age, gender, date of patient visit 
   add mocked dictionary to patient data template of patient disease and probability of disease occurs 
   as a result of patient genetic test 😉  

2) medical products list in a csv file, with product name, type, describtion, rating, amount of products purchase, list of diseases that product cures

#### Description:
1) Reads random patient and product data
2)	Add recommended weight score calculated for products, from number of products purchase and customer reviews - rating 
2)	Match the best product meds as cure for patient disorders

In full version: 
3)	Store final best product match as medical report - dictionary variables in MongoDB collection 

#### Output:
Print patient mediacal report with four best matched products for patient disorders

In full version:
1) Visualization of last patient report with products recommendation on web url 

####	What new skills will you need to acquire? What topics will you need to research?
Medical geo – mutations, pro medical products, genetic disorders for medical concept
Random data preparation 
AI for weighted product recommendation system 
AI for best product meds score match for patient disorders

In full version: 
ETL for flow goes around ending in mongo db collection for report storage
Data visualization,  web build for final report
PASS serv deployment for showing final report   








