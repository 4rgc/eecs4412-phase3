
supp_stock = [
    (0.547619, ('AAPL',), 1),
    (0.525794, ('GOOG',), 1),
    (0.525794, ('META',), 1),
    (0.523810, ('ORCL',), 1),
    (0.517857, ('MSFT',), 1),
    (0.515873, ('NVDA',), 1),
    (0.509921, ('IBM',), 1),
    (0.509921, ('TSLA',), 1),
    (0.482143, ('AMZN',), 1),
    (0.476190, ('INTC',), 1)
]

freq_item = [
    (0.440476, ('AAPL', 'MSFT'), 2),
    (0.424603, ('AAPL', 'GOOG'), 2),
    (0.410714, ('NVDA', 'AAPL'), 2),
    (0.404762, ('GOOG', 'MSFT'), 2),
    (0.402778, ('AAPL', 'META'), 2),
    (0.400794, ('GOOG', 'META'), 2),
    (0.398810, ('AAPL', 'AMZN'), 2),
    (0.392857, ('META', 'MSFT'), 2),
    (0.392857, ('NVDA', 'MSFT'), 2),
    (0.388889, ('NVDA', 'META'), 2)
]

def calculate_confidence(support_AB, support_A):
    return support_AB / support_A

sorted_rules = sorted(freq_item, key=lambda x: x[0], reverse=True)

print("Top 5 rules with highest confidence:")
for rule in sorted_rules[:5]:
    confidence = calculate_confidence(rule[0], supp_stock[rule[2] - 1][0])
    print(f"{rule[1][0]} -> {rule[1][1]} : {confidence}")

print("\nBottom 5 rules with lowest confidence:")
for rule in sorted_rules[-5:]:
    confidence = calculate_confidence(rule[0], supp_stock[rule[2] - 1][0])
    print(f"{rule[1][0]} -> {rule[1][1]} : {confidence}")
