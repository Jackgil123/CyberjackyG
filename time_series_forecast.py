import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA

data = pd.read_csv("C:\\Users\\1jack\\CyberjackyG\\datasets\\csvs\\monthly-beer-production-in-austr.csv", index_col='Month', parse_dates=True)
plot_acf(data['Monthly beer production'], lags=30)
plt.show()

plot_pacf(data['Monthly beer production'], lags=30)
plt.show()

model = ARIMA(data['Monthly beer production'], order=(2, 1, 2))
model_fit = model.fit()
print(model_fit.summary())
forecast = model_fit.forecast(steps=12)
print("Forecasted values for the next 12 months:")
