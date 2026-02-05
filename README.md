Ekran üzerindeki fare koordinatlarını anlık olarak takip eden ve tıklanan noktaları listeleyen bir yardımcı araçtır. Otomasyon projeleri ve script hazırlama süreçlerinde koordinat belirlemeyi kolaylaştırmak için tasarlanmıştır.

## Özellikler

* **Anlık Takip:** Fare hareket ettikçe X ve Y koordinatlarını gerçek zamanlı gösterir.
* **Tıkla ve Kaydet:** Ekranın herhangi bir yerine tıklandığında (uygulama odağı dışında olsa bile) o noktanın koordinatlarını listeye ekler.
* **Modern GUI:** CustomTkinter ile temiz ve anlaşılır arayüz.
* **Düşük Gecikme:** 100ms tazeleme oranıyla hassas takip.

## Kurulum

Gerekli kütüphaneleri yükleyin:

```
pip install customtkinter pyautogui mouse
```

## Kullanım

1. **BAŞLAT** butonuna basarak takibi aktif edin.
2. Fareyi ekranda hareket ettirerek koordinatları izleyin.
3. Kaydetmek istediğiniz noktaya sol tıklayın.
4. Koordinatlar alttaki kutuda listelenecektir. Buradan koordinatları kopyalayıp scriptlerinizde kullanabilirsiniz.
