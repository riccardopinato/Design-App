# Watermelon UI — audit di nove riferimenti richiesti (17/11/2026)

## Fonti

I nove URL esatti su DevLibraries sono stati tentati; il caricamento della pagina profonda non è riuscito. Pertanto nomi ed esempi di utilizzo provengono dalla richiesta dell'utente; i fatti tecnici sono verificati indipendentemente sul repository originale pubblico [WatermelonCorp/watermelon-platform](https://github.com/WatermelonCorp/watermelon-platform/tree/9d6defcf89880d0a00fbccad773c046bb51d7afb) fissato a commit `9d6defcf89880d0a00fbccad773c046bb51d7afb`, LICENSE MIT (blob `c76bf56983389c53194eecc9d088ac8de34debe1`). La piattaforma espone catalogo e sorgenti React con Motion, Vite e Tailwind. Non è Flutter, non è un'offerta di Flutter widgets.

### Tracciamento source-by-source

| Componente | Fonte verificata nel repository originale | Esito |
|---|---|---|
| [Carousel Slider](https://devlibraries.com/libraries/watermelon/carousel-slider) | [`src/data/contents/animated-components/carousel-slider/base.tsx`](https://github.com/WatermelonCorp/watermelon-platform/blob/9d6defcf89880d0a00fbccad773c046bb51d7afb/src/data/contents/animated-components/carousel-slider/base.tsx) blob `ccd0d565f1cd15ea44bf449ef7bdbfbc7cd0c25b`; metadata `src/data/contents/registry/carousel-slider.mdx` | SOURCE_FILE_READ |
| [Fractional Picker](https://devlibraries.com/libraries/watermelon/fractional-picker) | [`src/data/contents/animated-components/fractional-picker/base.tsx`](https://github.com/WatermelonCorp/watermelon-platform/blob/9d6defcf89880d0a00fbccad773c046bb51d7afb/src/data/contents/animated-components/fractional-picker/base.tsx) blob `b967c1465f20eca5d16034c97dcda180bc76def8`; metadata `src/data/contents/registry/fractional-picker.mdx` | SOURCE_FILE_READ |
| [Scrub Slider (base)](https://devlibraries.com/libraries/watermelon/scrub-slider-base) | [`src/data/contents/animated-components/scrub-slider/base.tsx`](https://github.com/WatermelonCorp/watermelon-platform/blob/9d6defcf89880d0a00fbccad773c046bb51d7afb/src/data/contents/animated-components/scrub-slider/base.tsx) blob `50dd8724adec082588cb4970463a37e65702f2d2`; metadata `src/data/contents/registry/scrub-slider.mdx` | SOURCE_FILE_READ |
| [Range Selection Slider](https://devlibraries.com/libraries/watermelon/range-selection-slider) | [`src/data/contents/animated-components/range-selection-slider/base.tsx`](https://github.com/WatermelonCorp/watermelon-platform/blob/9d6defcf89880d0a00fbccad773c046bb51d7afb/src/data/contents/animated-components/range-selection-slider/base.tsx) blob `c9d73a57572b4c6928f27ce9e2ed2b60e8edc67f`; metadata `src/data/contents/registry/range-selection-slider.mdx` | SOURCE_FILE_READ |
| [Swap Form](https://devlibraries.com/libraries/watermelon/swap-form) | [`src/data/contents/animated-components/swap-form/base.tsx`](https://github.com/WatermelonCorp/watermelon-platform/blob/9d6defcf89880d0a00fbccad773c046bb51d7afb/src/data/contents/animated-components/swap-form/base.tsx) blob `2b64bfab4cca53260b4d4ccd6364b0c856d00768`; metadata `src/data/contents/registry/swap-form.mdx` | SOURCE_FILE_READ |
| [Text Gradient](https://devlibraries.com/libraries/watermelon/text-gradient) | Nessun file/metadata esatto con quel nome rintracciato nella baseline | EXACT_SOURCE_NOT_LOCATED |
| [Dialog Stack (base)](https://devlibraries.com/libraries/watermelon/dialog-stack-base) | [`src/data/contents/animated-components/dialog-stack/base.tsx`](https://github.com/WatermelonCorp/watermelon-platform/blob/9d6defcf89880d0a00fbccad773c046bb51d7afb/src/data/contents/animated-components/dialog-stack/base.tsx) blob `0b0e401dc9ca5957bc048885bf8b29449cf24932`; metadata `src/data/contents/registry/dialog-stack.mdx` | SOURCE_FILE_READ |
| [Notification List](https://devlibraries.com/libraries/watermelon/notification-list) | Nessun file/metadata esatto con quel nome rintracciato nella baseline | EXACT_SOURCE_NOT_LOCATED |
| [Flip Clock](https://devlibraries.com/libraries/watermelon/flip-clock) | Nessun file/metadata esatto con quel nome rintracciato nella baseline | EXACT_SOURCE_NOT_LOCATED |

**Nota data quality:** per Range Selection Slider, il frontmatter e il codice descrivono un selettore di intervallo, ma il corpo MDX contiene un testo incongruente su un badge con pulsazione di notifica: non utilizzarlo come descrizione affidabile del comportamento.

**Componenti non risolti:** `Text Gradient`, `Notification List` e `Flip Clock` restano idee e link di riferimento. Non affermare che il codice delle versioni DevLibraries sia già presente nel repository pin-nato. Esiste invece [Event Reminders](https://ui.watermelon.sh/animated-components/event-reminders) con file `src/data/contents/animated-components/event-reminders/base.tsx` blob `fdc3d4a3fb1b5afc149316a4cf605bc7e2a81e24`, utilizzabile come **riferimento distinto** per le preferenze di reminder, NON come prova dell'esistenza di Notification List.

## Raccomandazione specifica Anna's Diary — Home Oggi

L'idea utente è un riquadro in cima alla home con gli impegni della giornata, mostrato **alla prima apertura quotidiana oppure a un orario prescelto**. Separare tre comportamenti:

1. **Riepilogo in-app:** al primo accesso a Oggi per data locale, risolve solo eventi reali; ordinamento cronologico, titoli e orari; gestione giornata vuota; non obbliga alcun permesso notifiche.
2. **Pianificazione in-app:** l'utente può configurare quando mostrare il riepilogo, ma se l'app resta chiusa non è garantita l'apertura visuale della Home. L'opzione non equivale a una notifica push.
3. **Notifica di sistema Android/iOS (feature separata):** eventuale alert anche ad app chiusa richiede autorizzazione, API di scheduling, fuso orario/DST, cancellazione e retry, privacy dei titoli su lock screen e QA fisico.

**Requisiti:** preferenza esplicita e revocabile, daily-key per profilo e data, niente duplicati a ogni navigation/tab switch, ricalcolo dopo sync e cambio account, limiti privacy eventi condivisi, gestione overdue/annullati, tap per aprire evento, dismiss/snooze se previsti da Product Bible. Non mostrare un evento non salvato né confermato. Non perdere la coerenza visiva Armonia iOS rose e non sostituire la Home esistente.

## Raccomandazione Ricordi / controlli

- Carousel Slider: alternare card Ricordi senza tagliare le immagini originali; non sostituire la galleria full-size o il calendario. Indicatori attivi e navigazione tastiera/screen reader.
- Fractional Picker: il codice è un ruler numerico, **non un date-picker completo**; selezionare il giorno solo se anno/mese e giorni validi vengono gestiti dall'app (28/29/30/31, leap years, timezone).
- Scrub Slider: controllo di un valore scalare o posizione nella timeline, non selezione arbitraria di data/ora senza mappatura.
- Range Selection Slider: doppia maniglia numeric bounds, non preimpostato per DateTime. Può essere adattato a intervalli solo con validazione e input alternativo.
- Swap Form: transizione grafica Login/Register; **non** fornisce Google/Apple OAuth, backend, account, permessi o security flows.
- Dialog Stack: wizard visivo, **non** invita persone né genera codici di condivisione. Va integrato con la reale capacità di spazio condiviso.
- Text Gradient: se applicato, solo a microaccenti leggibili del brand, rispettando palette e font già approvati.
- Flip Clock: non implementazione verificata; a titolo di idea, countdown a target reale, state-machine/timer + risparmio batteria e riduzione movimento.

## Gate Flutter / Compose / PWA

Il codice di sei componenti è React/TypeScript e può fungere da riferimento UI/UX; per Flutter preferire widget nativi `PageView`, `ScrollPhysics`, `CupertinoPicker` o `ListWheelScrollView`, `Slider`/`RangeSlider`, `AnimatedSwitcher`, `Dialog`, `Stack`, `TweenAnimationBuilder`. Nessun componente importato automaticamente in app. Per PWA React considerare un futuro source-level admission e test, preservando notice MIT e licenze immagini/dipendenze.

**Stato:** source inspection (6) / unresolved exact-name (3), 0 integrazioni, 0 asset vendorizzati, 0 dichiarazioni di runtime pass.
