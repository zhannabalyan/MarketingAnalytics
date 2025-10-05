# Bass Diffusion Model Analysis for Dyson OnTrac headphones

## Project Overview
This project aims to use the Bass Diffusion Model to forecast adoption of an innovation like the Dyson OnTrac headphones.This is done by by comparing it to the market adoption pattern of Apple AirPods.

## Project Contents:

- `BassModel.ipynb` : Jupyter notebook with thorough analysis.
- `helper_functions.py` : information about the helper functions
- `script1.py` : information about the data and the Bass Model.
- `script2.py` : information about the prediction and forecasts.
- `img/` : Folder containing images of the plots.
- `data/` : Folder containing the dataset used.
- `report/` : Folder containing PDF and markdown report of BassModel.
- `README.md` : This file.

## Innovation Selection process
- `Innovation selected from TIME` : Dyson OnTrac Headphones
- `Lookalike innovation` : Apple Airpods

## Methodology
- `Innovation Selection` : Chosen Apple AirPods as a reference model for the Dyson OnTrac Headphones due to similarities in market segment and product features.
- `Data Selection` : Collected historical sales data for Apple AirPods (2017–2024) and market share info.
- `Bass Model definition` : Implemented the Bass Model in Python using curve_fit to estimate parameters.
- `Forecasting` : Forecasted yearly and cumulative adoption for AirPods and Dyson OnTrac(assumed Dyson has 5% of AirPods’ market share).
- `Visualization` : Displayed the results with Matplotlib plots.

## Instructions
1. Open the Jupyter notebook (`BassModel.ipynb`) to see the analysis.
2. Plots are saved in the `img/` folder.
3. The report is in the `report/` folder as PDF.

## References
- Statista Historical Sales Data for Apple Airpods: https://www.statista.com/statistics/1421624/apple-airpods-unit-sales/ 
- Statista Headphone Market Share: https://www.statista.com/chart/26791/most-popular-headphone-brands-in-the-us/ 
- TIME Best Inventions of 2024: https://time.com/7094600/dyson-ontrac/
