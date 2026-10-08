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
  Q-Lab mit Roulette, Bar und Lizenzprüfung, Gun-Barrel-Easter-Egg per „007“ oder 3× Tipp auf Ms Unterschrift;
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
- Zielobjekt-Karten und Detailpanel zeigen statt Fadenkreuz mit Kartensymbol eine statische Fassaden-Miniatur
  (`bpThumb`, Klasse `bp bpth`, Ausschnitte in `THVB`): geschlossene Ansicht in vollem Detail (Ebenen `k`, `e`, `x`,
  Schriftzüge), ohne Schnitt und ohne Animation. Achtung: Der animierte
  Aufriss im Detail wird mit `.bp:not(.bpth)` gesucht, sonst greift die Animation auf die Miniatur.
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
- Version 14 (04.10.2026): Modul 03-P „Personenakten“ (`#persons`, nach den Lagekarten, Kürzel P): elf Akten zu den
  Zielpersonen aus `PP`. Zeichengenerator `PA.sheet()` (Front- und Profilansicht, Konstruktionslinien, Haare, Brauen,
  Iris, Bart, Brille, Kleidung, Schraffur, Fingerabdruck, nummerierte Merkmale `mk`), Merkmale und Akte in `PAX`
  (Rolle, Erstkontakt, Merkmale, Vorgehen, Schwachstelle, Ausrüstung, Status, Darsteller, Gefährdung, Drehorte, M-Notiz).
  Verknüpft mit Lagekarte („Auf der Lagekarte verfolgen“, in der Karte „Akte öffnen“) und den Zielobjekten. Auswahl unter `ops5-pa`.
- Version 15 (04.10.2026): Module Reiseorganisation (`#org`), Einsatzprotokoll (`#regs`) und Feldhandbuch (`#field`)
  auf Wunsch entfernt. Bereitschaft zählt nur noch Buchungen, Datum, Quittung, Lizenz. Garage: DB5, Esprit, 2CV nach
  CC0-Vektorvorlagen, Alpine nach Foto nachgezeichnet (`TRC`). Maßfigur 007 im Smoking (`BF`, `bondFig`) ersetzt alle
  Strichmännchen; ab 110 px Höhe mit nachgezeichnetem Craig-Gesicht (`BF.T`). Porträts nach Fotos in `PT` (`traced()`).
- Version 16 (05.10.2026): Alle 18 Fahrzeuge der Garage nach Vorlagen nachgezeichnet (`TRC`: Silhouette `sil`, Linien `tl`,
  Glas `tg`, Maße über den echten Radstand geeicht). Quellen: Wikimedia-Commons-Fotos und CC0-Vektoren, für DB10, DBS V12,
  Z8 und V12 Vanquish vom Nutzer gelieferte Bauplan-Zeichnungen (Quelle steht im Datenblatt). Porträts in `PT` von Hand nach
  Fotos digitalisiert (wenige klare Linien; Bond bewusst reduziert). Missionsbriefing (`#mission`) als Rohfassung vorhanden,
  wird nach Fertigstellung aller Zeichnungen ausgebaut.
- Version 17 (06.10.2026): Porträts aller elf Personenakten und die Maßfigur 007 im Smoking nach vom Nutzer gelieferten
  Grafiken, in Tonstufen vektorisiert (`PS` je Person: `bb` + Ebenen `L` [s,1,2,3,i,r], Zeichner `stencil()`; Figur `BFS` als
  `<symbol id="bfSym">`, `bondFig()` setzt nur `<use>`). Farben `.pst-*`. Mustang Mach 1 und BMW 750iL nach Nutzer-Vorlagen neu.
  Danach zwölf Fahrzeuge (Vanquish, DB10, 750iL, Mustang, Hornet, DBS 1969, Bentley, AEC-Bus, Esprit Turbo, DBS V12, 2000GT, Z8)
  nach neuen Nutzer-Seitenrissen: Maßlinien entfernt, Linien zusammengefasst und vereinfacht, Höhe auf Werksmaß geeicht.
- Version 18 (06.10.2026): Missionsbriefing (`#mission`) fertig: 32 Szenen, ca. 5:00 min (ohne Fahrzeugvorstellung am Start), in Reihenfolge des Einsatzplans (3 Tage):
  Kapitel AUFTRAG · TAG 1 · TAG 2 · TAG 3 · FINALE (Chips springen zum Kapitel, ‹ SZENE / SZENE › einzeln). 21 vom Nutzer gelieferte
  Strichzeichnungen in `MSA` (skelettiert, 2x-Einheiten, Gruppen `G`, Linienstärke `--sw` je Zoom). Einblendungen je Szene `fx`:
  draw, zoomout, zoomin, iris, scan, wipe, tiles, lock (Zielerfassung mit Fokuspunkt `f`); Kamera über `.ms-cam` per Web Animations.
  Szenen mit `bp` zeigen erst den Gebäude-Aufriss (zeichnen, öffnen) und blenden dann in die Zeichnung über (`two()`).
  Fahrt-Etappen `LEGS` a–d auf der Routenkarte: nur der aktive Abschnitt leuchtet, der DB5 fährt ihn ab. Dazu Aufrisse Kaiserbad,
  Barrandov, Planá, Pokertisch, Personen-Dossier, Finale. Startet automatisch, sobald sichtbar.
  Vollbild (`#msFull`, Taste F): echtes Fullscreen per `requestFullscreen`, sonst Overlay `.ms.full`; Esc beendet,
  Leertaste Pause, Pfeiltasten Szene; die laufende Szene wird in der neuen Größe neu aufgebaut (`redo()`).
