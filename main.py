# Task 1:
historical_data = []  

with open("orcl_rsi.csv") as file:
    header = file.readline().strip().split(",")

    for line in file:
        data_row = line.strip().split(",")
        data_dict = {header[i]: data_row[i] for i in range(len(header))}
        historical_data.append(data_dict)

for data_point in historical_data:
    print(data_point)
    
# Task 2:
def calculate_sma(data, window):
    sma_values = []
    for i in range(len(data)):
        if i < window - 1:
            sma_values.append(None)
        else:
            closing_prices = [float(data[j]["Close"]) for j in range(i - window + 1, i + 1)]
            sma = sum(closing_prices) / window
            sma_values.append(sma)
    return sma_values

def calculate_rsi(data, window):
    rsi_values = []
    gains = []
    losses = []

    for i in range(len(data)):
        if i == 0:
            rsi_values.append(None)
            continue

        current_close = float(data[i]["Close"])
        previous_close = float(data[i - 1]["Close"])
        price_difference = current_close - previous_close

        if price_difference > 0:
            gains.append(price_difference)
            losses.append(0)
        elif price_difference < 0:
            gains.append(0)
            losses.append(abs(price_difference))
        else:
            gains.append(0)
            losses.append(0)

        if i >= window:
            avg_gain = (sum(gains[-window:]) + gains[-1]) / window
            avg_loss = (sum(losses[-window:]) + losses[-1]) / window
            rs = avg_gain / avg_loss if avg_loss != 0 else None
            rsi = 100 - (100 / (1 + rs)) if rs is not None else None
            rsi_values.append(rsi)
        else:
            rsi_values.append(None)

    return rsi_values

# Calculating SMA and RSI values and printing them
sma_values = calculate_sma(historical_data, window=5)
rsi_values = calculate_rsi(historical_data, window=14)

print("SMA Values are:", sma_values)
print("RSI Values are:", rsi_values)

# Task 3: Fixing the file writing operations
with open("orcl_rsi.csv", "w") as rsi_file:
    rsi_file.write("Date,RSI\n")
    for i in range(len(historical_data)):
        rsi_file.write(f"{historical_data[i]['Date']},{rsi_values[i]}\n")