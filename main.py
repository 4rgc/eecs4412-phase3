import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

data = pd.read_csv("aggregated.csv")
data.dropna(inplace=True)
data.set_index("Date", inplace=True)

baskets = data.applymap(lambda x: 1 if x > 0 else 0)

min_support = 0.01
frequent_itemsets = apriori(baskets, min_support=min_support, use_colnames=True)

frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))

frequent_itemsets = frequent_itemsets[frequent_itemsets['length'] >= 2]

frequent_itemsets.sort_values(by='support', ascending=False, inplace=True)

print("\nTop 10 frequent itemsets:")
print(frequent_itemsets.head(10))

frequent_itemsets1 = apriori(baskets, min_support=min_support, use_colnames=True)

frequent_itemsets1['length'] = frequent_itemsets1['itemsets'].apply(lambda x: len(x))

frequent_itemsets1 = frequent_itemsets1[frequent_itemsets1['length'] < 2]

frequent_itemsets.sort_values(by='support', ascending=False, inplace=True)

print("\nsupport  of stock")
print(frequent_itemsets1.head(10))