- Version 19 (06.10.2026): Briefing auf Kino-Niveau: Titelsequenz (`opening()`: Tinte, Kartensymbole, Silhouette 007 aus `#bfSym`,
  Vorspann „MI6 · Q-Abteilung präsentiert“, „In den Hauptrollen Agent 01–04“, Titel-Schlag), Akt-Karten vor Tag 1–3 (`actCard()`),
  Abspann (`credits()`, „Die 00-Einheit kehrt zurück“). Szenenübergänge `TRS` (dissolve, whip, cut, glitch, flash) mit Ausblendung des
  alten Knotens (`.ms-old`), Letterbox in Titel/Karten/Abspann, Filmkorn und Vignette, Ortseinblendung `ms-sup` bei Ortswechsel
  („KARLOVY VARY, TSCHECHIEN · TAG 1 · 14:00 MEZ“), Sprecherkennung „M“ im Untertitel. Ton `SND` rein synthetisch per WebAudio
  (Grundton, Akkord-Stich, Schlag, Wischen, Herzschlag im Casino, Ping bei Zielerfassung, Tippen), standardmäßig aus, Knopf `#msSnd`,
  Wahl unter `ops5-mssnd`. Pause hält auch den Ton an.
- Version 20 (06.10.2026): Modul 08-X „Qs Gadgets“ (`#gadgets`, nach der Garage, Kürzel X, Nav „Gadgets“), Aufbau wie die Garage
  (Klassen `gz*` wiederverwendet): neun Gadgets in `GD` (Kugelschreiber-Granate, Omega Seamaster, Defibrillator, Smart Blood,
  Bell Rocket Belt, Little Nellie, Goldener Colt, Walther PPK, Q-Boot) mit Film, Basis, Funktion, Bedienung, Einsatz,
  Rückgabeprotokoll, Q- und M-Notiz. Baupläne aus vom Nutzer gelieferten Zeichnungen in `GDA` (vektorisiert, Zeichenanimation),
  Blatt mit Legende und Schriftfeld, nummerierte Merkmale `pts` mit Vorführeffekten (`FX`: shot, torpedo, laser, thrust, rotor,
  spin, waves, charge, defib, click, boom), „Vorführen“ spielt alle nacheinander. Filter nach Kategorie, Vollbild,
  Ausgabe quittieren (`ops5-gdq`), Ausgabebuch; gewähltes Gadget unter `ops5-gd`.
- Version 21 (06.10.2026): Seite neu geordnet nach Ablauf einer Mission: 01 Einsatzbefehl (`#tx`), 02 Missionsbriefing (`#mission`),
  03 Einsatzplan (`#ops`), 04 Quartiere & Assets (`#assets`), 05 Zielobjekte (`#targets`), 06 Lagekarten (`#maps`),
  07 Personenakten (`#persons`), 08 Qs Garage, 09 Qs Gadgets, 10 Trainingsprogramm (`#qlab`), 11 Das Archiv (`#world-sec`).
  Navigation in derselben Reihenfolge; Tastenkürzel 1–9 folgen den Modulnummern, dazu Q (Q-Lab), W (Archiv), B, P, G, X.
- Version 22 (06.10.2026): Vorführbaukasten `QV` (vor der Garage, global): Kamerafahrt über die viewBox (`cam`, `zoomBox`), Kino-Overlay
  `.qv-ov` (Letterbox, Kennung, REC-Zeitcode, Zähler, Bauchbinde `lower`), Zielerfassung `lock`, Mündungsblitz, Leuchtspur, Hülsen,
  Funken, Feuer, Rauch (SVG-Filter `qvGlow`/`qvBlur`/`qvFire` je SVG), Druckwelle, Explosion mit Trümmern, Lichtbogen, Weißblitz,
  Bildwackeln; Ton über `window.SND` (aus dem Briefing, nur wenn eingeschaltet). Ablauf je Punkt `QV.stage()`: Kamera hin, Erfassung,
  Effekt + Verstärkung (`boost` in der Garage, `gboost` bei Gadgets), Kamera zurück. Garage-Vorführung und Gadget-Vorführung laufen
  darüber. Qs Gadgets um zehn Einträge ohne Bild erweitert (`art:null`, Platzhalter-Blatt `sheetPh`, „Bauplan folgt“, Vorführung aus):
  Aktenkoffer, Rolex Submariner, Seiko-Fernschreiber, Skistock-Gewehr, Schlüsselfinder, Signatur-Gewehr, Ericsson-Handy (Link zum 750iL),
  Röntgenbrille, Ultraschallring, Walther PPK/S (Skyfall). Bilder liefert der Nutzer nach; dann `art` und Punkte `pts` mit x/y/Effekt setzen.
