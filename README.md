# MLOPS

Docker AWS Lambda API and Heroku Web App

This is a MLOPS template repository. There are two folders:
  - API: Here you can find the main file, app.py, where the FastApi GET and POST methods are defined, and also the I/O API data types. The model folder, consists of the Jupyter Notebook for ML, the preprocessor object, the model object trained and the model.py file, where the prediction is done.
  - Web/src: This is the project containing the web service for the user interface, prepared for deploying to Heroku.

The API is deployed at this moment as a AWS Lambda Function, being the files stored in AWS ECR.

The Web Service is at this time deployed in Heroku.

You can try it [here](https://predweight.herokuapp.com/), but remember, it may take a while to load (some seconds) because of the Heroku and AWS Lambda cold start.

Questions, suggestions or corrections are welcome.
