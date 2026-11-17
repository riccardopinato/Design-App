# Protocollo di adozione delle icone animate

**Stato: proposta tecnica, nessuna implementazione nelle app.** Questo protocollo allinea Gentleface all'Icon Adapter Pack attuale senza modificare API stabili.

## Decisione per app

1. Leggere Product Bible e UX/Theme attuali. Se il prodotto usa una famiglia Material Filled, mantenere quell'identità; Gentleface è alternativa da sperimentare come famiglia completa o in uno spot chiaramente separato.
2. Selezionare da [MATRICE_APP_ICONE.md](./MATRICE_APP_ICONE.md) solo una schermata reale e al massimo 2–3 icone. Non trasformare ogni icona del menu in un'animazione.
3. Verificare pagina e reale file SVG animato (nome, API, durata, stati finali), LICENSE MIT allegata al download e eventuali asset separati; pin della versione + SHA-256 dopo scaricamento.
4. Impostare comportamento: `on_action_succeeded`, `on_toggle`, `while_visible_and_real_operation`; in error/failure nessun feedback falso.
5. Verificare consumo, framerate, accessibilità, contrasto, dimensione visiva, pulsanti di almeno 48 dp, localizzazione, fallback statico e preferenze reduced-motion/sistema.
6. Eseguire test build + snapshot/widget e, quando mobile, test su device reale. Misurare impatto APK. Soltanto allora promuovere da REFERENCE a ADAPTED/LIBRARY_VERIFIED, e in seguito COPY_READY con evidenze.

## Path tecnici prioritari

**Flutter:** preferire `FactoryIconKey` in `packs/icons`, usare le capacità native `AnimatedSwitcher`, `TweenAnimationBuilder`, `AnimationController` su icona statica per evento o toggle; per veri morph, verificare renderer SVG/SMIL e la sua licenza/footprint prima di introdurlo. Un SVG SMIL non viene reso animato dal semplice esempio di codice Flutter statico sul sito.

**Compose Android:** l'icona statica Gentleface è un `ImageVector`/drawable candidato. Per animazione, valutare `AnimatedImageVector`/AnimatedVectorDrawable o Compose animation. Serve adattamento del motion: non dare per equivalente il parser XML Android e il file SVG SMIL Web.

**Web/PWA:** preferire file locali da bundle controllato, con inline SVG per poter fermare o cambiare stato. Rispettare `prefers-reduced-motion`; evitare loop nascosti e CTA senza nome accessibile. In `img`, lo SVG può animarsi ma non offre controllo del loop allo stesso modo dell'inline SVG: utilizzare solo dove appropriato.

## Priorità di pilot (non autorizzazione a modificare)

- **Omni Cleaner:** icona `video` (apertura player) + `images` (galleria), animazione una volta su apertura.
- **Anna's Diary:** `calendar` + `check` per salvataggio evento riuscito, senza cambiare tema approvato.
- **World Days:** `bookmark` e `download`; verificare azione e download reale.
- **Battery Guard:** `battery-charging` loop soltanto durante carica reale e UI visibile.
- **Notes-Ecosistema:** `search` e `bookmark` per focus e salvataggio, mantenendo accessibilità.

## Interazione con Golden e Pack

Il Golden Theme M3 e Golden App Shell / Responsive / Visual QA sono autorità trasversale; il pacchetto `packs/icons` è l'adapter semanticamente canonico per 24 ID. Questa sezione non modifica la versione o le 24 chiavi. Un futuro mapping verso Gentleface va introdotto come implementazione alternativa e testata senza cambiare l'ID pubblico; moduli indipendenti per web e mobile se necessario.