- Version 23 (06.10.2026): Lagekarten überarbeitet. Gelände: Höhenlinien per Marching Squares aus Gauß-Hügeln (`hills`, Route/Prag)
  bzw. Talabstand zur Teplá (`valley`, Karlsbad); Flüsse `rivers` (Donau, Ohře, Vltava, Berounka), Gebirgsnamen `ranges`, weitere Orte
  `towns2`, Bebauung entlang der Teplá (`blocks`, schematisch), Moldaubrücken `bridges`, mehr Orientierungspunkte in Prag.
  Animation: radiales Einblenden `reveal()` vom Fokus, Route wird gezeichnet (`m-draw`), Fließrichtung `m-flow`, Marker rasten
  gestaffelt ein, Scan-Balken, Leuchtspur hinter dem Fahrzeug (`m-comet`), Kamerafahrt `V.fly()` im Viewer, Zielerfassung `lockOn()`
  mit Peillinien und Koordinaten beim Klick auf Ziel/Asset, Tab-Wechsel mit Ausblendung (`switchMap`). HUD: Uplink-Zeile mit UTC-Uhr,
  Koordinaten-Fadenkreuz unter der Maus (`svg._inv` = Rückprojektion).
- Version 24 (06.10.2026): Briefing ohne Kitsch: Abspann und Vorspann-Credits entfernt, schlichter Titel (`opening()`), Akt-Karten ohne
  Drehen, Übergänge nur noch Überblendung und Schnitt. Sprachausgabe `VOX` (Web Speech API, deutsche Gerätestimme, Text über `norm()`
  aufbereitet: Uhrzeiten, 00-Einheit, 007); die Zeitleiste hält jede Szene, bis M zu Ende gesprochen hat. Knopf `#msVox`, Wahl
  `ops5-msvox` (Standard an, startet mit dem ersten Klick auf Abspielen). Musik live per WebAudio (`SND.mood(0–4)`: e-Moll i–VI–iv–V,
  92 BPM; Flächen, Bass-Ostinato, Puls, Pauken, Trommeln, Streicher-Tremolo, Blechstich), Stufe je Szene über `moodOf()`
  (Casino 3, DBS-Überschlag 4), wird unter der Stimme abgesenkt (`SND.duck`). Knopf `#msSnd` heißt jetzt „Musik“.
- Version 25 (06.10.2026): Briefing-Stimme neu: statt Gerätestimme vorab erzeugte neuronale Aufnahmen (Piper, `tools/tts.py`),
  (seit v26 nur noch `m`, Erzähler entfernt), als MP3/Base64 in
  `<script type="application/json" id="vxData">` am Seitenende, Schlüssel = Prüfsumme des Szenentexts (`key()` in `VOX`, gleich in Python).
  Wiedergabe per WebAudio, Musik wird darunter abgesenkt. Aussprache-Umschreibungen in `SAY` (tools/tts.py). **Nach jeder Änderung
  an Szenentexten `SC[].c` das Skript erneut ausführen**, sonst liest für diese Szene die Gerätestimme (Fallback).
  Klang (`radio()` in tools/tts.py): abhörsichere Funkverbindung – Stimme ca. 1 Halbton tiefer, Funkband 260–3900 Hz, Sättigung,
  Kompression, Rauschteppich, Rauschstoß + Piepton beim Öffnen, Quittungston am Ende; Tempo `m` 0.96, `s` 0.93.
- Version 26 (06.10.2026): Briefing-Dramaturgie: Cold Open `coldOpen()` (eingehende Übertragung, Stimme startet verzögert `vd`), Kernsätze
  `s.pw` [Anker, Text, Klassen r/a/big/boom] synchron zur Stimme (Anteil des Ankers im Text × Cliplänge, `punch()`), Akt-Montagen
  (`actCard(...,arts)`, Schnitte mit Verschluss-Ton), Poker-Höhepunkt (Musik leise `SND.hush`, Herzschlag, roter Blitz, „STRAIGHT FLUSH“),
  Einschlag `impact()` (Blitz + Bildwackeln + `SND.boom`), Finale mit Stempel „AUFTRAG ERTEILT“ und T-minus, Schlussszene `lost()`
  „Übertragung beendet“. Handkamera und Schärfe ziehen über Wrapper `.ms-hh`. Untertitelzeile: Oszilloskop `#msScope` (Analyser der
  Stimme), Text `#msCapT`, Lagestufe `#msLage`. Musik standardmäßig an. Stimme jetzt Chatterbox Multilingual (`tools/tts_chatterbox.py`,
  synthetische Piper-Referenzen, Satz für Satz, `SEED` für Nachbesserung), danach `tools/tts.py --wavdir` (dezenter Klang `radio(light)`).
  Prüfung per Spracherkennung (faster-whisper). Qs Gadgets: Baupläne für 18 von 19 (fehlt: Walther PPK/S Skyfall), GDA `g10`–`g18`.
  Intro: statt des eigenen Emblems das MI6-Logo (Nutzer-Vorlage) als Blaupause gezeichnet, gefüllt, Leuchten (`.el.lg`, `.lgf`, `.lgm`).
  Garage: Schleudersitz in Fahrzeugmaßstab (Flugbahn per rAF, Kamera zoomt heraus: `stage` mit zoom < 1), DB5-Schild senkrecht.
  Briefing nur mit M (kein Erzähler, kein Sprecher-Knopf).
  Personenakten: Organisationen `OG` (MI6, Schatzamt, CIA, Quantum, SPECTRE) mit Abzeichen (SPECTRE, Quantum, MI6-Emblem und CIA-Siegel
  vom Nutzer, vektorisiert in Seitenfarben `LG`/`LG2`; Schatzamt eigenes Abzeichen), Akte, Mitglieder (→ `paOpen`), Organigramm `#ogSvg` (Befehlsweg, Geld,
  Feindkontakt; Hover hebt Verbindungen hervor), Auswahl `ops5-org`.
