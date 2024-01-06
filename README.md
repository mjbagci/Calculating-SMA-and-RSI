# Calculating-SMA-and-RSI
Bu proje, finansal veriler üzerinde basit hareketli ortalama (SMA) ve göreceli güç endeksi (RSI) hesaplamalarını gerçekleştirir ve sonuçları bir dosyaya kaydeder.

Kullanım
1. Veri Yüklemek
Proje, "orcl_rsi.csv" adlı bir dosyadan finansal verileri yükler. Bu dosyanın uygun formatta olduğundan emin olun.

python
Copy code
# Task 1: Veri Yüklemek
historical_data = []  

with open("orcl_rsi.csv") as file:
    header = file.readline().strip().split(",")

    for line in file:
        data_row = line.strip().split(",")
        data_dict = {header[i]: data_row[i] for i in range(len(header))}
        historical_data.append(data_dict)

for data_point in historical_data:
    print(data_point)
2. SMA ve RSI Hesaplamak
Proje, finansal veriler üzerinde SMA ve RSI hesaplamak için iki fonksiyon içerir.

python
Copy code
# Task 2: SMA ve RSI Hesaplamak
def calculate_sma(data, window):
    # Fonksiyon içeriği

def calculate_rsi(data, window):
    # Fonksiyon içeriği
3. Sonuçları Kaydetmek
Proje, hesaplanan SMA ve RSI değerlerini "orcl_rsi.csv" adlı bir dosyaya kaydeder.

python
Copy code
# Task 3: Dosya Yazma İşlemlerini Düzeltmek
with open("orcl_rsi.csv", "w") as rsi_file:
    rsi_file.write("Date,RSI\n")
    for i in range(len(historical_data)):
        rsi_file.write(f"{historical_data[i]['Date']},{rsi_values[i]}\n")
Bağımlılıklar
Projenin çalışabilmesi için şu bağımlılıklara ihtiyaç vardır:

Python 3.x
Kurulum
Proje dosyalarını bilgisayarınıza indirin.
Ana dizinde terminal veya komut istemcisini açın.
pip install -r requirements.txt komutunu kullanarak gerekli bağımlılıkları yükleyin.
Lisans
Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasını inceleyin.
