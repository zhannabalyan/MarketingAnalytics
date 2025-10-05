**Innovation Diffusion Analysis Based on TIME’s Best Innovations
List**

In this assignment, I will explore how *Dyson OnTrac headphones* might spread in the personal audio market using the Bass Model. To guide this forecast, Dyson OnTrac will be compared to the infamous *Apple Airpods*, which was a past innovation that revolutionized the wireless audio indsutry and set a benchmark for other similar products.

**Innovation from 2025: Dyson OnTrac headphones** 

Dyson OnTrac headphones are a recent innovation in the wireless audio industry. The headphones offer advanced noise cancellation that can block up to 40dB of external sounds. This sets up an immersive and effective listening experience for the users. Furthermore, they also provide a wide sound range, customizable sound settings and quite a long battery life of up to 55 hours. Dyson Ontrac is aimed at users who value high-quality audio experiences and cherish comfort above all else

**Innovation from the past: Apple Airpods**

Apple AirPods changed the wireless audio market when they were first introduced in 2017. They removed the useless discomfort of wires, offered very efficient Bluetooth connectivity, and worked smoothly with all Apple devices. This innovation also introducted noise cancellation and adaptive audio when it entered the market. Apple Airpods became a widely adopted innovation and set the standard for wireless headphones.

**The motive behind comparing the two products:**

Both Dyson OnTrac headphones and Apple AirPods have made a strong impact and have left a trace in the wireless audio market in their own ways. AirPods focused on convenience, portability, and integration which made wireless audio mainstream and got everyone to switch from regular headphones to wireless ones. Dyson OnTrac puts a huge emphasis on giving its users premium sound quality, advanced noise cancellation, and long battery life. This might appeal more to users seeking a more immersive experience. Despite these differences, they both rely on Bluetooth technology, target consumers who are more technologically oriented, and show how innovative features encourage users to adopt the product. This is why studying AirPods’ adoption patterns provides useful insight for predicting how Dyson OnTrac might spread in the market.


```python
# Install necessary libraries
#!pip install pandas numpy matplotlib

```


```python
#!pip install pandas openpyxl


```


```python
#!pip install scipy

```


```python
#importing the necessary libraries

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

```

The data that will be utilized in the scope of this assignment was retrieved from the Statista website, the link to which can be found here:https://www.statista.com/statistics/1421624/apple-airpods-unit-sales/ 
The dataset is an Excel workbook containing a description of the data and the **annual unit sales of Apple AirPods from 2017 to 2024.**


```python
file_path = r"C:\Users\HP\Desktop\airpods_data.xlsx"
df = pd.read_excel(file_path, sheet_name="Data")  

#Since, the excel sheet is not written in a proper way as there are many skipped rows, the information doesnt print out in the right way.
#Since the data is pretty small, in the cell below I will enter it manually into a dataframe to avoid any errors.


```


```python
data = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Sales': [15, 35, 60, 114, 85, 82, 75, 66]  
}

airpods = pd.DataFrame(data)
airpods

#Now we have the crucial information that we need for our analysis.
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017</td>
      <td>15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2018</td>
      <td>35</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2019</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2020</td>
      <td>114</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2021</td>
      <td>85</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2022</td>
      <td>82</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2023</td>
      <td>75</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024</td>
      <td>66</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize=(8,4))

plt.bar(airpods['Year'], airpods['Sales'], color='pink', alpha=0.6)

plt.plot(airpods['Year'], airpods['Sales'], marker='o', color='blue', linewidth=2)

plt.title('Apple AirPods Unit Sales(2017-2024)')

plt.xlabel('Year')

plt.ylabel('Unit Sales in Milions')

plt.show()

```


    
![png](output_12_0.png)
    


The plot above displays the historic sales of Apple AirPods from 2017 to 2024. As we can see, the sales started at approximately 15 million in 2017, after which they started rising sharply to a peak in 2020. Then we can see how the sales gradually declined by 2024. This indicates a rapid initial adoption followed by a slowdown as the market became saturated.


```python
from scipy.optimize import curve_fit
```