- Version 27 (06.10.2026): Briefing v3. Drehbuch mit Story: Cold Open, Lagebild 1–4 aus dem Organigramm (`orgScene`/`orgOn`, Kamera über
  `vbTo`, `OGB`/`OGL`; Markup über `window.ogMarkup`), Konto VESPER (`acct`, `TX`), dann Titel und Tage. Kernsätze neu verankert.
  Routenkarten neu (`rmap`/`rdrive`, Etappen `RL`): Gelände/Flüsse/Grenze/Orte aus `maps.route` (`rbase(fz)`), Kamera folgt dem Fahrzeug,
  Live-Werte Distanz/Uhrzeit/Tempo, Wegpunkte, Grenzübertritt, Ankunft; Schrift skaliert mit `--fz`. Überlappungstest über alle Szenen
  (Desktop/Handy) und Korrekturen. Stimme: Chatterbox mit natürlicher Studio-Referenz (XTTS-Sprecherin, synthetisch), Tempo 1,12
  (~150 Wörter/min), fehlerhafte Clips satzweise mit Spracherkennungs-Kontrolle neu erzeugt. Faktenkorrektur: Dimitrios stirbt auf den Bahamas.
- Version 28 (06.10.2026): Briefing v4, ca. 3:10 min. Auftrag (~60 s): Cold Open, Lagebild 1–3 (Organigramm, Szene 2 mit zweiter
  Kamerafahrt `og2`), Konto VESPER, Titel. Danach 13 Zielobjekte entlang der Route (`ZIELOBJEKT 01–13 / 13` statt Tag/Uhrzeit), Fahrten
  a–d (HUD zeigt Fahrzeit), Pokertisch nach dem Kaiserbad, Finale. Kapitel-Chips AUFTRAG · LOKET · KARLSBAD · PRAG · RÜCKWEG · FINALE.
  Texteinblendungen (Kernsätze) auf Wunsch entfernt. Musik: fünf Orchester-Stücke per MusicGen (`tools/music.py`, `#muData`:
  brief, title, drive, casino, final), Auswahl `cueOf()`, Überblendung und nahtlose Schleifen in `SND.cue`; Synthese nur noch als Fallback.
  Stimme: `tools/tts_robust.py` (ganzer Text bis 3 Versuche, sonst Satz für Satz bis 6, Whisper-medium-Kontrolle, Annahme ab 97 %,
  Eigennamen müssen hörbar sein, Kürzung erfundener Silben am Ende, `SEEDOFF` für neue Zufallswerte), Tempo 1,17 in `tools/tts.py`.
- Version 29 (06.10.2026): Briefing-Drehbuch komplett neu (Ms Stimme, Missionsbriefing statt Reiseführer: Lage, Konto VESPER, Auftrag
  „Folgen Sie dem Geld“, je Zielobjekt ein Auftrag/Risiko). Längen wie v28 (Auftrag ~60–90 s, 13 Zielobjekte, Fahrten a–d).
  Deutsche Namen, wo sie sicher ausgesprochen werden (Karolinenthal, Plan, Markt unter dem Schlossturm); heikle Begriffe umschrieben (Reiterdenkmal statt Vítkov, „Blatt seines Lebens“ statt Straight Flush, „Lizenz zum Töten“).
  Lesbarkeit: `legib()` hebt SVG-Schrift im Briefing auf mind. 12 px (Handy 10,5 px), Halo `.lgh`, Kollisionsschutz; Handy hochkant: Vollbild wird quer gedreht (`.rot`, Knopf `#msRot`), unlesbare Feinschrift ausgeblendet.
  Stimme: `tools/tts_perfect.py` (Wort-für-Wort-Prüfung per Ausrichtung gegen faster-whisper medium: jedes Soll-Wort vorhanden,
  kein Zusatzwort, korrektes Ende, keine Pause > 0,9 s, Tempo plausibel; am Stück, sonst satzweise, mehrere Runden; Bericht
  `report.txt`). Lautschrift weiter in `SAY` (tools/tts_robust.py), Erkennungs-Schreibweisen in `ALT`.
- Version 30 (07.10.2026): Briefing-Kino-Ebene (`cine()` je Szene, Klassen `cx-*`): Partikel `cx-dust` und Farbstimmung `cx-grade` je Lage,
  Lichtstreifen bei Schnitten, Übergänge `zoom`/`push`/`glitch`, Kamerafahrt per CSS `scale`/`translate` (`cxDolly`). Cold Open mit
  3D-Globus (`globe()`, Küsten aus `WORLD`, Funkstrecke London → Böhmen). Ziel-HUD `tgtHud()` (Zähler 01–13, Zeitcode, Koordinaten
  entschlüsseln, Signal, Fadenkreuz in der Zeichnungsphase, Tracking-Rahmen `track()` ohne Kollision), Plotterkopf über Aufrissen,
  Datenpakete im Organigramm (`orgFx`), Geldströme und hochzählende Beträge (`acctFx`), Titel entschlüsselt mit Lichtkante und 13 Zielpunkten
  (`openFx`), Scheinwerferkegel auf der Routenkarte, Kartenwenden und Herzschlag am Pokertisch, Staub beim Stempel (`finFx`), Bildrauschen
  und Röhre aus am Ende (`lostFx`). Alles respektiert reduzierte Bewegung.
