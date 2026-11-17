# Voice Orb — mappa di applicabilità condizionata alle future note vocali

**Fonte:** [DevLibraries](https://devlibraries.com/libraries/beui/voice-orb) → [beUI Voice Orb](https://beui.dev/components/agents/voice-orb) · [Audit tecnico e licenza](../sources/BEUI_VOICE_ORB_AUDIT_2026-11-17.md). **Tutte le 10 associazioni sono `PROPOSED_ONLY`: nessuna feature voce è dichiarata presente o approvata.**

| App | Fit | Possibile collocazione | Vincolo estetico |
|---|---|---|---|
| [Notes-Ecosistema](../PER_APP/notes-ecosistema.md) | HIGH | Composer note/canvas | palette editoriale attuale |
| [Anna's Diary](../PER_APP/annas-diary.md) | HIGH | Editor Ricordi o acquisizione evento | rosa, Manrope/Lora approvati |
| [Wonderlog](../PER_APP/wonderlog.md) | HIGH | Dettaglio tappa/ricordo | colori viaggio esistenti |
| [BeerClass AI](../PER_APP/beerclass-ai.md) | MEDIUM | Rapid Log o scheda birra | identità calda |
| [Cooking Anime](../PER_APP/cooking-anime.md) | MEDIUM | Dettaglio ricetta, non overlay costante | anime/kawaii senza distrarre dalla ricetta |
| [CamperBoss](../PER_APP/camperboss.md) | MEDIUM | Diario tappa | verde/bosco oro |
| [World Days](../PER_APP/world-days.md) | MEDIUM | Spazio note utente separato dal contenuto editoriale | palette attuale invariata |
| [App Factory Dashboard](../PER_APP/app-factory-dashboard.md) | MEDIUM | Composer idea/nota | UI tecnica e leggibile |
| [Deskland Android](../PER_APP/deskland-android.md) | MEDIUM | Pannello vocale separato dal launcher | effetto launcher leggero |
| [FrameLab](../PER_APP/framelab.md) | MEDIUM | Pannello note del progetto | non sovrapporre alla foto |

**Applicazione pratica:** il recorder e i permessi precedono il feedback visivo. L'orb riceve solo livelli audio reali; pause, stop, salvataggio, errori e privacy restano nella feature. Per Flutter/Compose implementazione nativa e fallback statico; mai introdurre dipendenze GPU pesanti senza benchmark su device e peso APK.
