!A better version has been made. It is in the testing phase.!
### English Introduction

This Python script showcases an advanced application developed using PyQt6, focusing on the brute-force decryption of AES-encrypted files. Leveraging the `Crypto.Cipher` module from the PyCryptodome library, the script attempts to decrypt data by systematically iterating over all possible combinations of keys and initialization vectors (IVs) within the AES encryption standard's constraints. The core of this application, the `DecryptorThread` class, extends `QThread` to perform decryption operations in a separate thread, preventing the graphical user interface (GUI) from becoming unresponsive during the computationally intensive decryption process.

Upon launching the application, users are greeted with a GUI that allows for the selection of an encrypted file via a file dialog. Following the selection, the application begins the brute-force decryption process, iterating through a predefined key space (256 possibilities for each byte of the key and IV, resulting in \(256^{32}\) potential key combinations for a 256-bit key and \(256^{16}\) for a 128-bit IV) until the correct combination is found or all possibilities are exhausted. Progress is visually represented through a QProgressBar, offering real-time feedback on the decryption attempt's progress.

Notably, the application emits signals upon significant events, such as updating progress or successfully decrypting the file, facilitating communication between the decryption thread and the main GUI thread. This design pattern enhances the application's responsiveness and user experience by separating the decryption logic from the GUI updates.

In summary, this script demonstrates the practical application of brute-force decryption methods against AES encryption, wrapped in a user-friendly PyQt6 interface. It is a powerful tool for educational purposes, illustrating the computational challenges associated with decrypting modern encryption algorithms without prior knowledge of the key or IV.

### Türkçe Tanıtım

Bu Python betiği, PyQt6 kullanılarak geliştirilmiş, AES şifreli dosyaların kaba kuvvet ile deşifre edilmesine odaklanan ileri düzey bir uygulamayı sergilemektedir. PyCryptodome kütüphanesinin `Crypto.Cipher` modülünü kullanarak, AES şifreleme standardının sınırlamaları dahilinde tüm olası anahtar ve başlatma vektörü (IV) kombinasyonlarını sistematik olarak deneyerek verileri deşifre etmeye çalışır. Uygulamanın çekirdeği olan `DecryptorThread` sınıfı, `QThread`'i genişleterek deşifreleme işlemlerini ayrı bir iş parçacığında gerçekleştirir, bu da yoğun hesaplama gerektiren deşifreleme işlemi sırasında grafiksel kullanıcı arayüzünün (GUI) yanıt vermez hale gelmesini önler.

Uygulama başlatıldığında, kullanıcılar şifreli bir dosyayı dosya diyalogu aracılığıyla seçebilecekleri bir GUI ile karşılanır. Seçim yapıldıktan sonra, uygulama kaba kuvvet deşifreleme işlemine başlar, önceden tanımlanmış bir anahtar uzayı üzerinde iterasyon yapar (256 bitlik bir anahtar için \(256^{32}\), 128 bitlik bir IV için \(256^{16}\) olası anahtar kombinasyonu) doğru kombinasyon bulunana kadar veya tüm olasılıklar tükenene kadar devam eder. İlerleme, bir QProgressBar aracılığıyla görsel olarak temsil edilerek, deşifreleme girişiminin ilerlemesi hakkında gerçek zamanlı geri bildirim sunar.

Özellikle, uygulama, ilerlemeyi güncelleme veya dosyanın başarıyla deşifre edilmesi gibi önemli olaylarda sinyaller yayınlar, deşifreleme iş parçacığı ile ana GUI iş parçacığı arasında iletişimi kolaylaştırır. Bu tasarım deseni, deşifreleme mantığını GUI güncellemelerinden ayırarak uygulamanın yanıt verme yeteneğini ve kullanıcı deneyimini artırır.

Özetle, bu betik, kullanıcı dostu bir PyQt6 arayüzüne sarılmış olarak AES şifrelemesine karşı kaba kuvvet deşifreleme yöntemlerinin prat

ik uygulamasını gösterir. Anahtar veya IV hakkında önceden bilgi sahibi olmadan modern şifreleme algoritmalarının deşifre edilmesiyle ilişkili hesaplama zorluklarını öğretici amaçlar için güçlü bir araç olarak sunar.
