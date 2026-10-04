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
  versteckt: Agentenstatus per Klick, geschwärzte Zeile aufdecken, Klick auf die Einstufung „OFFICIAL–SENSITIVE“, Konsolen-Nachricht)
  laufen als Inline-JavaScript im Browser.
- Seit v5 zusätzlich: Abreisedatum im Einsatzplan (Wochentage, Sonnenuntergang per NOAA-Näherung in MEZ,
  Montags-Warnung Vítkov, 14.11. = 20 Jahre Premiere, Adventsmarkt-Hinweis), Countdown im Casino-Kasten,
  Uhren LDN/PRG, abhakbare Zielobjekte und Missionsziele, „Befehl quittieren“-Stempel, Modul 07 Feldhandbuch
  (Tschechisch-Sätze, Wechselstube, Packliste), Lizenzprüfung (Quiz) im Q-Lab (jetzt Modul 08), Druckansicht,
  Tastatur-Eggs „vesper“, „martini“, „mathis“, Tab-Titel „M wartet.“
- `localStorage`: Tag/Nacht unter `ops-theme`; v5-Fortschritt (gesicherte Ziele, Missionsziele, Packliste, Datum,
  Kurs, Quittung) unter Schlüsseln mit Präfix `ops5-`; seit v12 außerdem `ops5-rt` (Roulette), `bar`, `bk`
  (Buchungsstatus), `done`, `notes`, `plan`, `budget`, `drivers`, `lic` (Lizenzprüfung). Alles in try/catch, nur pro Gerät. „Gerät bereinigen“ im
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
- Version 7 (04.10.2026): Modul 03-W „Weltlage / Das Archiv“: Weltkarte (Natural Earth 1:110 Mio., gemeinfrei,
  abstandstreu, als eingebetteter Pfad in `WORLD`), alle 25 offiziellen Filme plus Casino Royale 1967 und
  Sag niemals nie in `FILMS` (Handlungsorte, fiktive Orte markiert, Hauptfiguren). Routen je Film, ~140 bewegte
  Figuren, Filmfilter, Chronologie-Wiedergabe, Orts- und Personendossiers, Markierung „Operation Splendide“.
  Zoom-Logik ist jetzt der gemeinsame Baustein `viewer()` für Lage- und Weltkarte.
- Version 8 (04.10.2026): Bewegungen als Simulation statt festem Takt (`placeAt`/`planLeg`, Arten in `MOT`):
  `road` (Fahrzeuge bleiben auf der Strecke, wechselndes Tempo, zufällige Halte, gelegentliches Umkehren),
  `roam` (Fußgänger, zufälliges nächstes Ziel, Bögen, Schwanken, Umhertreten beim Warten), `fly` (Weltkarte,
  Flugbögen zwischen den Schauplätzen in zufälliger Reihenfolge). Weiches Anfahren und Bremsen, zufällige
  Aufenthalte, gelegentlich lange Pausen. Bei reduzierter Bewegung stehen alle Figuren still an einem Zufallsort.
- Version 9 (04.10.2026): Aufrisse der 13 Zielobjekte (`BP`, Zeichenhelfer `bR/bL/bP/bC/bWin/bCols`): Blaupause
  wird Linie für Linie gezeichnet, dann gleitet die Fassade (`e`) auseinander, Umgebung (`x`) bleibt stehen,
  Innenleben (`i`) mit nummerierten Markierungen und pulsierender Filmszene erscheint. Schriftfeld, Maßstabsfigur.
  Erweiterte Akten in `XT` (Baujahr, Architekt, Stil, Fakten, Besuch, Fotospot, Auftrag, Q-Notiz, Bewertung),
  nächstes Zielobjekt mit berechneter Entfernung, Aufträge abhakbar (`ops5-tasks`). Zahlen nur, wo belegt.
- Version 10 (04.10.2026): Weltkarte deutlich langsamer (`fly` 6–11 E/s, Aufenthalte 4–12 s, ruhigeres Umhertreten).
  Intro beim ersten Besuch (`#intro`, `runIntro`): Terminal, Netzhaut-Scan, Stempel, „Zugang gewährt“, Panzertore,
  danach gestaffelter Seitenaufbau (`body.boot`) und gezeichnete Route (`heroDraw`). Seit v13 bei jedem Laden;
  überspringbar per Knopf, Klick, Esc; „Intro wiederholen“ im Footer. Zustandsklassen heißen `i-*` (nicht `stamp`!).
