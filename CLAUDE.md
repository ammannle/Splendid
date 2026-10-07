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
- Tests: Playwright-Skripte müssen vor dem Laden `window.__NOINTRO=1` per `addInitScript` setzen, sonst läuft das Intro.
