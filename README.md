# DS-4002-Project-3
This project uses data containing the average retail motor gas price from 1976 - 2023 adjusted for inflation to assess whether or not prices are time-dependent. Data may be considered time-dependent, or seasonal, through a test for stationarity. 

## SRC
### Installing/Building Code
  We downloaded the data as a CSV from the U.S. Energy Information Administration. The dataset contained monthly average non-diesel retail motor gas price from 1976 - 2023, both as real (adjusted for inflation) and nominal values. Using the datetime module, we converted the dates from Month YYYY to YYYY-MM-DD format and created two separate columns containing the year as YYYY and the month as M [1].


### Usage of Code
  We then imported adfuller from the statsmodels.tsa.stattools module to peform an augmented Dickey-Fuller test (ADF), which produced an ADF statistic, p-value, and set of critical values [2]. After performing the ADF test, we imported matplotlib and tensorflow to produce a visual of the Dickey-Fuller test for stationarity. 

## Data
Data Dictionary
|Column Name|Definition                                                                                    |Data Type      | 
|-----------|----------------------------------------------------------------------------------------------|---------------|
|Month |The date of gas price observation (e.g., March 2023).                             |Datetime        |
|CPI |The consumer price index published by the Bureau of Labor Statistics.    |Float        |
|Nominal      |The price of gas in the year of the observation.  |Float      |
|Real      |The price of gas in inflation-adjusted dollars for 2023 (e.g., 4.22).     |Float         |

[Link to data](https://github.com/avneetch/DS-4002-Project-3/blob/3715b5e2e6df349ab240e39c4735fe80adb80e76/Data/real_gas.csv)


### Relevant notes about the Use of Data
  The data only contains monthly averages as opposed to daily or weekly. This limits the ability to draw precise conclusions about gas price time-dependence. 

## Figures
Table of Contents
|Figure     |Key Takeaways| 
|-------------------------------------------------|--------------------------------------------------------------------------------------------------|
|Figure 1 Gas Price Prediction                   | RNN accurately predicted gas priices. |
|Figure 2 Autocorrelation                  | Trend, not random |
|Figure 3 Stationary Analysis | Cannot reject stationarity|
|Figure 4 Price Rise/Decline | Likelihood of rise/decline fluctuates and hovers around 50%|

## References
[1] S. Girgin. "Python-based oil & gas price analysis." Medium.com. https://medium.com/pursuitnotes/python-based-oil-gas-price-analysis-1fe5e10a23b0. (accessed April 18, 2023).   
[2] Jiwidi. "Time series forecasting with python." Github. https://github.com/jiwidi/time-series-forecasting-with-python/blob/master/time-series-forecasting-tutorial.ipynb. (accessed April 18, 2023).  


### Links to MI1 and MI2
[MI1](https://docs.google.com/document/d/16KW47FVTcNRLVW94Ycd_IxVnLPN2BU77JGky71UFqJQ/edit?usp=share_link)  
[MI2](https://docs.google.com/document/d/1_ug_r5ILIBxlOvBHoCTClUHNrOUrktU2ir1bjQX7YkU/edit?usp=share_link)
