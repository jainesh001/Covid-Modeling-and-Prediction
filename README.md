# Covid Modeling and Prediction
Current state of the covid 19 and estimation of its progression.

Steps involved
![image](https://user-images.githubusercontent.com/16863645/192909031-cc05a63b-1070-47ea-af49-2ca0cfa38674.png)


Source Identification 
JHU Source & OurWorldInData Source

Integration of Source in Current code with Github Submodules
 
![image](https://user-images.githubusercontent.com/16863645/192909173-f512287b-6e6c-4c0d-800e-937ef68e2fae.png)


Data Cleanup
Identify the missing Values
 -Using Lat data as identifier and adding the data  

Identify Incorrect Values
-Using Lat data as identifier and deleting the data


Data Analysis
- Descriptive Analysis
   * One week moving average
   * One month moving average
   
- Prescriptive Analysis(comparision of prediction amongst below)
    1.  AR(Auto regressive model)
        MAPE-8924.98 for 14 AR lag 
    2.  MA(Moving average regression model)
        MAPE- Too large
    3.  ARMA(Autoregressive moving average model)
        MAPE-8852.55 for 12 AR and 3 MA lag 

![image](https://user-images.githubusercontent.com/16863645/192909338-61b9a2d3-ebab-4f2c-b9c2-48f15a5619de.png)
![image](https://user-images.githubusercontent.com/16863645/192909345-2a00441c-3af1-4b6f-b12e-e5c3047077ae.png)
![image](https://user-images.githubusercontent.com/16863645/192909356-b8a192d5-c9b0-4a94-bfaa-07da014764b3.png)

   
Backend approach
  
![image](https://user-images.githubusercontent.com/16863645/192909417-a30fd2d7-9bf1-415e-a271-346849a7c7ae.png)
 
 Visulization
 
Amazon Quicksight
Quick Sight uses filters to focus on or exclude a visual element representing a particular value. Introduced global features.
To change the datatype, choose the data type icon under the field you want to change.
Dimensions and Measures: Dimensions are text or date fields that can be items, like products, or attributes that are related to measures. 
Measures are numeric values that you use for measurement, comparison.

![image](https://user-images.githubusercontent.com/16863645/192909617-2641c4ca-474e-434e-af03-fa594a5c6339.png)
![image](https://user-images.githubusercontent.com/16863645/192909636-80f4f06a-7bbd-4ff9-9523-f9fe571aab30.png)
![image](https://user-images.githubusercontent.com/16863645/192909646-a5b8c183-9457-44bb-97f8-9ecac7f74db3.png)


Connectivity

- SQL Joins
- Common field between tables

![image](https://user-images.githubusercontent.com/16863645/192909675-5946395c-66fb-4cb2-8293-11fc38415af6.png)


Dashboard

![image](https://user-images.githubusercontent.com/16863645/192909826-7bf4dbc5-3278-43ed-a8e2-8acd28c91ece.png)



Conclusion

* Performed Data collection, Data Preparation, also worked on AR, MA and ARMA model for data analysis in which ARMA is showing better performace in terms of MAPE.
* More time series analysis approach needs to be checked for there performace in order to establish better perfromance.
* Dashboard current version shows data related to positive, deaths and recovered cases. 
* With our current prediction we have tried to forcast month in future for the covid cases trend, as model tries to predict more further its effect seem to fade away.






