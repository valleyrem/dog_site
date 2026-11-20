// Cookie consent (custom banner).
// Nothing is loaded before consent: GTM (and with it Google Analytics)
// is injected ONLY after the visitor grants analytics consent.

(function () {
  const STORAGE_KEY = "woof_consent";
  const CONSENT_VERSION = 1;
  // Garante guidance: ask again after about six months.
  const CONSENT_MAX_AGE_MS = 183 * 24 * 60 * 60 * 1000;
  const GTM_ID = "GTM-NJCSC592";

  const banner = document.getElementById("cookie-banner");
  const editBtn = document.getElementById("cookie-edit");
  const layerFirst = document.getElementById("cookie-banner-first");
  const layerDetails = document.getElementById("cookie-banner-details");
  const acceptBtn = document.getElementById("cookie-accept-all");
  const declineBtn = document.getElementById("cookie-decline-all");
  const openDetailsBtn = document.getElementById("cookie-open-details");
  const saveBtn = document.getElementById("cookie-save");
  const backBtn = document.getElementById("cookie-back");
  const closeBtn = document.getElementById("cookie-close");
  const analyticsToggle = document.getElementById("cookie-analytics-toggle");

  function readConsent(ignoreAge) {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      const data = JSON.parse(raw);
      if (!data || data.v !== CONSENT_VERSION) return null;
      if (!ignoreAge && !(Date.now() - data.ts < CONSENT_MAX_AGE_MS))
        return null;
      return data;
    } catch (e) {
      return null;
    }
  }

  function saveConsent(analytics) {
    const existing = readConsent(true);
    const data = {
      v: CONSENT_VERSION,
      // Stability of the ID across re-choices is intentional: Art. 7 GDPR
      // evidence works best as an event history under one consent ID.
      id: existing && existing.id ? existing.id : newConsentId(),
      analytics: !!analytics,
      ts: Date.now(),
    };
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    return data;
  }

  function newConsentId() {
    if (window.crypto && typeof window.crypto.randomUUID === "function") {
      return window.crypto.randomUUID();
    }
    return (
      "c-" +
      Date.now().toString(36) +
      "-" +
      Math.random().toString(36).slice(2, 12)
    );
  }

  function gtmLoaded() {
    return !!document.querySelector("script[data-consent-gtm]");
  }

  function loadGTM(analyticsGranted) {
    if (gtmLoaded()) return;

    window.dataLayer = window.dataLayer || [];

    // Consent Mode v2 signals: Google tags must respect the choice.
    window.dataLayer.push({
      consent: "default",
      ad_storage: "denied",
      ad_user_data: "denied",
      ad_personalization: "denied",
      analytics_storage: analyticsGranted ? "granted" : "denied",
    });

    window.dataLayer.push({
      "gtm.start": new Date().getTime(),
      event: "gtm.js",
    });

    const s = document.createElement("script");
    s.async = true;
    s.dataset.consentGtm = "1";
    s.src = "https://www.googletagmanager.com/gtm.js?id=" + GTM_ID;
    document.head.appendChild(s);
  }

  function applyConsent(data) {
    if (data && data.analytics) loadGTM(true);
  }

  function showBanner() {
    if (!banner) return;
    layerFirst.hidden = false;
    layerDetails.hidden = true;
    banner.hidden = false;
  }

  function hideBanner() {
    if (banner) banner.hidden = true;
  }

  function showEditButton() {
    if (editBtn) editBtn.hidden = !readConsent();
  }

  function setToggleFromConsent() {
    if (!analyticsToggle) return;
    const data = readConsent();
    analyticsToggle.checked = data ? data.analytics : false;
  }

  function finish(analytics, action) {
    const data = saveConsent(analytics);
    applyConsent(data);
    hideBanner();
    showEditButton();
    updateConsentIdDisplay();
    reportConsent(action, analytics, data.id);
  }

  // Show the visitor's own consent ID on the Cookie Policy page.
  function updateConsentIdDisplay() {
    const line = document.getElementById("cookie-policy-consent-id");
    const code = document.getElementById("cookie-consent-id");
    if (!line || !code) return;
    const data = readConsent();
    if (data && data.id) {
      code.textContent = data.id;
      line.hidden = false;
    } else {
      line.hidden = true;
    }
  }

  // Consent decisions are reported to the site's Telegram chat. The payload
  // carries no cookies and no identifiers beyond the visitor's own consent
  // ID (Art. 7 GDPR evidence) — the decision, the analytics flag, the page
  // path and the notice version. Reporting must never break the banner.
  function reportConsent(action, analytics, consentId) {
    try {
      fetch("/consent-log/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          action: action,
          analytics: !!analytics,
          path: window.location.pathname,
          id: consentId || "",
          notice: CONSENT_VERSION,
        }),
        keepalive: true,
      }).catch(() => {});
    } catch (e) {
      /* ignore: reporting is best-effort */
    }
  }

  // Initial state
  const saved = readConsent();
  if (saved) {
    hideBanner();
    showEditButton();
    applyConsent(saved);
  } else {
    showBanner();
    showEditButton();
  }
  updateConsentIdDisplay();

  // Buttons
  if (acceptBtn)
    acceptBtn.addEventListener("click", () => finish(true, "accepted_all"));
  if (declineBtn)
    declineBtn.addEventListener("click", () => finish(false, "declined"));

  if (openDetailsBtn) {
    openDetailsBtn.addEventListener("click", () => {
      setToggleFromConsent();
      layerFirst.hidden = true;
      layerDetails.hidden = false;
    });
  }

  if (backBtn) {
    backBtn.addEventListener("click", () => {
      layerDetails.hidden = true;
      layerFirst.hidden = false;
    });
  }

  // X button: on the very first visit (no choice stored yet) closing the
  // notice means declining analytics cookies — the refusal is recorded and
  // reported. When the banner was reopened to view or adjust preferences,
  // the X only dismisses it and must NOT overwrite the existing choice or
  // send a misleading report.
  if (closeBtn) {
    closeBtn.addEventListener("click", () => {
      if (readConsent()) {
        hideBanner();
      } else {
        finish(false, "closed");
      }
    });
  }

  if (saveBtn) {
    saveBtn.addEventListener("click", () =>
      finish(
        analyticsToggle ? analyticsToggle.checked : false,
        analyticsToggle && analyticsToggle.checked
          ? "saved_analytics"
          : "saved_necessary",
      ),
    );
  }

  if (editBtn) {
    editBtn.addEventListener("click", () => {
      setToggleFromConsent();
      showBanner();
    });
  }

  // Button on the Cookie Policy page: reopen the same consent window
  const policyOpenBtn = document.getElementById("cookie-policy-open");
  if (policyOpenBtn) {
    policyOpenBtn.addEventListener("click", () => {
      setToggleFromConsent();
      showBanner();
    });
  }
})();
