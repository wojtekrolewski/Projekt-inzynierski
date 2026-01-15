# Projekt-inzynierski 2023
# Box-Counting Dimension for Image Analysis

## 1. Problem
Celem projektu było opracowanie narzędzia do wyznaczania wymiaru pudełkowego obiektów na obrazach
jako miary ich złożoności geometrycznej.

## 2. Dane
- obrazy binarne / w skali szarości
- dane syntetyczne oraz rzeczywiste obrazy testowe

## 3. Podejście
Zaimplementowano algorytm box-counting polegający na:
- nakładaniu siatek o różnych rozmiarach
- zliczaniu pudełek zawierających fragment obiektu
- estymacji wymiaru jako nachylenia zależności log-log

## 4. Implementacja
- Python
- NumPy
- przetwarzanie obrazów
- modułowa struktura kodu

## 5. Przykładowe wyniki
<img width="431" height="286" alt="image" src="https://github.com/user-attachments/assets/45b2efe7-68ae-43dc-a4d7-4ce8778e2b5e" />
<img width="303" height="397" alt="image" src="https://github.com/user-attachments/assets/110641e9-db05-4116-a415-6afd43f8ed19" />
<img width="450" height="267" alt="image" src="https://github.com/user-attachments/assets/f122f349-565d-4dca-97ed-ecc7ad8c6b1d" />
<img width="283" height="362" alt="image" src="https://github.com/user-attachments/assets/586e2928-556c-4486-9fd0-a381cfae73b6" />




## 6. Wnioski i ograniczenia
- wrażliwość na jakość binarnej segmentacji
- wpływ rozdzielczości obrazu na stabilność wyniku

## 7. Dalszy rozwój
- możliwość integracji z metodami ML
- automatyczna segmentacja obrazu