- Version 31 (07.10.2026): Routenkarten im Briefing neu (`rleg`/`rmap`/`rdrive` v2, Klasse `.ms-rm.v2`): Strecke als Catmull-Rom-Spline
  (`crSpline`), Grundkarte ohne Schrift (`rgeo`), Beschriftung, Start-/Zielmarken, Wegpunkte und Fahrzeug in einer Ebene in Bildschirmpixeln
  (`.rl-ov`, Labels aus `rlabels()`, Kollision nach Rang, meiden HUD-Felder). Kamera: Totale (`T1`), Anflug (`T2`), Verfolgung mit Vorausblick,
  Schlusstotale (`TE`). Die gefahrene Linie wird jedes Bild exakt bis zur Fahrzeugposition gebaut (kein Nachhinken); Scheinwerferkegel entfernt.
  Fahrt-Szenen a, c, d jetzt 6,5 s.
- Version 32 (07.10.2026): Pokerszene neu als echte 3D-Szene (`poker()`/`pk()`/`pkCue()`, Klassen `p3*`): perspektivischer Tisch, Kamera
  über Einstellungen `P3` (wide, bet, board, lc, show, win, seat, end), Karten mit Vorder-/Rückseite drehen in 3D (`p3flip`, Zeitlupe `p3slow`),
  Chips als 3D-Stapel, Spotlicht, Rauch (Canvas), Giftglas mit Tropfen und EKG, Einsatz zählt auf 10.000.000 $, Le Chiffre Full House,
  Bond Straight Flush mit Lichtausbruch, am Ende Platz der 00-Einheit und Karten werden verdeckt. Ablauf synchron zur Stimme über `s.cue`
  (Anker im Text × Cliplänge, in `pwGo`). Schlusshand korrigiert: Board A♠ 8♠ 6♠ 4♠ A♥. Szene 10 s.
- Version 33 (07.10.2026): Neuer Seitenablauf: Verbindungsanimation (`#intro`, endet jetzt mit „VERBINDUNG STEHT · KENNWORT ERFORDERLICH“) →
  Kennwort-Tor `#vgate` im Stil der Vesper-Szene (`vGate()`, Bankterminal mit 6 Feldern, Kennwort VESPER, Fehlversuche mit Schütteln und
  M-Hinweisen ab dem 2. Versuch) → Missionsbriefing startet automatisch im Vollbild-Overlay (`msArm()` schaltet Stimme/Musik in der
  Eingabe-Geste frei, `msAuto(done)`, Klasse `.ms.auto`, Knopf „BRIEFING ÜBERSPRINGEN“, Esc) → danach reguläre Seite (`pageIn()`,
  Seitenaufbau `boot`). Läuft bei jedem Laden und bei „Intro wiederholen“. Tests mit `__NOINTRO` überspringen alles.
- Version 34 (07.10.2026): Keine künstliche Drehung mehr im Briefing-Vollbild (`.rot` und Orientierungssperre entfernt, Knopf „Quer lesen“
  ausgeblendet): Hochformat zeigt das Bild aufrecht in 4:3 mit Steuerung darunter, Querformat bildschirmfüllend. Kennwort-Tor erscheint
  sofort über dem Intro (keine Türöffnung mehr, die Seite blitzt nicht auf); beim Freigeben startet das Briefing unter dem Tor, das dann ausblendet.
- Version 35 (07.10.2026): Pokertisch im technisch gezeichneten Stil (wie Aufrisse): Raster, Tisch als Cyan-Kontur mit Schraffur, Achsen,
  Maßketten (2 400 / 1 200), nummerierte Plätze, Karten mit Linienrahmen und schraffierter Rückseite, Chips als gestrichelte Konturstapel;
  Gewinnkarten amber. Animation und Ablauf unverändert (CSS-Block „Pokertisch im technisch gezeichneten Stil“).
- Version 36 (07.10.2026): Pokertisch noch technischer: Giftglas, Lichtkegel, Rauch, rote Blitze und Herzschlag-Vignette entfernt.
  Tisch als Konstruktionszeichnung, die wie vom Plotter gezogen wird (`.p3draw`: Außen-/Innenkontur, Setzlinie, Achsen, Maßketten,
  Platzkreise 1–8, Beschriftung). „Gift im Glas“ jetzt als Befund-Kasten mit Hinweislinie zum Sitz von Bond und EKG (`.p3call`, `.p3ov`),
  Handauswertung als Tabelle (`.p3eval`), Gewinn mit Messringen und Scanlinie statt Leuchten. Kamera-Einstellungen nach links versetzt,
  damit rechts Platz für die Auswertung bleibt; Farbstimmung der Szene cyan statt rot.
- Version 37 (07.10.2026): Szene 1 (Cold Open) neu als SIGINT-Leitstelle (`coldOpen()`/`globe()`, Klasse `.co2`): Raster, Rahmenmarken,
  Kopfzeile mit UTC-Uhr, Verbindungsaufbau Zeile für Zeile mit OK-Vermerken, Messwerte (Latenz, Bitrate, Signal, Frequenz), Stimmanalysator
  „LIVE · M“. Globus technisch: Gradring mit Teilung (dreht), Gradnetz, gestrichelte Küsten, zwei Satellitenbahnen, Relais London → ARGUS-3 →
  Böhmen mit Datenpaketen, Zielerfassung Böhmen mit Fadenkreuzlinien und Koordinaten, Zoom in den nächsten Schnitt.
