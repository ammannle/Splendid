# Operation Splendide mit Claude Code online stellen

## Voraussetzungen
- Claude **Pro oder Max** (bzw. Team/Enterprise mit freigeschaltetem öffentlichem Teilen)
- **Claude Code** als CLI (ab Version 2.1.183) oder die **Claude Desktop-App**
- Anmeldung mit deinem claude.ai-Konto über `/login` (nicht per API-Key)

## Schritt 1 – Ordner vorbereiten
ZIP entpacken. Du hast jetzt den Ordner `operation-splendide` mit:
- `operation-splendide.html` – die fertige Seite
- `CLAUDE.md` – Regeln, die Claude Code automatisch liest
- `ANLEITUNG.md` – diese Datei

## Schritt 2 – Claude Code im Ordner starten
Terminal öffnen und eingeben:

    cd Pfad/zu/operation-splendide
    claude

Falls noch nicht angemeldet: `/login` eingeben und mit deinem claude.ai-Konto anmelden.
(In der Desktop-App: Code-Bereich öffnen und den Ordner `operation-splendide` als Projekt wählen.)

## Schritt 3 – Diesen Prompt einfügen

    Veröffentliche operation-splendide.html unverändert als Artifact mit dem Titel
    „OPS // Operation Splendide“ und dem Emoji ♠️. Halte dich an die CLAUDE.md.
    Trage danach die Artifact-URL in die CLAUDE.md ein.

Claude Code fragt beim ersten Mal um Erlaubnis zum Hochladen → mit **Yes** bestätigen.
Danach öffnet sich die Seite im Browser.

## Schritt 4 – Öffentlich teilen
1. Auf der geöffneten Seite oben auf **Share** klicken.
2. Öffentlichen Link wählen (bei Pro/Max ist das die einzige Teilen-Option).
3. **„Always share latest version“** einschalten – dann sehen alle automatisch spätere Änderungen.
4. **Copy link** → Link in die Gruppe schicken.

Wer den Link ohne Anmeldung öffnet, braucht kein Claude-Konto. Statt deines Namens steht dann
im Kopf der Hinweis „Content is user-generated and unverified.“ – das ist normal.

## Später etwas ändern
Claude Code im selben Ordner starten und z. B. schreiben:

    Trage in die Übertragung von M den Zeitraum 20.–22. November 2026 ein und
    veröffentliche das bestehende Artifact neu.

Dank CLAUDE.md aktualisiert Claude dieselbe Seite, der Link bleibt gleich.
Den Link wiederfinden: `/artifacts` → Artifact auswählen → `c` kopiert den Link.

## Falls es nicht klappt
- Claude schreibt nur eine lokale Datei ohne Link → Plan, Version oder Anmeldung prüfen (Schritt „Voraussetzungen“).
- Kein öffentlicher Link auswählbar (Team/Enterprise) → ein Owner muss „External sharing“ aktivieren.
- Notlösung ohne Claude Code: Ordner per Netlify Drop hochladen (Datei vorher in `index.html` umbenennen).
