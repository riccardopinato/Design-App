# ICONE — libreria e selezione App Factory

Questa sezione distingue le **famiglie di icone**, le **animazioni d'interazione** e la **compatibilità molti-a-molti** delle app. Non sostituisce [UI-UX](../UI-UX/README.md), [MOCKUP ESTETICI](../MOCKUP%20ESTETICI/README.md) né l'[Icon Adapter Pack](../packs/icons/README.md) già esistente.

## Stato e struttura

- **Fonte iniziale:** [Gentleface — categoria animated](https://gentleface.com/categories/animated), [demo animate](https://gentleface.com/animated-icons), [come usarle](https://gentleface.com/use).
- **Audit:** [GENTLEFACE_AUDIT_2026-11-17.md](./GENTLEFACE_AUDIT_2026-11-17.md).
- **Catalogo relazionale unico:** [REGISTRO_ICONE.json](./REGISTRO_ICONE.json).
- **Navigazione bidirezionale:** [MATRICE_APP_ICONE.md](./MATRICE_APP_ICONE.md) per icona ↔ app.
- **Protocollo di uso:** [GUIDA_INTEGRAZIONE.md](./GUIDA_INTEGRAZIONE.md).
- **Anteprime ufficiali apribili:** [ANTEPRIME.md](./ANTEPRIME.md).

## Regole canoniche

1. Un'icona descrive **una sola intenzione semantica** su ogni app. Conservare i 24 ID stabili in `packs/icons/manifest/icons.json`; il catalogo Gentleface è un **candidato a fornitore visivo**, non un secondo elenco di ID runtime concorrenti.
2. Ogni famiglia scelta per una app deve rimanere coerente. Non mescolare in modo casuale Material Filled e Gentleface line-round nella stessa barra. Preferire adattamento dell'**intera famiglia** o soli spot decorativi ben separati.
3. Per ogni icona, memorizzare collegamento, variante, licenza e verifica del file: nessun SVG/PNG o marchio di terzi viene caricato nel repo finché non passa il gate asset-level.
4. Motion **solo quando comunica evento o stato**. Le animazioni decorative non sostituiscono feedback testuale, stato verificato o controlli accessibili.
5. Il fallback statico è obbligatorio per reduced motion, incompatibilità renderer, contenuto offline o risparmio energetico.
6. Stato iniziale: `REFERENCE`, abbinamenti `PROPOSED_ONLY`; non `COPY_READY`, non `IMPLEMENTED`, non Golden. Non modificare automaticamente il codice delle app.
7. Per passare a `COPY_READY`: diritti sui singoli file e notices, pacchetto minimo (solo le icone usate), adapter versione-pinned, test e benchmark, screenshot e collaudo reale su consumer quando applicabile.

## Modello di associazione

`source 1 → N icone → N app`, con record singolo per coppia `(icon_id, app)`, fit HIGH/MEDIUM, superficie suggerita e stato. La stessa app può usare icone statiche di altri fornitori: questo catalogo non prende decisioni di branding al posto del Product Bible.

**Stato ad oggi:** 28 icone candidate, 24 app/piattaforme, 114 associazioni. 2 icone richiedono ancora una verifica specifica della disponibilità dell'animazione. Nessun SVG animato importato; nessuna app modificata.
