# Uiverse — analisi tecnica degli originali HTML/CSS

Questa analisi usa i **57 sorgenti originali realmente letti** dal repository Design-App; ciascun file è ancorato a un blob SHA Git corrispondente a Uiverse Galaxy. Non equivale a test Flutter, emulatore, screenshot o QA visiva del componente.

## Risultati statici

- **57 sorgenti**; 35 con almeno una animazione @keyframes; 16 con selettori :hover; 18 con SVG incorporato; 12 con effetti 3D; 26 con gradienti.

- INFINITE_ANIMATION_WITHOUT_REDUCED_MOTION: 32 file (segnale da valutare, **non** fallimento runtime dimostrato).
- HOVER_ONLY_PATTERN: 13 file (segnale da valutare, **non** fallimento runtime dimostrato).
- GLOBAL_CSS_SELECTOR_POTENTIAL_COLLISION: 2 file (segnale da valutare, **non** fallimento runtime dimostrato).
- HEAVY_SOURCE_REVIEW: 3 file (segnale da valutare, **non** fallimento runtime dimostrato).

## Componenti di riferimento da valutare prioritariamente

- **[UIV-014 — ElSombrero2/tricky-robin-67](https://uiverse.io/ElSombrero2/tricky-robin-67)**: CARD; tag originali card, flip, 2 keyframes. [Codice](../CODICE_SORGENTE/UIV-014_original.html). Card flip: prototipo Ricordi/collezioni, non hover-only.
- **[UIV-019 — JkHuger/new-deer-97](https://uiverse.io/JkHuger/new-deer-97)**: LOADER; tag originali loader, astronaut, 2 keyframes. [Codice](../CODICE_SORGENTE/UIV-019_original.html). Loader illustrato astronauta: attenzione a performance e coerenza prodotto.
- **[UIV-021 — JohnnyCSilva/black-rabbit-68](https://uiverse.io/JohnnyCSilva/black-rabbit-68)**: CARD; tag originali card, crypto, bitcoin, rotating, 1 keyframes. [Codice](../CODICE_SORGENTE/UIV-021_original.html). Coin/crypto card: possibile CashMate, non insinuare dati finanziari reali.
- **[UIV-022 — Lakshay-art/curvy-earwig-22](https://uiverse.io/Lakshay-art/curvy-earwig-22)**: INPUT; tag originali input, 2 keyframes. [Codice](../CODICE_SORGENTE/UIV-022_original.html). Input con effetti luce: ricerca Notes solo con accessibilità e contrasto.
- **[UIV-025 — Nawsome/ancient-yak-42](https://uiverse.io/Nawsome/ancient-yak-42)**: LOADER; tag originali loader, compass, 4 keyframes. [Codice](../CODICE_SORGENTE/UIV-025_original.html). Compass loader: candidate TrailPath, Wonderlog, CamperBoss.
- **[UIV-039 — SelfMadeSystem/pretty-treefrog-77](https://uiverse.io/SelfMadeSystem/pretty-treefrog-77)**: LOADER; tag originali animation, gradient, loader, spinner, text animation, animated, gradients, svg, 4 keyframes. [Codice](../CODICE_SORGENTE/UIV-039_original.html). Spinner/gradienti: attenzione a animazioni, contrasto e stato reale.
- **[UIV-088 — mobinkakei/great-skunk-8](https://uiverse.io/mobinkakei/great-skunk-8)**: SWITCH; tag originali neumorphism, switch, 0 keyframes. [Codice](../CODICE_SORGENTE/UIV-088_original.html). Switch neumorfico: candidate Battery Guard/utility, deve riflettere stato reale.

## Archivio analisi macchina

- [Analisi codice 1](./ANALISI_CODICE_PART_01.json)
- [Analisi codice 2](./ANALISI_CODICE_PART_02.json)
- [Analisi codice 3](./ANALISI_CODICE_PART_03.json)
- [Analisi codice 4](./ANALISI_CODICE_PART_04.json)

## Lavoro non attestato

È stata fatta **lettura statica** dei source snapshot e rilevazione euristica dei rischi CSS. Non è stato eseguito rendering del componente, test accessibilità, porting Flutter o Compose, né analisi degli asset esterni uno per uno. I 43 Favorites senza HTML/CSS originale sono nel [registro dei mancanti](./CODICE_NON_REPERITO.md).
