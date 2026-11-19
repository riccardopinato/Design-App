# Unslop UI — archivio sorgente e provenienza

- Upstream: https://github.com/felipebasurto/unslop-ui
- Commit pin: `cd891160453f26aaacc569bad96a8d10d595076d` (19 novembre 2026).
- Licenza: MIT, copyright © 2026 Felipe Basurto; [LICENSE](./LICENSE) conservata.
- Riuso: `SOURCE_ARCHIVED / REFERENCE`, non `COPY_READY`. Nessun componente Flutter, Compose o runtime Android presente nell'upstream.
- File acquisiti: originali `skills/unslop-ui/SKILL.md`, `scripts/count_tells.py`, `scripts/load_unslop.py`, `references/tokens.md`, `references/unslop-fallback.md`, `references/examples.md`, `tests/test_skill.py` e licenza MIT.
- Asset grafici, filmati, esempi HTML/React, plugin Claude duplicato: non copiati, perché non necessari per questa capability.
- Riferimento operativo: [audit e mappa di adozione](../../UNSLOP_UI_AUDIT_2026-11-19.md).
- Non eseguire script vendorizzati con permessi estesi o su dati privati. Script upstream non integra Dart/Kotlin; deve essere abbinato all'adapter nativo AppLab.
- Evidenza: file acquisiti via GitHub alla revisione fissa. Non equivale a test locale o CI del codice vendorizzato.
