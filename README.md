# Students Performance In Exams

 To develop an application which predict the performance of students in the exams
## Description of the data

   The dataset consist of the marks secured by the students of high school in various subjects
   
   Features of the data 

    There are 8 independent variables :

    1) gender : specifies the sex of the students either male or female
    2) race/ethnicity : ethnicity of the students and they are of 5(group A,group B,group C,group D,group E)
    3) parental level of education : education qualification of the students parents (bachelor's degree,some college,master's degree,associate's       degree,high school)
    4) lunch : either standard lunch or free/reduced luch type
    5) test preparation course :the type of preparation courses for the exams (completed,none)
    6) math score : scores secured in math subject out of 100
    7) reading score : scores of subject reading with max marks of 100
    8) writing score : scores in writing subject out of 100
     
    The dataset has 3 numerical and 5 categorical columns

    Target variable :
     
     Total scores : the sum of numerical coulmns (maths,reading and writing scores)

     dataset source : https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977
 
   ## Approach for the Project

    This is a regression based project where the total scores secured by a student in the exam is predicted.

   ## Tech stack used in the project
    1. Python
    2. Docker
    3. Machine learning algorithms

   ### Structure of the Project

   <img width="872" alt="Screenshot 2023-06-15 at 3 42 34 PM" src="https://github.com/sowmyah22/End-To-End-Data-science-project/assets/28885876/1f4b499a-2cc5-4dc5-ad46-c0026fecfc10">

   1. Data Ingestion :
     * The data is read as a csv file
     * The data is split into train ,test datasets and saved as csv files

   2. Data Transformation:
    * For the numerical data the imputation was a simple imputer with median for the missing values and the data was scaled using the standard scalar
    * The categorical data is imputed using simple imputer with mode for the missing values ,encoding of the data was done using OneHot encoding and the data was been scaled using standard scalar
    * The column transformer was used to perform this in sequential manner
    * The preprocessed data is saves as a pickle file

   3. Model Training:
   * The data is trained using various algorithms 
   * Further the hyperparameter tuning is performed and and among those models the best model is selected by the r2 scores
   * The model is saved as a pickle file

   4. Prediction:
   * The performance of the student is predicted by providing the details . Those details are taken in the form of dataframe and the saved pickle files are used for the predicton

   5. Application:
   * A flask application is created as a user interface for the prediction of the performance of the students

   ### Screenshot of the UI 

   <img width="864" alt="Screenshot 2023-06-13 at 6 04 23 PM" src="https://github.com/sowmyah22/End-To-End-Data-science-project/assets/28885876/dcc79c09-e820-4848-8455-6835bd93e42b">

   <img width="632" alt="Screenshot 2023-06-13 at 6 04 35 PM" src="https://github.com/sowmyah22/End-To-End-Data-science-project/assets/28885876/7d54210a-8769-4c4d-92d1-52249a3e3989">
    
   6. Docker Image:
   * A Docker image is built for the project and pushed to the dockerhub repository 
     https://hub.docker.com/repository/docker/soumyah22/performanceindicator-app
   
   ### Exploratory Data Analysis Notebook
      link :1.EDA_Student_performance.ipynb
   ### Model Training Notebook
       link:
   
   7. Deployment:
   * Deployed using AWS beanstalk for the web application and codepipeline for automating continious delivery service 