- Version 38 (07.10.2026): Zielobjekte technischer: Seitenleiste als Datenblatt (`side()`: Bau und Stil aus `XT`, Risikostufe `RISK`
  als Ms Einschätzung, Lageskizze der Route mit allen 13 Zielen `locMini()`), im HUD 3D-Abgleich mit Fortschritt (`.cx-ab`), Scanband
  (`.cx-band`), Tracking abwechselnd als Messlinie mit Maß (`.cx-dim`) und technische Kennungen (`TRK`).
- Version 39 (07.10.2026): Intro ohne die drei Zielerfassungen (Augsburg, Karlsbad, Prag); nach dem Netzhaut-Scan direkt „Verbindung steht“, Kennwort-Tor nach ca. 10 s statt 17 s.
- Version 40 (07.10.2026): Lagebild 1–3 im Briefing technischer: Raster-Hintergrund, Organigramm rechts (73 %), links Analysespalte
  (`orgDos`, `OGK`: Dossier der Zielperson mit Porträt aus `PA.sheet`, Scanlinie, Rolle/Status/Gefahr; Netzwerkanalyse mit hochzählenden
  Knoten/Kanten/Dichte und Pegelbalken). Zielerfassung im Netz (`orgFx(root,s)`): rotierendes Fadenkreuz am Schlüsselknoten, Amber-Hinweislinie
  vom Dossier, gestrichelte Peillinien; aktive Verbindungen mit Fließ-Strichelung, Datenpakete ohne Glühen. Handy: Spalte ausgeblendet.
- Version 41 (07.10.2026): Titelszene „Ihr Auftrag: Operation Splendide“ als technisches Operationsblatt (`opening()`, Klasse `.op2`,
  Container-Abfragen): Kopfzeile mit UTC-Uhr und Rahmenmarken, Codename als Kontur mit Konstruktions- und Maßlinien, die sich füllt, Stammdaten;
  Lageskizze der Route (`opGeo()` aus `LOCB`, Reihenfolge `OPO`, Gruppen `OPC`) mit Geldspur aus Konto 7714-V (Datenpakete), 13 Zielpunkten,
  Gruppenbeschriftung, Lauflicht über die Route und Fadenkreuz, das den Empfänger sucht (Koordinaten live); unten Auftragsparameter
  (AUFTRAG, ZIELOBJEKTE, ROUTE, EMPFÄNGER, PROFIL). Ablauf synchron zu Ms Worten über `cue:openCue`. Lichtkante, Ringe und Leuchten entfernt.
- Version 42 (07.10.2026): Lagebild ohne laufende Strichelung auf den Linien (blinkte durch pathLength 1), Datenpakete langsamer.
  Konto-Szene neu (`acct()`/`acctFx`/`acctCue`, Klasse `.ac2`): Kontoblatt mit Status EINGEFROREN → REAKTIVIERT, Kennwort in sechs Feldern,
  Buchungsjournal (Zeilen erscheinen zu „Neun Überweisungen“, Beträge zählen), Summe; rechts Weltkugel (orthografisch, Canvas: Gradring,
  Gradnetz, gestrichelte Küsten) mit Quellen `ACS` (Beschriftung seitlich mit Hinweislinien), Geldflüsse als Großkreisbögen mit Höhe und
  Paketen, ab „Alle Empfänger“ logarithmischer Zoom (bis 95×) auf Böhmen mit Empfängern `ACD` und Fadenkreuzen.
- Version 43 (07.10.2026): Einsatzbefehl inhaltlich wie das Briefing (Le Chiffre, Quantum/SPECTRE, Konto 7714-V, „Folgen Sie dem Geld“),
  Abreisedatum jetzt dort (`#dep`, `depFlags()`). Missionsziele: 15 Punkte aus dem früheren Einsatzplan (Speicher `ops5-goals2`).
  Modul Einsatzplan (`#ops`, `plans`, `D1–D3`, `BK`, `DRIVE`) entfernt; Module neu nummeriert (03 Quartiere … 10 Archiv), Kürzel 1–9 angepasst.
  Bereitschaft: Datum 30, Quittung 30, Lizenz 40. Quartiere & Assets als kompaktes Register `AS` (36 Einträge in sechs Kategorien `ASK`,
  `<details>` je Eintrag, Standard nur befohlene/wichtige, „weitere anzeigen“, Kategorie unter `ops5-ascat`). Q-Lab: Ausrüstungsausgabe,
  Kontopasswort, Defibrillator und Le Chiffres Tell entfernt. Bar neu als technische Zeichnung (`#barSvg` 960×440): Hinterbuffet mit
  Flaschenprofilen `BPR`, Gläser/Gefäße im Schnitt `GV` (Füllhöhe über Innenvolumen `volTab`), Messbecher, Boston-Shaker, Rührglas,
  Barlöffel, Hawthorne-Sieb, Stößel, vorgezeichnete Bewegungsbahnen, Bewegungsunschärfe beim Schütteln, Schichtbeschriftungen,
  Messwerte (Simulation), Schriftfeld, Schrittliste `#barSteps`; am Handy seitlich scrollbar, folgt der Zubereitung.