```python
def bass_model(t, p, q, M):
    """Bass Diffusion Model for the annual sales"""
    return (M * (p + q)**2 * np.exp(-(p + q) * t)) / ((p + q * np.exp(-(p + q) * t))**2)


airpods['Year_norm'] = airpods['Year'] - airpods['Year'].min()


initial_guess = [0.03, 0.38, 160]  
parameters, _ = curve_fit(
    bass_model, 
    airpods['Year_norm'], 
    airpods['Sales'], 
    p0=initial_guess
)
p, q, M = parameters


print("\nBass Model Parameters for Apple AirPods:")
print(f"coefficient of innovation(p): {p:.4f}")
print(f"coefficient of imitation(q): {q:.4f}")
print(f"market potential in millions(M): {M:.2f}")

```

    
    Bass Model Parameters for Apple AirPods:
    coefficient of innovation(p): 0.0430
    coefficient of imitation(q): 0.5557
    market potential in millions(M): 26.08
    

In this step, the Bass Diffusion Model was applied to estimate how AirPods spread in the market over time. The model uses three key parameters: p(coefficient of innovation), q(coefficient of imitation), and M(market potential). First, the years were normalized to start from zero. Then, the curve_fit() function was used to find the best-fitting values for p, q, and M based on the observed sales data. These parameters describe how quickly the product was adopted and help predict the diffusion of similar innovations.

**Interpretation of the results:**

As the results of the bass model show in the above cell, our coefficient of innovation is 0.430, which essentially indicates, that about 4.3% of potential adopters purchased the Apple AirPods based on external influences such as advertising, media coverage, or early adopter behavior.
The coefficient of imitation is 0.5557, which means that social influence and word-of-mouth played a major role in driving adoption, with many consumers purchasing AirPods after observing others use them.
And finally, the market potential is 26.08, and it represents the estimated total number of consumers who are expected to adopt AirPods over their lifecycle.



**Prediction approach for the Dyson Ontrac headphones:**

According to a research on Statista website conducted on the headphone market share by different brands, it is known that *Apple is the market leader with 34% market share, followed by Beats by Dr. Dre, Bose, Samsung, JBL, Sony, SkullCandy and LG Electronics*.

**Link to the study**:  https://www.statista.com/chart/26791/most-popular-headphone-brands-in-the-us/?srsltid=AfmBOor328Kh0PmZBsgWBKornVRW12GPn3Wrz2zRPBNzsClPeNi-9WR7 

From this study, we can assume that Dyson OnTrac headphones have a negligible and unquantifiable market share as they are a relatively new product from a company not traditionally present in the headphone market. Furthermore, since it is a newer product, there is no historical sales data or established adoption pattern to rely on. To estimate its potential market impact, we can use Apple’s market share as a benchmark and assume that Dyson, being a new entrant with limited presence in the audio segment, might capture a small fraction of that market. For the purpose of forecasting, we conservatively estimate that Dyson could reach approximately 5% of Apple AirPods’ market potential. This allows us to use the Bass Diffusion Model parameters derived from AirPods to simulate Dyson OnTrac’s potential adoption over the next several years.
Below, we will try to predict Dyson OnTrac' sales based on this methodology that I explained above.


