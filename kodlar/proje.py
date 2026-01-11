# 1. ADIM: Kullanıcıdan web sayfasında görünecek kişisel bilgileri alıyoruz
ad_soyad = input("Adınız ve Soyadınız: ")
biyografi = input("Kısa biyografi: ")
dersler = input("Hangi dersleri alıyorsunuz: ")

# 2. ADIM: HTML şablonunu hazırlıyoruz
# Python'daki f-string (f"...") yapısını kullanarak kullanıcıdan alınan değişkenleri
# HTML etiketlerinin (h1, p, b vb.) arasına yerleştiriyoruz.
html_kodum = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Kişisel Sayfam</title>
</head>
<body style="background-color: #f0f0f0; text-align: center;">

    <h1 style="color: blue;">{ad_soyad}</h1>

    <p><b>Kısa Biyografi:</b> <i>{biyografi}</i></p>

    <h3 style="background-color: lightgrey;">Aldığım Dersler</h3>

    <p>
        {dersler}
    </p>

    <hr>
    <p><small>Bu sayfa Python tarafından otomatik oluşturuldu.</small></p>

</body>
</html>
"""

# 3. ADIM: Oluşturulan metni fiziksel bir .html dosyası olarak kaydediyoruz
# 'w' parametresi yazma modunu, 'utf-8' ise Türkçe karakter desteğini sağlar.
with open("index.html", "w", encoding="utf-8") as dosya:
    dosya.write(html_kodum)

print("index.html başarıyla oluşturuldu! Klasörünüzü kontrol ediniz.")
