# Bank Note ML Classifier

An ML classifier web app to classify bank notes whether they are fake or not.

Dataset Link: https://archive.ics.uci.edu/ml/datasets/banknote+authentication

 The model is based on the following predictor variables:
 + Variance of the image
 + Skewness of the image
 + Curtosis of the image
 + Entropy of the image
 
 ## Prerequisites
 The following dependencies are required to be installed before running the application:
 + Docker
 + Pipenv
 
 ## Running the application
 
 Step 1: Make sure the prerequisites are installed
 
 Step 2: Clone the repo and initialize the pipenv shell environment
  + ```pipenv shell```
  
 Step 3: Install the required dependencies from the Pipfile.lock
  + ```pipenv install```
  
 Step 4: Run the postgres database docker and start the uvicorn server
  + ```make run-db start-server```
 
 Step 5: Start the streamlit server in a separate terminal
  + ```make run-streamlit```
  
 
 ## Contributing
 
 There are a whole bunch of things that can be added as feature to the project, I welcome all to raise issues or pull requests but please understand the project was made as a personal portfolio project and not a full-fledged one.