- Version 11 (04.10.2026): Intro ohne „STRENG GEHEIM“-Stempel; stattdessen Zielerfassung Augsburg, Karlsbad, Prag
  (Koordinaten rasten ein, `i-lock`), gesamt ca. 5 s länger. Aufrisse auf Werkplanungsniveau: Blatt 700×400 mit
  Achsraster (`ax`), Höhenkoten (`lv`), Maßkette (`ch`), Schriftfeld; Zeichenbibliothek mit Sprossenfenstern
  (`bWin` inkl. Verdachung/Balkon), Rustika, Gesimsen mit Zahnschnitt, Pilastern, korinthischen Säulen, Balustraden,
  Mansarddächern mit Gauben, Portalen, Treppen, Schnittwänden (`bWall`) und Decken (`bSlab`), Möblierung.
  Ebenen: `k` Hintergrund, `e` Fassade, `x` Umgebung, `i` Schnitt. Vollbild-Ansicht der Aufrisse (Esc schließt).
- Version 12 (04.10.2026): Intro beginnt mit eigenem, als Blaupause gezeichnetem Emblem (Vauxhall Cross von der Themse,
  bewusst kein offizielles SIS-Wappen), das danach nach oben wandert; Intro ca. 18 s. Einsatzplan v2 (`BK` Buchungsregister,
  `DRIVE` Etappen, Tage `D1–D3` mit Dauer, Ort, Kosten, Plan B, Notizen, Zeitleiste, Jetzt-Modus mit „läuft/als Nächstes“,
  Buchungsstatus OFFEN/ANGEFRAGT/BESTÄTIGT, abhakbar). Neues Modul 04-L „Disposition“ (`#org`): Buchungsstand, Budgetrechner,
  Etappen mit Fahrereinteilung und Navigation, Notfallnummern, Kalender-Export (.ics), Teilen, Druck. Q-Lab: echter
  europäischer Roulette-Tisch (alle Einsatzarten, Kessel mit Kugelphysik, französische Ansagen, Statistik) und Bar mit
  animiertem Barkeeper (schütteln, rühren, muddeln, abseihen) und Rezepten aus vielen Filmen. Flair: Einstufung
  „OFFICIAL–SENSITIVE“ statt „STRENG GEHEIM“, Fußzeile „UK EYES ONLY“, Bereitschaftsanzeige `#rdyBtn` (`readiness()`,
  Lagebericht), Tastenkürzel 1–9/Q springen zu Modulen, „?“ zeigt Lagebericht und Kürzel (Ziffer nach „0“ springt nicht,
  damit „007“ funktioniert).
- Zielobjekt-Karten und Detailpanel zeigen statt Fadenkreuz mit Kartensymbol eine Aufriss-Miniatur (`bpThumb`,
  Ausschnitte in `THVB`): links Fassade, rechts Schnitt; bei Hover/Auswahl gleitet die Fassade zur Seite.
  Die Codes „OBJ A♠“ usw. bleiben als Kennung (Karten, Einsatzplan).
- Dateiausgabe: Im Artifact-Viewer gehen Downloads nur über die Capability `downloads` (beim Veröffentlichen
  `capabilities: {downloads: true}` angeben). `.ics` ist dort nicht erlaubt, darum ist der ICS-Knopf im Viewer
  ausgeblendet; stattdessen Google-Kalender-Links je Termin (`#orgCal`) und „Plan als Textdatei“ (.txt).
- Version 13 (04.10.2026): Modul 08-G „Qs Garage“ (`#garage`, vor dem Q-Lab, Kürzel G): 18 Bond-Fahrzeuge in `GZ`
  (Maße in mm, Profil `top`, Fensterfläche `dlo`, Säulen `pil`, Details `ft`, Motor/Tank/Antrieb für die Röntgenansicht,
  Gadgets `g` mit Animationsart, Datenblatt `sp`, Rückgabeprotokoll, Q- und M-Notiz). Seitenriss-Generator `draw()`
  (Catmull-Rom-Profil, Radläufe, Speichen-/Alu-/Stahlräder, Bremsscheiben, Maßketten, Achsen, Maßfigur 1,80 m,
  Schriftfeld). Zündung, Probefahrt mit Tacho, Q-Ausstattung vorführen (Effekte in `FX`), Durchleuchten,
  Maßstab DB5 als Vergleich, Vollbild (am Handy hochkant gedreht), Pfeiltasten. Fuhrparkbuch `GZB` für alle 25 Filme,
  Leistungsvergleich. Nur belegte Werte im Datenblatt; geschätzte Zeichnungsmaße sind mit ≈ markiert (`est`).
  Gewähltes Fahrzeug unter `ops5-car`. Intro läuft jetzt bei **jedem** Laden (kein `ops5-intro` mehr).
- Tests: Playwright-Skripte müssen vor dem Laden `window.__NOINTRO=1` per `addInitScript` setzen, sonst läuft das Intro.
