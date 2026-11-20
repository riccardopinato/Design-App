# App Factory — pipeline di motion UX e produzione video (candidata, 20/11/2026)

**Stato:** `PROPOSED_ONLY`. Nessun runner, editor, renderer, modello AI o skill installato. Nessun video prodotto. Controlli tecnici Golden, Product Bible e preferenze estetiche utente hanno precedenza.

## Corsia A: motion UI autentica (app Flutter / Kotlin Compose)

1. Leggere il Product Bible, il mock-up scelto, le componenti Design-App gia' approvate e la capability richiesta (loading/success/error, navigazione, cards, interazioni gestuali). Riprodurre stati reali, niente animazioni fittizie di attività.
2. Prendere **timing, easing, choreography, reduced motion** come guida da [motion-design-skill](https://github.com/LottieFiles/motion-design-skill); `reanimate` solo per riferimenti visivi legittimamente utilizzabili e con implementazione originale.
3. Tier minimo per il problema: **native/framework** → Flutter `flutter_animate` → `lottie`/`dotlottie` per vettori bounded → `rive` per interazioni con veri state machine. Non aggiungere strumenti PC/Web 3D al runtime APK.
4. Gate: numero minimo di motion token, interrompibilità, tap targets, a11y e `prefers-reduced-motion` quando applicabile, contrast, device 360dp/tablet, consumi e stabilità frame rate (target UX 60 FPS quando sostenibile), flash/vestibolare, screenshot QA.
5. QA nel consumer con CI exact-head, layout e percezione sul dispositivo; nessuna UID/COPY_READY prima dei controlli documentati.

## Corsia B: video marketing esterno ai binari delle app

1. **Brief e diritto:** prodotto reale, screenshot/video autentici, claim verificati, testo brand, destinazioni 16:9/9:16 con layout nativo per ciascuna versione.
2. **Regia:** `cinetic` per concept, shotlist, grafica di lancio/aggiornamento, `motionmaxxing` per lint di qualità visiva. Consultare i 15 stili `mg-styles-15` e le pitture/doodle `huashu-art-motion`/`anidoodle` **come reference**, non come stile obbligatorio.
3. **Media:** produzione originale o ricerca `Openverse` con fingerprint della sorgente, autore, URL originale, licenza/versione, uso commerciale e attribuzione. Non usare contenuti NC/ND per commercial/derivative senza un permesso compatibile.
4. **Musica e ritmo:** solo tracce proprie/licenziate; `librosa` per estrarre marker del ritmo da verificare ascoltando. Dato che la musica non e' un asset libero perche' trovato su Openverse, applicare gate per ogni sorgente.
5. **Produzione:** `Remotion Skills` come documento di lavoro, ma motore Remotion soggetto a licenza Free/Company e fonte skills senza LICENSE root trovata; alternativa renderer originale con effettive rights.
6. **Caption:** `WhisperX` locale solo con diritto/consenso sull'audio; controllare parole, tempi e nomi, per ogni lingua. Non assumere precisione millisecondo automatica. Per audio sintetico verificare diritti voce/modello.
7. **Encode:** `FFmpeg` CLI in macchina di build sotto corretta licenza, output e formati richiesti, codec/build verificati prima di distribuire binari. QA codec, peso, dimensioni, durata, fps, sottotitoli, loudness e checksum.
8. **Release:** licenze source/asset, confronto claim vs app, contrasto, no flashing, caption reali, motion pacing, credits e destinazione video sono tutti gate di pubblicazione.

## Corsia C: educational storytelling e 3D

- `Manim` per curve/formule/grafici da dati corretti (es. World Days, Edu 01), non una dashboard real-time.
- `huashu-art-motion` per arte mobile in video solo con pitture e personaggi originali o autorizzati; per temi medici valida i contenuti indipendentemente dalla resa visiva.
- `blender-skills` / `EffectCraft` desktop per progettare asset/filmati; `three.quarks`, `react-postprocessing` e `Tweakpane` sono tool Web prototype che richiedono budget GPU e non danno widget Flutter.

## Cosa non autorizza questa pipeline

- Copia automatica di animazioni protette da pagine Web, video altrui, effetti brand, tracce musicali, font o modelli non licensed.
- Introduzione di video rendering server, AI cloud, credenziali provider, acquisizione screenshot senza diritto, pacchetti Android, pubblicazioni, merge o addebiti in app.
- Promozione a `COPY_READY`, Donor certificato o Golden in assenza di source origin per componente, license, test e evidence.

[Audit delle 18 fonti](./MOTION_VIDEO_18_AUDIT_2026-11-20.md) · [Manifest pin SHA](./MOTION_VIDEO_18_REGISTRY_2026-11-20.json) · [Matrice per app](../UI-UX/MOTION_VIDEO_18_APP_MAP_2026-11-20.md).