```python
dyson_market_potential = M * 0.05  

years_future_dyson = np.arange(0, 20)  #We will predict 20 years from the release date of Dyson OnTrac headphones.

predicted_dyson = bass_model(years_future_dyson, p, q, dyson_market_potential)

years_calendar_dyson = np.array(range(2025, 2025 + len(years_future_dyson)))
dyson_adoption_df = pd.DataFrame({
    'Year': years_calendar_dyson,
    'Yearly Adoption of Dyson': predicted_dyson,
    'Cumulative Adoption of Dyson': np.cumsum(predicted_dyson)
})

print("\nForecasted Adoption for Dyson OnTrac:")
print(dyson_adoption_df.round(2))


plt.figure(figsize=(10, 6))

#Here, we will plot the yearly adoption.
plt.subplot(2, 1, 1)
plt.plot(years_calendar_dyson, predicted_dyson, marker='o', color='pink')

plt.title('Forecasted Yearly Adoption of Dyson OnTrac headphones')

plt.xlabel('Year')

plt.ylabel('Yearly Adoption')
plt.xticks(years_calendar_dyson)
plt.grid(True)

#And here we will plot the cumulative adoption.

plt.subplot(2, 1, 2)
plt.plot(years_calendar_dyson, np.cumsum(predicted_dyson), marker='o', color='blue')

plt.title('Forecasted Cumulative Adoption of Dyson OnTrac headphones')

plt.xlabel('Year')

plt.ylabel('Cumulative Adoption')
plt.xticks(years_calendar_dyson)
plt.grid(True)

plt.tight_layout()
plt.show()



```

    
    Forecasted Adoption for Dyson OnTrac:
        Year  Yearly Adoption of Dyson  Cumulative Adoption of Dyson
    0   2025                      1.30                          1.30
    1   2026                      2.12                          3.42
    2   2027                      3.18                          6.60
    3   2028                      4.24                         10.84
    4   2029                      4.86                         15.70
    5   2030                      4.67                         20.37
    6   2031                      3.79                         24.16
    7   2032                      2.68                         26.84
    8   2033                      1.72                         28.56
    9   2034                      1.03                         29.59
    10  2035                      0.60                         30.19
    11  2036                      0.34                         30.52
    12  2037                      0.19                         30.71
    13  2038                      0.10                         30.82
    14  2039                      0.06                         30.87
    15  2040                      0.03                         30.91
    16  2041                      0.02                         30.92
    17  2042                      0.01                         30.93
    18  2043                      0.01                         30.94
    19  2044                      0.00                         30.94
    


    
![png](output_19_1.png)
    


**Analysis and Interpretation of the Predicted results:**

From the yearly forecasted prediction plot that we can see above, it becomes evidently clear that Dyson OnTrac headphones will start with relatively low adoption rate in 2025 but it will grow rapidly over the next few years. Then, it will peak around 2029 with approximately 4.8 million units. After this peak, yearly adoption will gradually decli, which just shows that that most of the potential market is already being captured, so there are no new buyers remaining to be adopted. By 2044, yearly adoption actually reaches zero, which suggests that almost all potential customers have already adopted the product.

When we look at the cumulative forecasted prediction plot, we see that essentially it just shows the total number of the product sold over time. It grows quickly in the starting years, which shows that the Dyson OnTrac headphones are starting to catch on with consumers.  By 2030, roughly two-thirds of the estimated market potential is already reached. By 2044, total adoption are positioned at about 30.94 million units, reaching the market potential we estimated for Dyson(5% of AirPods’ market). 

If we look at the bigger picture, we see that the adoption pattern follows a typical Bass diffusion curve. It starts slowly and gradually, it accelerates due to imitation. Then it peakes at one point and then it starts slowly decreasing as the market saturates. 
Furthermore, the peak adoption occurs about 4–5 years after launch, which is typical for innovative consumer electronics in a niche market.
The model suggests that Dyson OnTrac has potential for significant growth but will remain much smaller than a market leader like Apple AirPods.



**The scope of the market chosen for this project:**

In this project, I decided to integrate a global perspective rather than focusing on a single country. Dyson OnTrac headphones are designed for a broad market, and their potential demand is not limited to any specific region. Similar past innovations in premium audio devices, such as Apple AirPods, have followed global adoption trends rather than being confined to one country. Choosing a global scope, in my opinion, helps the project be more accurate because it takes into account the effects of marketing, social influence, and word-of-mouth across multiple markets. This means that it will offer a more comprehensive and extensive picture of Dyson OnTrac’s diffusion potential.


**Estimation of the number of adopters by period:**

Based on the Bass Model parameters, the forecasted yearly adoption for Dyson OnTrac forms a pattern like this:

*Number of adopters by 2025:* approximately **1.3** million 

*Number of adopters by 2030:* approximately **4.7** million

*Number of adopters by 2035:*  approximately **0.6** million

*Number of adopters by 2044:* approximately **30.94** million.

