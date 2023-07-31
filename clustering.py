import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.cluster import KMeans
from sklearn.preprocessing import Normalizer

companies_dict = {
    'Amazon': 'AMZN',
    'Apple': 'AAPL',
    'Intel': 'INTC',
    'IBM': 'IBM',
    'Microsoft': 'MSFT',
    'Tesla': 'TSLA',
    'Oracle': 'ORCL',
    'Google': 'GOOG',
    'Nvidia': 'NVDA',
    'Meta': 'META'

}
companies = sorted(companies_dict.items(), key=lambda x: x[1])
data_source = 'yahoo'
start_date = '2021-06-08'
end_date = '2023-06-08'
panel_data = yf.download(list(companies_dict.values()), start=start_date, end=end_date)

stock_close = panel_data['Close']
stock_open = panel_data['Open']
stock_close = np.array(stock_close).T
stock_open = np.array(stock_open).T
row, col = stock_close.shape
movements = np.zeros([row, col])
for i in range(0, row):
    movements[i, :] = np.subtract(stock_close[i, :], stock_open[i, :])
for i in range(0, len(companies)):
    print('{}, Change: {}'.format(companies[i][0], sum(movements[i][:])))

normalizer = Normalizer()

new = normalizer.fit_transform(movements)

print('new max: ' + str(new.max()))
print('new min: ' + str(new.min()))
print('new mean: ' + str(new.mean()))

normalizer = Normalizer()
kmeans = KMeans(n_clusters=5, max_iter=1000)
pipeline = make_pipeline(normalizer, kmeans)
pipeline.fit(movements)
labels = pipeline.predict(movements)
df = pd.DataFrame({'labels': labels, 'companies': companies})
print(df.sort_values('labels'))

kmeans_5 = KMeans(n_clusters=5, max_iter=1000)
pipeline_5 = make_pipeline(normalizer, kmeans_5)
pipeline_5.fit(movements)
sse_k5 = pipeline_5.named_steps['kmeans'].inertia_

kmeans_7 = KMeans(n_clusters=7, max_iter=1000)
pipeline_7 = make_pipeline(normalizer, kmeans_7)
pipeline_7.fit(movements)
sse_k7 = pipeline_7.named_steps['kmeans'].inertia_

print("SSE for K=5:", sse_k5)
print("SSE for K=7:", sse_k7)