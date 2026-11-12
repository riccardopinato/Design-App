# Componenti UI/UX di Minimal Controls / Control Center

## Elementi utili da studiare e ricreare

- Quick Settings e pannelli di regolazione
- Slider, switch, icone, indicatori
- Widget per stato reale e azioni frequenti

## Token da estrarre dai futuri riferimenti

- Colori semantici, ruoli e contrasto (senza presumere che i colori di una reference siano già quelli definitivi).
- Tipo di font, scala tipografica, peso, interlinea.
- Spacing, radius, border, shadow, elevation/blur (solo dove presenti).
- Griglia mobile/tablet, safe area, tastiera, gesture e component states.
- Motion duration/easing, feedback di stato e rispetto reduced-motion.
- Loading, empty, offline, error e disabled states.

## Vincoli prima dell'adozione

Ogni controllo richiede etichetta/semantics, target almeno 48dp, stato attivo distinguibile e gesture non ambigue.

**Implementazione:** nessuna, per ora. Estrazione di pattern ammessa solo in progetto approvato con validazione su codice proprio e licenze compatibili.
