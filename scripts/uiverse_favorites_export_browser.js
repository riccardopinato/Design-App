/*
 * Design-App — Esportatore di link Uiverse "My Favorites".
 *
 * Eseguire solo nella Console del proprio browser, mentre si visita
 * https://uiverse.io/favorites con il proprio account Uiverse autenticato.
 * Non legge cookie/token, non invia dati a siti esterni e non modifica i favoriti.
 * Legge i collegamenti visibili nel DOM mentre scorre la pagina e salva un
 * file JSON in locale. "Tutti" va verificato contro il conteggio del sito.
 */
(async function exportUiverseFavorites() {
  "use strict";
  var here = new URL(window.location.href);
  if (!["uiverse.io", "www.uiverse.io"].includes(here.hostname) ||
      here.pathname.replace(/\/+$/, "") !== "/favorites") {
    console.error("Apri prima https://uiverse.io/favorites");
    return;
  }

  if (document.body.innerText.includes("Sign in to save posts to Favorites")) {
    console.error("Accesso mancante: entra con GitHub in Uiverse e riprova.");
    return;
  }

  var found = new Set();
  var sleep = function (ms) { return new Promise(function (resolve) {
    window.setTimeout(resolve, ms);
  }); };

  function normalizeLink(href) {
    var u;
    try { u = new URL(href, window.location.href); }
    catch (_) { return null; }
    if (!["uiverse.io", "www.uiverse.io"].includes(u.hostname)) return null;
    var bits = u.pathname.split("/").filter(Boolean);
    if (bits.length !== 2) return null;
    if (!/^[a-z0-9_.-]+$/i.test(bits[0])) return null;
    // I componenti Uiverse hanno in genere slug aggettivo-animale-numero.
    if (!/^[a-z0-9_-]+-\d+$/i.test(bits[1])) return null;
    return "https://uiverse.io/" + bits[0] + "/" + bits[1];
  }

  function scanLinks() {
    document.querySelectorAll("a[href]").forEach(function (node) {
      var clean = normalizeLink(node.getAttribute("href"));
      if (clean) found.add(clean);
    });
  }

  // Scansione incrementale per non perdere link in liste lazy/virtualizzate.
  var root = document.scrollingElement || document.documentElement;
  var idle = 0;
  var maxSteps = 900;
  var steps = 0;

  for (var i = 0; i < maxSteps; i++) {
    steps++;
    scanLinks();
    var startTop = root.scrollTop;
    var startCount = found.size;
    var advance = Math.max(240, Math.floor(window.innerHeight * 0.7));
    root.scrollTop = Math.min(root.scrollHeight - root.clientHeight,
      root.scrollTop + advance);
    await sleep(210);
    scanLinks();

    var bottom = root.scrollTop + root.clientHeight >= root.scrollHeight - 3;
    if (bottom) {
      // Click solamente di pulsanti di paginazione con testo inequivocabile.
      var more = Array.from(document.querySelectorAll("button")).find(function (b) {
        return !b.disabled &&
          /^(load more|show more|mostra altri|carica altri)$/i.test(
            (b.textContent || "").trim());
      });
      if (more) {
        more.click();
        await sleep(500);
        scanLinks();
      }
    }

    if (root.scrollTop === startTop && found.size === startCount) {
      idle++;
    } else {
      idle = 0;
    }
    if (bottom && idle >= 9) break;
  }

  if (found.size === 0) {
    console.error("0 link estratti: il sito potrebbe usare un markup diverso, " +
      "una pagina non autenticata o uno scroll interno. Non è stato creato alcun export.");
    return;
  }

  var data = {
    schema_version: 1,
    source: "UIVERSE_AUTHENTICATED_FAVORITES_DOM",
    page: "https://uiverse.io/favorites",
    exported_at: new Date().toISOString(),
    extraction_method: "visible_anchor_links_after_progressive_scroll",
    scan_steps: steps,
    count: found.size,
    completeness: "REQUIRES_USER_COUNT_VERIFICATION",
    favorites: Array.from(found).sort()
  };
  var contents = JSON.stringify(data, null, 2) + "\n";
  var blob = new Blob([contents], {type: "application/json;charset=utf-8"});
  var downloadUrl = URL.createObjectURL(blob);
  var anchor = document.createElement("a");
  anchor.href = downloadUrl;
  anchor.download = "uiverse-favorites-export.json";
  document.body.appendChild(anchor);
  anchor.click();
  anchor.remove();
  window.setTimeout(function () { URL.revokeObjectURL(downloadUrl); }, 2000);
  console.log("Uiverse: " + found.size + " link esportati in JSON. " +
    "Confronta il totale con i preferiti mostrati da Uiverse prima di dichiarare COMPLETE.");
  console.log("Il JSON contiene solo gli URL dei componenti e metadati tecnici; " +
    "non include token, password o cookie.");
})();
