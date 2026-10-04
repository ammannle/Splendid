# Operation Splendide – Projektkontext

Dieses Projekt enthält genau eine fertige Webseite: `operation-splendide.html`.
Es ist ein Bond-Reiseplan (Casino Royale, November 2026) für eine Gruppe von vier Personen,
gestaltet als MI6-Ops-Zentrale. Die Seite wird als **Claude-Code-Artifact** veröffentlicht
und anschließend per öffentlichem Link geteilt.

## Regeln für Claude
- Inhalt, Texte, Daten und Design nur ändern, wenn der Nutzer es ausdrücklich verlangt.
- Immer genau diese eine Datei veröffentlichen: `operation-splendide.html` (Single Page, bereits self-contained).
- Artifact-Titel: `OPS // Operation Splendide` · Emoji: ♠️
- Beim ersten Mal ein neues Artifact anlegen. Bei späteren Änderungen **dasselbe Artifact aktualisieren**
  (URL steht unten unter „Artifact-URL“ oder über `/artifacts` anhängen) – nie ein zweites anlegen.
- Nach dem Veröffentlichen: URL hier unter „Artifact-URL“ eintragen.
- In jeder **neuen Sitzung** (lokal oder Cloud): vor dem Veröffentlichen das Artifact unter der URL unten mit
  `action: "read"` lesen, dann `operation-splendide.html` mit `url` = Artifact-URL veröffentlichen. Ohne `url`
  entsteht ein zweites Artifact mit neuem Link – das ist zu vermeiden. Ist die veröffentlichte Version neuer als die
  Datei im Repo, zuerst zusammenführen.
- Nach jeder Änderung: committen und pushen, damit lokale und Cloud-Sitzungen denselben Stand haben.
- Prüfen ohne Server: Skript-Syntax mit `node --check` auf dem extrahierten `<script>`-Block; die Seite selbst
  ist eine statische Datei und braucht keinen Dev-Server.
- Keine Personennamen in die Seite schreiben. Die Gruppe wird nur als „00-Einheit“ / „Agent 01–04“ angesprochen.

## Technische Rahmenbedingungen (bereits erfüllt)
- Keine externen Bilder, keine externen Skripte. Schriften kommen von Google Fonts (erlaubt), mit Fallbacks.
- Alle Interaktionen (Karten-Tabs, Zielobjekte, Einsatzplan 2/3/4 Tage, Entschlüsselungs-Animation, Radar,
  Q-Lab mit Roulette-Training, Vesper-Prüfstand, Gadget-Ausgabe, Le Chiffres Tell (Reaktionstest),
  Defibrillator (Timing), Kontopasswort (Wort-Raten), Gun-Barrel-Easter-Egg per „007“ oder 3× Tipp auf Ms Unterschrift;
  versteckt: Agentenstatus per Klick, geschwärzte Zeile aufdecken, Klick auf „STRENG GEHEIM“, Konsolen-Nachricht)
  laufen als Inline-JavaScript im Browser.
- Seit v5 zusätzlich: Abreisedatum im Einsatzplan (Wochentage, Sonnenuntergang per NOAA-Näherung in MEZ,
  Montags-Warnung Vítkov, 14.11. = 20 Jahre Premiere, Adventsmarkt-Hinweis), Countdown im Casino-Kasten,
  Uhren LDN/PRG, abhakbare Zielobjekte und Missionsziele, „Befehl quittieren“-Stempel, Modul 07 Feldhandbuch
  (Tschechisch-Sätze, Wechselstube, Packliste), Lizenzprüfung (Quiz) im Q-Lab (jetzt Modul 08), Druckansicht,
  Tastatur-Eggs „vesper“, „martini“, „mathis“, Tab-Titel „M wartet.“
- `localStorage`: Tag/Nacht unter `ops-theme`; v5-Fortschritt (gesicherte Ziele, Missionsziele, Packliste, Datum,
  Kurs, Quittung) unter Schlüsseln mit Präfix `ops5-`. Alles in try/catch, nur pro Gerät. „Gerät bereinigen“ im
  Footer löscht die `ops5-`-Schlüssel.
- Ms Stimme: knapp, trocken, schneidend, siezt, Ironie über Schatzamt/Spesen/Q. Randnotizen stehen in `MN`
  (Zielobjekte), Feld 5 von `H` (Quartiere), Feld 3 von `B` (Protokoll) und in den Plan-Notizen.
- Externe Links (Google Maps, Quellen) öffnen in neuem Tab.

## Design-System (bei Änderungen beibehalten)
- Farben Nacht: Hintergrund #050C12, Panel #0B1C27, Text #DCEBEF, Cyan #8FD7E8, Grün #4BE39A, Amber #F2B65E, Rot #F0554A
- Schriften: Chakra Petch (Überschriften), IBM Plex Mono (Daten/Labels), IBM Plex Sans (Fließtext)
- Stil: dunkle Monitorwand, dünne Cyan-Linien, Scanlines, Amber = Priorität, Rot = Zielobjekt

## Artifact-URL
https://claude.ai/artifact/VkhpteuzLouPymEZGJYyp2
(erstmals veröffentlicht am 04.10.2026; Updates immer an diese URL)
Freigabe: „Anyone with the link“ ist aktiv. Wer die Seite offen hat, sieht neue Versionen automatisch.

## Stand
- Version 4 (04.10.2026): Promille-Hinweise entfernt, Q-Lab (Modul 07) mit sechs Spielen, versteckte Gags.
- Version 5 (04.10.2026): M neu geschrieben (Einsatzbefehl mit Kopie, Aktenzeichen, P.S., Randnotizen überall),
  Countdown füllt das freie Feld im Casino-Kasten, Datumsplanung, Fortschritt zum Abhaken, Feldhandbuch,
  Lizenzprüfung, Druckansicht, weitere Eggs. Statusleiste läuft auf keiner Breite mehr über.
- Version 6 (04.10.2026): Lagekarten überarbeitet. Beschriftungen auf Schildern (`plate()`), größere Schrift,
  Assets beschriftet, Orientierungspunkte (`marks`), Länder, Straßenschilder, Maßstab, Nordpfeil. Zoom (+/−,
  Doppelklick, Ctrl/Trackpad-Pinch), Ziehen zum Verschieben; am Handy höheres Kartenformat mit Ausschnitt.
  Bewegte Zielpersonen aus dem Film (`PP`, `maps.*.people`), Klick öffnet Dossier, Karte folgt der Person.
  Auf der Startkarte fährt das 00-Einheit-Fahrzeug die Route. Animation läuft nur für sichtbare Karten.
