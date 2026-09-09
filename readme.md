# Space Shooter 2D

Klasyczna gra zręcznościowa typu "Top-Down Shooter" stworzona w języku Python. Projekt demonstruje praktyczne zastosowanie programowania obiektowego (OOP), trygonometrii do obliczania wektorów ruchu oraz implementację mechanik fizyki.

## Technologie
* **Język:** Python 3.x
* **Biblioteki:** 
  * `pygame` - renderowanie grafiki, obsługa pętli gry i zdarzeń wejścia.
  * `numpy` - optymalizacja zaawansowanych obliczeń trygonometrycznych.

## Główne Funkcjonalności

* **Płynne sterowanie i wektoryzacja ruchu:** Statek gracza dynamicznie obraca się w stronę kursora myszy. Kąty i wektory przesunięcia są na bieżąco przeliczane za pomocą funkcji trygonometrycznych (`np.atan`, `np.sin`, `np.cos`).
* **Mechanika grawitacji:** Na mapie generowane są czarne dziury, które stale modyfikują trajektorię obiektów (przeciwników, gracza i pocisków). Obliczenia opierają się na uproszczonym prawie powszechnego ciążenia (`F = G * (m1 * m2) / r^2`).
* **Wielowątkowa detekcja kolizji:** Zoptymalizowane sprawdzanie granic ekranu (bounding box) oraz precyzyjna weryfikacja dystansu między obiektami przy użyciu twierdzenia Pitagorasa.
* **Separacja logiki:** Ścisły podział na modele obiektowe, warstwę analityczną i centralną konfigurację ułatwiającą balansowanie gry.

## Struktura Projektu

| Katalog / Plik | Odpowiedzialność |
| :--- | :--- |
| **`assets/`** | Zbiór plików graficznych (sprite'y statku, przeciwników, czarnej dziury i eksplozji). |
| **`classes/`** | Definicje klas odpowiedzialnych za stan i zachowanie obiektów (`Game`, `Ship`, `Alien`, `Blackhole`, `Bullet`). |
| **`functions.py`** | Zbiór czystych funkcji matematycznych (`calculate_angle`, `calculate_vectors`), co ułatwia testowanie i zapobiega duplikacji kodu w klasach. |
| **`settings.py`** | Centralny plik konfiguracyjny (zarządzanie masą obiektów, stałą grawitacji, prędkością, paletą kolorów). |
| **`main.py`** | Punkt wejścia aplikacji. Inicjalizuje środowisko, kontroluje FPS (`clock.tick`) oraz przechwytuje zdarzenia użytkownika. |

## Uruchomienie Projektu

1. Sklonuj repozytorium na swój dysk lokalny.
2. Upewnij się, że posiadasz zainstalowanego Pythona w wersji 3.x.
3. Zainstaluj wymagane zależności za pomocą menedżera pakietów `pip`:
   ```bash
   pip install -r requirements.txt
   ```
4. Uruchom grę
    ```bash
    python main.py
    ```