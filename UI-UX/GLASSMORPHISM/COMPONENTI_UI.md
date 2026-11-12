# Componenti UI/UX di Glassmorphism

## Elementi utili da studiare e ricreare

- Card glass sopra fotografie
- Bottom sheet e modali stratificate
- Navbar e toolbar semitrasparenti

## Token da estrarre dai futuri riferimenti

- Colori semantici, ruoli e contrasto (senza presumere che i colori di una reference siano già quelli definitivi).
- Tipo di font, scala tipografica, peso, interlinea.
- Spacing, radius, border, shadow, elevation/blur (solo dove presenti).
- Griglia mobile/tablet, safe area, tastiera, gesture e component states.
- Motion duration/easing, feedback di stato e rispetto reduced-motion.
- Loading, empty, offline, error e disabled states.

## Vincoli prima dell'adozione

Fallback opaco in caso di contrasto scarso, riduzione trasparenze e dispositivi meno potenti; verificare costo blur/GPU.

**Implementazione:** nessuna, per ora. Estrazione di pattern ammessa solo in progetto approvato con validazione su codice proprio e licenze compatibili.