- Version 44 (08.10.2026): Konto-Szene beginnt mit Abgriff: abgefangene SWIFT-Nachrichten laufen im Journal (`.ac-raw`), bis die Buchungen
  kommen; Globus dreht langsam, Suchmeridian mit Spur, Prüfsignale an Finanzplätzen `FIN` (ab „reaktiviert“ Treffer an den Quellen), Anzeige
  ABGRIFF %. Lageskizze der Titelszene neu (`opGeo()`/`opMap()`, SVG `.op-lsk.nolg` – `legib()` überspringt `nolg`): Ausschnitt `FB`, Gradnetz mit
  Randteilung, Höhenlinien/Flüsse/Grenze aus `rbase`, Route als Doppellinie mit km-Teilung (hin 475, zurück 425 km), Strecke wird mit Kopf
  gezeichnet, Detailkreise A Karlsbad und B Prag (gespreizt, nicht maßstäblich), Maßstab, Nordpfeil, Geldspur, Fadenkreuz sucht in den Details.
  Allgemeine Regel `section{margin-top:56px}` im Briefing neutralisiert (`.ms-stage section{margin:0}`). Bar: Barkeeper wieder da, als technische
  Figur (`BKG`, Maßstab eigener), Arme mit IK `bkIK`, Hände folgen Griffpunkten `grip.L/R` (Flasche, Messbecher, Shaker, Löffel, Sieb, Glas),
  läuft hinter dem Tresen mit; Braue bei „gerührt verlangen“.
- Version 45 (08.10.2026): Organigramm im Briefing mit technischer Ebene `ogDecor()` (Sektoren A/B schraffiert mit Eckmarken, Ebenenlineal E1–E5,
  Kennungen ORG-xx/P-xx, Messmarken an Personen, Pfeilspitzen je Verbindungsart, Kästen hinter Kantenbeschriftungen `.elb`, Legende, Einrast-Klammern
  `.ogk` an aktiven Knoten). Konto-Zoom zeichnet Kartengrund (Grenze, Flüsse, Moldau/Teplá, Route als Straße, Orte, Ländernamen). Titelszene:
  Geldspur/Quellkasten/Pakete entfernt, rechtwinklige Hinweislinien zu den Detailkreisen, keine km-Zahlen im Kartenbild. Routenkarten: technische
  Ebene `.rt-x` in Bildschirmpixeln (Gradnetz mit Grad-/Minutenangaben `RP`, Rahmen mit Teilung, km-Teilung an der Strecke, Maßstab, Nordpfeil,
  Koordinaten des Fahrzeugs), Anzeige KURS, Straße als Doppellinie (`.rm-cas` + Mittellinie), Hinweiskasten statt Banner. Bar in gemeinsamem
  Maßstab `K=.45` (Gläser, Shaker, Werkzeug in echten Längen, Barkeeper nach Körpermaßen in mm, Arme mit Verkürzung, Ellbogen nach unten).
- Version 46 (07.10.2026): Missionsbriefing nicht mehr als Modul auf der Seite (`#mission` nur sichtbar mit Klasse `live`, die `msAuto` setzt
  und `setFull(false)` entfernt; Nav-Eintrag weg, Module 01–09, Kürzel angepasst). Titelszene: statt Fahrt-Animation baut eine Scanlinie die
  Lageskizze auf (`opScan`, `.scl`), zu „Route“ leuchten die Etappen A–D nacheinander (`.lgp`, `.ltag`, Kopfzeile `.op-km`). Konto-Zoomkarte:
  Höhenlinien aus dem Lagekarten-Gelände (`acGeo()`), Siedlungsflächen `AC_URB`, Gewässer `AC_RIV`, Orte `AC_TWN`, Landschaften `AC_RNG`,
  Entfernungsringe um Prag, Kartenrahmen mit Gradteilung, Maßstab mit Verhältniszahl, Nordpfeil, Beschriftung mit Kollisionsschutz.
  Zielobjekte im Briefing: statt der Strichbilder hochdetaillierte technische Zeichnungen (Ansicht/Schnitt/Axonometrie/Typenblatt) für
  loket, pupp, mlyn, trziste, airport, strahov, ministry, danube, vitkov, museum. Daten in `<script type="application/json" id="detData">`
  (je id: w, h, f = Kamera-Fokus, L = Ebenen a/f/h/c/m/r, T = Texte), `DET(k)`/`ART(k)`, Darstellung in `artSVG()` (Klasse `ms-det`),
  in `art()` vollständig sichtbar (contain) links neben dem Panel mit sanfter Fahrt zum Fokus. Generatoren lagen im Scratchpad; MSA-Strichbilder
  bleiben als Rückfall.
- Version 47 (07.10.2026): Detailzeichnungen global (`DET`, `detSVG`, `detHud` im ersten Inline-Skript vor dem Haupt-IIFE; `#detData` je id
  zusätzlich `an` Merkmale [Nr, x, y, Hinweis-x, Hinweis-y, Name] aus den Hinweisnummern/-linien der Zeichnung, `tg` Filmszene, `tl` Zielname).
  Modul Zielobjekte: Umschalter DETAILBLATT / AUFRISS & SCHNITT (`.dvw`, Wahl in `window.__dvw`), `.detbox` mit Zeichnung (`.dsv`), Legende der
  Merkmale (Hover/Klick misst ein: `hud.focus`), ANALYSE (Merkmale nacheinander, dann Ziel), NEU ZEICHNEN, VOLLBILD (`detView()`).
  Briefing: Zielerfassung sitzt auf echten Merkmalen der Zeichnung (`detHud` in der Kamera-Ebene, Klammern rasten ein, Hinweislinie, Kennung
  MESSE → ERFASST, max. 4 Merkmale je ~1 s, dann rotes Fadenkreuz mit Peillinien, „ZIEL ERFASST“, Name und Koordinaten); Anzeige MERKMALE n/m
  statt 3D-ABGLEICH; zufällige Tracking-Rahmen, ERFASST-Fadenkreuz und Lock-Overlay entfallen bei Detailzeichnungen.
