# Dock, floating taskbar e widget in-place — riferimenti del 16/11/2026

**Stato:** REFERENCE (non ADAPTED, non SOURCE_VERIFIED, non COPY_READY). Factory `c5adc147046beb7024629466d10eeb799c3c2619`.

## 1. OpenTaskbar — OSS MIT / C# WPF Windows

Repo/pin: https://github.com/alztrk/opentaskbar/tree/6348d7519f83e032c31a065d72ad3b327906da15

File ispezionati: `README.md`, `LICENSE`, `Design/README.md`, `Services/DockAutoHideController.cs`, `Services/TaskbarReplacementSession.cs`, `Services/WindowThumbnailPreview.cs`, `OpenTaskbar.csproj`.

| Pattern | Evidenza e token | Possibile applicazione |
|---|---|---|
| Floating dock con fisheye e anchor inferiore | `Design/README.md`: cella 52 DIP, icona 42 DIP, hover 1.28x, influenza 90 DIP, headroom 24 DIP | Dock PC e Deskland Android **concettuale**, trasformando pointer→touch senza effetti invasivi |
| IntelliHide con trigger al bordo | `Services/DockAutoHideController.cs`: stato overlap, reveal, debounce 400ms, hide/reveal 200/220ms | Pannelli non invasivi e dock desktop; su Android usare policy OS native, non Win32 |
| Glass leggibile | `Design/README.md`: opacity 60–100%, testo/icona non trasparenti, fallback opaque/high-contrast; Acrylic Win11 | Token surface/blur con contrasto e fallback, no trasparenza globale su testo |
| Anteprime finestre contestuali | `Services/WindowThumbnailPreview.cs`: DWM thumbnails, animazione ~160ms | Pattern di preview per desktop, non API Android trasferibile |
| Safety recovery | `Services/TaskbarReplacementSession.cs`: journal stato taskbar + rollback | Invarianti UX «torna alla UI originale» in ogni app che sostituisce una shell |
| Reordering e indicatori stato | README + design tokens | Feedback di drag e indicatori running/active senza scroll-jitter |

MIT per codice repository, **non** licenza universale di icone o dipendenze; copiare solo file selezionati con attribuzione e audit. Non inserire C# nella codebase Flutter Android.

## 2. lumabar — UI e concept reference, non codice OSS

Repo/pin: https://github.com/Acadbek/lumabar/tree/5929d128d617b7d86165f74fa74bfc3fbcfbed32 · sito: https://lumabar.xyz/

README dichiara che il repository conserva release commerciali e che il sorgente **non è pubblico**. Nessuna LICENSE OSS alla radice. Non scaricare/ripubblicare screenshot, immagini, MSI, loghi o codice e non presentare Liquid Glass proprietario come asset nostro.

Pattern documentali:
- Dock compatto con app + widget immediatamente leggibili (note, todo, calendario, meteo, musica, screen time, CPU/RAM).
- Picker dei widget, drag/sort, personalizzazione top/bottom, tre densità/taglie e cinque temi commerciali descritti.
- Estetica «Liquid Glass» usabile come **direzione concettuale**; disegnare composizione e materiali originali, con fallback contrasto e reduce motion.
- Widget di stato GitHub/AI limit/revenue: idea per una futura superficie App Factory **solo via API autorizzate**; mai aggirare autenticazioni o scrutare cookie/sessioni.
- Claim privacy «local/no telemetry» dal README: non verificato sul runtime.

Il README pinned conta 85 widget; altrove il marketing ne indica 100+: non dichiarare un numero di funzioni come validato.

## Crosswalk app (non autorizzazioni di sviluppo)

| Destinazione | Proposta | Priorità | Gate |
|---|---|---|---|
| Adaptive-Landscape-Android / Deskland | gesti launcher, dock responsive, recovery, indicatori e motion soft | P1 sicurezza, P2 polish | app drawer, launcher lifecycle, fisico Android, privacy, accessibilità |
| App Factory Control Center | micro-widget PR/CI/stato dei build/release | P2 | accesso dati GitHub, accuratezza, local-first |
| Notes-Ecosistema | Quick Capture in superficie/proiezione task e calendario | P3 | riuso modelli canonici, niente duplicati |
| Desktop Utility Factory | dock Windows indipendente | P2 studio | Product Bible, concorrenza, license per-file, build e tester Windows |
| Anna's Diary | nessuna modifica ora | — | evitare UI troppo densa |

## Regole di adattamento

Controllo 48dp touch e focus keyboard, reduced-motion, accessibilità, high contrast, timeout animazioni, uso RAM/CPU con superficie inattiva, salvataggio e rollback. Nessun pattern è implementato in una app per la sola presenza nel catalogo.

**Fonti:** OpenTaskbar @ `6348d7519f83e032c31a065d72ad3b327906da15`; lumabar @ `5929d128d617b7d86165f74fa74bfc3fbcfbed32`. Classificazione: primo `CODE_DONOR_CANDIDATE_WINDOWS + UI_UX_REFERENCE`, secondo `REFERENCE_ONLY`.
