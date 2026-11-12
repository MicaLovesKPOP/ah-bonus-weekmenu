# AH Weekmenu recepten

Persoonlijke recepten, publiek bereikbaar als statische webpagina's en via Albert Heijn **Extern recept** te importeren.

- Startpagina: https://micaloveskpop.github.io/ah-bonus-weekmenu/
- Individuele recepten: `recepten/*.html`
- Genereren: `python publish_individual_recipes.py`

## Afspraken voor toekomstige recepten

1. Publiceer **één recept per URL en één schema.org Recipe per HTML-pagina**. Vermijd samengestelde weekmenu's als één recept.
2. Vermeld per recept het juiste aantal porties/personen, ingredienthoeveelheden, voedingsvoorkeuren en genummerde bereidingsstappen.
3. Gebruik `recipeIngredient`, `recipeInstructions` (HowToStep), `prepTime`, `cookTime`, `totalTime`, `recipeYield`, `name` in JSON-LD.
4. Link vanuit de startpagina naar ieder nieuw recept, met een aparte gecombineerde boodschappenlijst.
5. Pas koophoeveelheden en productverpakkingen niet zomaar aan de bereidingshoeveelheden aan; zet Bonus-tips apart.
6. Controleer gegenereerde JSON-LD en de publieke URL voordat je een link als werkend presenteert.
7. De gebruiker importeert de publieke link zelf via AH → Koken → Mijn recepten → + → Extern recept. **Publicatie voegt op zichzelf niets toe aan het AH-account.**
8. Vermijd accountgegevens, locatiegegevens, privé-geschiedenis en andere persoonlijke data op openbare receptpagina's.
9. Voeg toekomstige recepten toe zonder bestaande publieke URL's te breken.
10. AH kan producten anders matchen; vraag de gebruiker om bij toevoegen in de app de exacte producten en aantallen te controleren.
11. **SKU-first**: controleer vóór publicatie de officiële AH-productpagina op actuele naam, inhoud en type (bijvoorbeeld vastkokend vs. iets kruimig; belegen vs. jong belegen; diepvries vs. vers). Gebruik de letterlijke producttitel in `recipeIngredient` waar die ondubbelzinnig is.
12. Geef de aankoopverpakking expliciet aan als de beste prijs/Bonus daarvan afhangt: `1 zak AH Vastkokende aardappelen 3 kg (gebruik 1,5 kg)`, niet alleen `1,5 kg aardappelen`.
13. Houd **kookhoeveelheden en aankoophoeveelheden** gescheiden, bijvoorbeeld 200 g kaas uit een stuk van 425 g. Pas recepten alleen aan op werkelijke economische verpakkingshoeveelheden als het gerecht er niet slechter van wordt.
14. Link belangrijke (of door de importer vaak verkeerd gekozen) AH-artikelen rechtstreeks naar hun productpagina op de receptenwebsite, zodat `Wissel` in AH snel kan worden gecorrigeerd. Een exacte naam garandeert geen correcte automatische matching.
15. Vermijd keuze-ambiguïteit in de gestructureerde ingrediënten: geen `belegen of jong belegen`, maar bijvoorbeeld `AH Goudse belegen 48+ stuk`. Zet alternatieven afzonderlijk in de toelichting.
16. Let op uitverkochte/uit assortiment-artikelen; controleer voorraad in de AH-app vóór de definitieve boodschappenlijst. Verander een artikel niet stiekem in een ander type.
17. De gecombineerde weekmenupagina is **alleen overzicht**, geen los recept voor 12/18 personen. Import in AH uitsluitend via de individuele recept-URL's, standaard 6 porties voor deze grote batches.
18. Leer van de werkelijke AH-importscreenshots: evalueer productmatch, aantal verpakkingen, prijs per kg, Bonus Box en alternatieven voordat de volgende week wordt opgesteld.

### Problemen geconstateerd op 12 november 2026

- 3 kg vastkokend werd drie keer 1 kg **iets kruimig**.
- 250 g biologische oesterzwammen werd 2 × 150 g.
- 2 × 450 g biologische pompoen werd 3 × 400 g andere pompoen.
- 1 kg winterpeen in zak werd één losse winterpeen.
- Diepvriesbroccoli werd verse broccoli.
- Belegen kaas werd jong belegen kaas.
- Gedroogde groene spliterwten werden niet aan een product gekoppeld.
- 400 g bloemkoolrijst werd als tijdelijk uitverkocht getoond; verifieer dan het alternatieve diepvriesartikel.

Deze repo is onafhankelijk van Albert Heijn.
## Melk bij koken

Gebruik voor recepten met kleine hoeveelheden melk bij voorkeur **AH Houdbare halfvolle melk 6-pack, 6 × 200 ml** (https://www.ah.nl/producten/product/wi130270/ah-houdbare-halfvolle-melk), in plaats van 500ml/1L melkpakken. Boursin-kip heeft 150 ml halfvolle melk nodig. Noem het vetgehalte expliciet. Als er al genoeg op voorraad is: niet kopen.

## AH-matching feedback 12 november, 23:29

- De suggestie voor 2 × 480 g AH Scharrel kipdijfilet bleek 1 kg **kipfilet** (verkeerde snit); in de app via *Wissel* corrigeren naar kipdijfilet.
- AH Biologisch Oesterzwammen van 250 g werd als 150 g gematcht. Let op de hoeveelheid of kies de 250 g Bonus-verpakking.
- AH Terra Biologisch spliterwten 500 g is met Premium €1,79 en voordeliger dan HAK €2,19; bio is hier een goede optie.
- AH Biologisch Bloemkoolrijst van 400 g is een prima alternatief als de reguliere 400 g tijdelijk uitverkocht is.
- Producten die de gebruiker al op voorraad heeft, kunnen in de AH-app uitgevinkt worden.