- Version 48 (07.10.2026): Detailzeichnungen auch als Miniatur (`detThumb(k)`, Ausschnitt `th` 2:1 je id in `#detData`, nur Ebenen a/f):
  Zielobjekt-Karten (`thUp()` nach DOMContentLoaded, ersetzt die Aufriss-Miniatur), Detailpanel links („DETAILBLATT“) und Zielstatus-Liste
  der Startseite (`#tlist .ti`). Kaiserbad, Barrandov, Planá behalten die Aufriss-Miniatur.
- Version 49 (08.10.2026): Briefing: Überspringen beendet Stimme und Musik wirklich (`VOX.hold` blockt spätes `speak`, `SND.cue(null)` trennt die
  Musik auch bei pausiertem Ton). Zielobjekt-Szenen zeigen statt der alten Aufrisse **Lagepläne aus OpenStreetMap** (`#mapData`, `MAPG(k)`, `lpSVG(k,o)`;
  je id: Gebäude in Streifen, Straßen als Doppellinien nach Klasse r1–r6, Bahn/Tram, Gewässer, Grün/Wald, Plätze, Parkplätze, Bäume, Quellen/Brunnen,
  Haltestellen, Höhenlinien aus AWS-Terrain-Tiles, Straßen-/Gewässer-/Ortsnamen, Meter-Gitter, Rahmen mit Bogensekunden-Teilung, Maßstab, Nordpfeil,
  Ziel rot schraffiert mit Ringen 50/100/200 m und Kennung). Aufbau in Ebenen (Klasse `run`), Kamerafahrt über die viewBox (`lpGo`), Statuszeile
  LAGEPLAN/OSM %. Zweiphasen-Szenen (`two()`): Lageplan ~52 % der Szene, dann Detailzeichnung; Kaiserbad/Barrandov/Planá: nur Lageplan.
  Generator im Scratchpad (`map/gen.py`, `cfg.py`, `dem.py`; Daten © OpenStreetMap-Mitwirkende, ODbL, Hinweis in Karte und Footer).
  Modul Zielobjekte: Ansichten DETAILBLATT · AUFRISS & SCHNITT (neu auf Basis der Detailzeichnung: Fassade tritt zurück, Schnitt-Ebenen `S`
  in `#detData` mit `s`/`sh`/`sf` + Texten, `cutView`) · LAGEPLAN (`mapView`), alte Aufrisse nur noch für Kaiserbad, Barrandov, Planá (`viewInit`).
- Version 50 (08.10.2026): Routenkarten im Briefing auf OSM-Grundlage (`#routeData`, `RTD()`): Vektorkacheln von OpenFreeMap
  (z8 außerhalb, z11 im Korridor ±16 km, z12 im Nahkorridor ±3 km mit Nebenstraßen und Bächen) als Kacheln `ch` (Rahmen `b`, Ebenen
  Wald, Siedlung, Gewerbe, Gewässer, Flüsse, Grenze, Straßen r1–r5 als Doppellinien, Bahn), Höhenlinien `ct`, Orte `pl`, Gipfel `pk`,
  Straßennummern `rf`, echte Strecken `rt` aus OSRM (Etappen a 313, b 14, c 134, d 404 km). Ebenenfolge `RQL`, Kachel-Culling `rcull`,
  LOD-Klassen `qn` (Nahsicht, Nebenstraßen) und `qf` (Totale). Beschriftung nur in Streckennähe, Dörfer je Etappe max. 110 nahe der
  Route, versteckte Labels mit display:none. Generator im Scratchpad (`route/`). Quellenhinweis im Footer.
- Version 51 (08.10.2026): Routen-Animation ruhig und flüssig: Grundkarte wird im Leerlauf (Kennwort-Tor, `vGate` → `window.rimQueue`,
  sonst nach 9 s bzw. beim ersten `rdrive`) als Bilder vorgerendert (`RIM`: `bg` ganze Karte, je Etappe `k1` Totale und `k2` Verfolgung,
  `rimJob`/`rqSrc`/`rimReg`, Größe gedeckelt 6144 px/16 MPx) und als `<img class="rm-ly">` per `translate3d/scale` (GPU) unter der
  SVG-Ebene bewegt (`lyUp`), Überblendung k1→k2 nach Zoom; Vektoren `.rq` nur noch als Rückfall (Klasse `im` blendet sie aus).
  Kamera-Richtung `hc` aus Sehne weit voraus, stark geglättet (Fahrzeug folgt weiter der Straße mit `hd`), Kamera-Dämpfung 260 ms.
  HUD-Maße nur alle 300 ms (`hudC`), Labels: Vorrang für sichtbare, Einblenden erst nach 180 ms Stabilität, Einblenden mit Übergang.
  Defekte Pfadsegmente („M x yl“ ohne Punkte) aus `#routeData` entfernt (brachen Pfade ab), Generator korrigiert.
- Tests: Playwright-Skripte müssen vor dem Laden `window.__NOINTRO=1` per `addInitScript` setzen, sonst läuft das Intro.
