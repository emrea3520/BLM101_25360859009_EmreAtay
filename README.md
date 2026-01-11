### Öğrenci Bilgileri: Emre Atay  25360859009 

### Proje Konusu: Ağlar, İnternet ve HTML 

### YouTube Sunum Linki:
...

### Kod Açıklaması:

### Kod Ne Yapıyor?
Bu Python programı, kullanıcıyla etkileşime girerek aldığı verileri (ad, biyografi, dersler) önceden tanımlanmış bir HTML şablonuna işler. Sonuç olarak, kullanıcının bilgilerini içeren, stil verilmiş (CSS içeren) bir `index.html` dosyası oluşturur. Bu, web sayfalarının temel yapısını ve dinamik içerik oluşturma mantığını basit bir seviyede gösterir.

### Kullanılan Kütüphaneler
* **Standart Python Kütüphaneleri:** Bu projede harici bir kütüphane kurulumuna (pip install vb.) gerek duyulmamıştır. Python'un temel `input-output` (giriş-çıkış) ve `file handling` (dosya yönetimi) özellikleri kullanılmıştır.

### Algoritma Mantığı
Programın çalışma algoritması şu adımlardan oluşur:
1. **Veri Toplama:** `input()` fonksiyonu kullanılarak kullanıcıdan metinsel veriler alınır.
2. **Metin Birleştirme (Templating):** Python'un `f-string` özelliği kullanılarak, HTML etiketleri arasına kullanıcının girdiği değişkenler yerleştirilir.
3. **Dosya İşlemleri:** `with open()` yapısı kullanılarak sistemde `index.html` adında bir dosya açılır (veya varsa üzerine yazılır).
4. **Kalıcı Kayıt:** Hazırlanan HTML bloğu bu dosyanın içine yazılarak işlem tamamlanır.
