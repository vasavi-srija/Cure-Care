<h1 align="center"><b>
    Cure & Care
  </b>
</h1>

**DESCRIPTION**

**Software**

**Cure & Care** is a website created for the ease of common people and the staff of a speciﬁc hospital. It is a Covid-19 centric help centre.
![Idea_des](https://user-images.githubusercontent.com/54552117/118690973-39079b80-b826-11eb-8282-1ff124bbde4c.PNG)

➢ **HOME PAGE**

The home page provides you with four options:

**1. Covid prediction** : This section takes in symptoms as input and predicts the possibility of a person suffering with covid 19. It uses the logistic regression ML model to do so.





<p align="center"><b>
    Covid Prediction
  </b>
</p>

![symptom_check](https://user-images.githubusercontent.com/54552117/118691567-d662cf80-b826-11eb-9fe4-fba958069419.png)


**2. Contribution** : This is a division which provides an interface to ﬁll up personal details if anyone is interested in donating money, plasma, oxygen or blood. It has separate forms for each of the mentioned sections.

**3. Vaccination slots** : It displays a calendar with dates and timings of slots available to get vaccinated. It also provides a link which redirects the user to the oﬃcial cowin website.

**4. Inventory** : This keeps people informed about the beds and oxygen availability of the hospital. It gets the information about the number of patients from a patients' database and calculates the resources left.

➢ **LOGIN INTERFACE**

This is exclusively for the staff of a hospital. Sign-up option adds a staff member into the staff database (a second database exclusively for the staff members) and the login option ensures that the user is present in the same database.





There are again four options in the login interface:

**1. Add a patient** : It is an interface to add a patient into the patients' database. Here it also predicts if the covid patient is severe, moderate or mild again using a logistic regression ML model and accordingly assigns them ICU, normal ward or home isolation. The severity is alerted to the patient by sending them email alerts. This is done using SMTP.

<p align="center"><b>
    Patient classiﬁer
  </b>
</p>

![Classifier](https://user-images.githubusercontent.com/54552117/118691773-07430480-b827-11eb-8faa-3cdb1179254e.png)

**2. Patients list**: This renders to the patients database to list out details of all the patients admitted.

**3. Dashboard**: Displays the list of patient ids and names. It redirects the user to the dashboard when they click on the Patient ID. This dashboard helps in visualizing the patient's condition. Jquery, AJAX, JSON endpoints, python scripts. It will take information dynamically from a spreadsheet and display it as a table in dashboard section.

>Spreadsheet link: https://docs.google.com/spreadsheets/d/1oSLcvPqsJm-Tgto7Hu1M6PyZuVrjBj6H6guqs3wgn1o/edit?usp=sharing

**4. Predict Capacity:** Based on the number of patients in the database, inventory of hospital and frequency of patients being admitted per day, it predicts the number of days in which the hospital might run out of beds and oxygen.This helps the staff to be prepared for the upcoming covid wave.





**Hardware**

The hardware part of our project is a robotic arm having 4 degrees of freedom. It is mainly used as a transport vehicle to deliver important items like the medicines and food to the patients in isolation. Nodemcu has been used as a microcontroller and ESP8266-12E for communication purposes. The whole bot can be wirelessly controlled using the blynk app.

**HARDWARE AND SOFTWARE REQUIREMENTS**

![Implementation_Flow_Chart](https://user-images.githubusercontent.com/54552117/118691908-2a6db400-b827-11eb-90f9-e8d606584151.PNG)

The **hardware** components used in the Robotic-arm:

● Servos

● Nodemcu

● ESP8266-12E

● Jumper wires

● Battery





The **software** components used :

● Flask

● MySQL Workbench

● Amazon Web Services(AWS)

● Anaconda Jupyter Notebook

● Arduino IDE

● Blynk App

**PROCESS FLOW**

<p align="center"><b>
    Software Process Flow
  </b>
</p>

![flow_chart](https://user-images.githubusercontent.com/54552117/118691982-3e191a80-b827-11eb-8af4-efd33a2607f9.png)



<p align="center"><b>
    Hardware Process Flow
  </b>
</p>

![hardware](https://user-images.githubusercontent.com/54552117/118692050-4d986380-b827-11eb-9c44-c1d6057c35a6.PNG)

**DATA FLOW DIAGRAM**

<p align="center"><b>
    Patient’s Database
  </b>
</p>

![pat_data](https://user-images.githubusercontent.com/54552117/118692231-71f44000-b827-11eb-8a04-71f0b28102e6.png)




<p align="center"><b>
    Staff’s Database
  </b>
</p>

![doc_data](https://user-images.githubusercontent.com/54552117/118692395-a0721b00-b827-11eb-92e3-9edbe2aaec95.png)

![bedandoxy](https://user-images.githubusercontent.com/54552117/118692368-96501c80-b827-11eb-9a0f-63df08b36254.PNG)



**HOW TO RUN THE CODE :**




**Method-1:**

**Installation**

● Python 3.x version

● Install MySQL Workbench and create database

● Create virtual environment

● Make sure you have ﬂask, mysqldb, sklearn installed

**Usage**

● Run the check.py ﬁle




**Method-2 :**

You can access the website via <http://18.116.46.160:5000/>



**NOTE**: "Add a patient" section of the login interface, sends a mail to the patient's email id which requires SMTP authentication. Hence this feature works only when the files are downloaded and are run on localhost. The above link does not implement that part of the project. 
