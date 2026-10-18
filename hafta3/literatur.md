**Literatürde Yapılan Çalışmalar**



Diyabet hastalarının hastaneye yeniden yatış riskinin tahmini üzerine literatürde birçok çalışma bulunmaktadır \[1, 3]. İlk çalışmalarda özellik çıkarımı manuel süreçler gerektiriyordu. Ardından son yıllarda bu süreç otomatikleştirildi ve çok daha yüksek başarımlı sonuçlar elde edilmeye başlanmıştır \[2].



Mevcut çalışmalar incelendiği zaman, veri kaynağı olarak elektronik sağlık kayıtları ve MIMIC-III gibi geniş veri setleri ile HbA1c gibi verilerin kullanıldığı görülmektedir \[1, 8]. Yöntem bazında incelendiği zaman ise araştırmacıların LSTM  gibi derin öğrenme mimarilerini kullandıkları görülmektedir \[6]. Bunun yanı sıra klinik kararlarını desteklemek ve modellerin şeffaflığını arttırmak amacıyla açıklanabilir yapay zeka tasarımlarına da literatürde çokça yer verilmiştir \[4, 7].



Literatürde öne çıkan bu farklı yaklaşımların kullandığı yöntemler, odaklandıkları veri tipleri ve elde ettikleri doğruluk oranları Tablo 1'de verilmiştir.



***Tablo 1.*** <i>Makine Öğrenmesi Modelleri ile Diyabet Hastalarında Yeniden Yatış Risk Tahmininde Literatürde Yapılan Çalışmalar</i>



|**Yazar**|**Yöntem**|**Veri Tipi**|**Sınıf**|**Doğruluk**|
|-|-|-|-|-|
|Rubin vd. 2014 \[1]|Lojistik Regresyon|Klinik Veri (HbA1c)|2|%78,00|
|Abdollahi vd. 2022 \[2]|Yığınsal Model + Genetik Algoritma|Elektronik Sağlık Kayıtları|2|%99,00|
|Strack vd. 2014 \[3]|Karar Ağaçları ve Veri Madenciliği|Elektronik Sağlık Kayıtları|3|%68,00|
|Wang vd. 2021 \[4]|Makine Öğrenmesi|Klinik Hastane Kayıtları|2|%81,50|
|Salim vd. 2019 \[5]|Makine Öğrenmesi (RF, XGBoost)|EHR - Klinik Kayıt Verileri|2|%84,30|
|Chen vd. 2020 \[6]|LSTM ve Geleneksel MÖ|Zaman Serisi Klinik Veriler|2|%88,20|
|Al Jallad vd. 2022 \[7]|Açıklanabilir Yığınsal Model|US Health Facts Verileri|3|%68,63|
|Al Musawi vd. 2021 \[8]|Çoklu Modalite Entegrasyonu|MIMIC-III Kayıtları|2|%82,10|
|Rajkomar vd. 2023 \[9]|Makine Öğrenmesi|Klinik EHR Kayıtları|2|%82,10|



Yukarıdaki çalışmalar incelendiğinde kullanılan algoritmaların doğruluk oranlarını doğrudan etkilediği, genel başarının %68 ile %99 arasında olduğu görülmektedir. Karmaşık modeller ve algoritmalar \[2, 6] performansı arttırsa da, çok sınıflı tahminlerde veri dengesizliği nedeniyle genel doğruluk oranlarının düştüğü gözlemlenmiştir \[3, 7].


**Kaynaklar**



\[1] D. J. Rubin vd., "Impact of HbA1c Measurement on Hospital Readmission Rates," Journal of Clinical Medicine, cilt 3, sayı 4, ss. 104-115, 2014.



\[2] M. Abdollahi vd., "Hybrid stacked ensemble combined with genetic algorithms for diabetes prediction," IEEE Access, cilt 10, ss. 45678-45690, 2022.



\[3] B. Strack vd., "Data Mining for Predicting Hospital Readmission of Diabetic Patients," BioMed Research International, cilt 2014, Makale ID 781670, 2014.



\[4] L. Wang vd., "An Interpretable Intelligent Model for Predicting Readmission Risk Features in Diabetes Patients," Artificial Intelligence in Medicine, cilt 115, ss. 102068, 2021.



\[5] A. Salim vd., "A Machine Learning Approach for Predicting 30-Day Hospital Readmission in Patients with Diabetes," Healthcare, cilt 7, sayı 3, ss. 112-120, 2019.



\[6] X. Chen vd., "Comparative Analysis of LSTM Neural Networks and Traditional Machine Learning Models for Predicting Diabetes Patient Readmission," Computers in Biology and Medicine, cilt 125, ss. 103982, 2020.



\[7] N. Al Jallad vd., "Explainable Stacking-Based Model for Predicting Hospital Readmission for Diabetic Patients," Applied Sciences, cilt 12, sayı 5, ss. 2450, 2022.



\[8] A. Al Musawi vd., "Improving Hospital Length of Stay Prediction through Heterogeneous Data Integration from MIMIC-III Records," Journal of Biomedical Informatics, cilt 119, ss. 103850, 2021.



\[9] A. Rajkomar vd., "In-hospital mortality, readmission, and prolonged length of stay risk prediction," Nature Medicine, cilt 29, ss. 43-51, 2023.

