
# Machine Learning tool to predict number of Aircraft Departures

### Problem:

Aviation sector is showcasing intriguing growth rate in the emerging economies like India and other APAC nations. Due to various government initiatives, new aviation infrastructure is being developed in India. There is a push to provide affordable air travel for wider population. In addition, the economic growth of India is leading to distribution of economic activities across tier-II cities, which wasn’t necessarily the case in the recent past. Hence, many air-travel routes between metro / tier-I cities and tier-II cities have come up. This trend will continue where demand for more such routes with direct connectivity between tier-II cities will come up. Further, with increasing global involvement from Indian industry and diaspora, the long haul traffic is also primed to increase.

### Expected Solution:

In this track of the hackathon, we apply Machine learning concepts to built an analytical model that takes macro-economic data and identifies potential number of aircraft departures at cities/region level.

## Objective 

The objective of this project are:

a. Create a prediction model which can predict number of aircraft departures

b. Identify key factors influencing the number of aircraft departures

c. Make the model accessable to end users, and aid them in predicting the number of aircraft departures

## Approach : Constructing the prediction model

### Data Audit & Analysis 

The data was sourced from the World Bank Database. The data is at country X year level. 

Following were the input attributes considered 

Dependent Variable: Air transport, registered carrier departures worldwide

Independent Variables:
1. Population ages 0-14, female
2. Population ages 0-14, male
3. Population ages 15-64, female
4. Population ages 15-64, male
5. Population ages 65 and above, female
6. Population ages 65 and above, male
7. Rural population
8. Urban population
9. Agriculture, forestry, and fishing, value added (current US$)
10. Industry (including construction), value added (current US$)
11. Manufacturing, value added (current US$)
12. Services, value added (current US$)
13. Fixed broadband subscriptions
14. Fixed telephone subscriptions
15. Mobile cellular subscriptions
16. Fixed broadband subscriptions
17. Fixed telephone subscriptions
18. Mobile cellular subscriptions

### Feature Engineering 

Top-3 features constituted 60% of feature importances

![image](https://user-images.githubusercontent.com/122376420/229372374-06aceffb-0af0-4c68-8037-4549ff9d98a6.png)


The following attributes were considered for the final model: Fixed telephone subscriptions, Services, value added (current US$), Manufacturing, value added (current US$)

### Optimisation and final model 

XGBoost was the final model considered

![image](https://user-images.githubusercontent.com/122376420/229372419-3c8b82ee-aadb-4ab3-9a2d-925038e94396.png)


## Usage & Implementation

### Usage 

The model was deployed in cloud and API was created to enable end users to leverage the prediction model to predict number of aircraft departures. A user can access the prediction model on this URL: https://airdepartures-pred38.azurewebsites.net/

### Implementation on local system 

The following steps underline the approach for implementation :

1. Go to the project directory in your local system. Activate the python version 3.8 environment

2. Clone the repository: Execute the following code 

```
git clone https://github.com/span-11/airdepartures_pred.git
```

3. Go to the repository folder 

```
cd airdepartures_pred
```

4. Install the needed libraries by executing below comands

```
pip install -r requirements.txt
```
5. Run the following command  
```
python app.py
```

Addendum: The source files (to obtain the raw dataset and the model file) can be referred in the following directory of the repository

```
cd source_codes
```
The file 'WorldBank_Data.xlsx' is the extract after executing the code RR_PassengerPrediction_DataPull
Executing RR_PassengerPrediction_Model file produces the model file


## License

This project is licensed under the MIT License - see the LICENSE file for details.
