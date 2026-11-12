from pathlib import Path
from html import escape
import json
import re

ROOT = Path(r"D:\Projects\AH-Recipes")
REC = ROOT / "recepten"
REC.mkdir(exist_ok=True, parents=True)
PUBLIC = "https://micaloveskpop.github.io/ah-bonus-weekmenu/"
CSS = """
:root{font-family:system-ui,-apple-system,'Segoe UI',sans-serif;color:#20382e;background:#f6f8f6}
*{box-sizing:border-box}body{margin:0}header{background:#fff;border-bottom:4px solid #128249}
header .wrap,main,footer{max-width:910px;margin:auto;padding:20px}
header .wrap{padding-top:33px;padding-bottom:32px}
h1{font-size:clamp(1.8rem,5vw,2.75rem);line-height:1.17;margin:.45em 0 .25em}
h2{font-size:1.36rem;margin:0 0 .65em}p,li{line-height:1.65}
a{color:#087442}a:focus-visible{outline:3px solid #ffa500}
.tag{display:inline-block;color:#18512e;background:#e0f2e4;border-radius:24px;padding:5px 12px;font-size:.86rem;font-weight:600}
.muted{color:#66756e}.intro{font-size:1.07rem;max-width:760px}
.card{background:#fff;border:1px solid #d9e3dd;border-radius:14px;margin:16px 0;padding:24px;box-shadow:0 2px 5px #1232}
ol,ul{padding-left:1.45em}li{padding:5px 0}
.topnav{display:flex;gap:15px;flex-wrap:wrap;margin:3px 0 24px}
.notice{border-left:4px solid #168449;padding:13px 17px;background:#ecf5ee;border-radius:8px}
.sublabel{font-size:.91rem;color:#55675e}
@media(min-width:760px){.two{display:grid;grid-template-columns:.85fr 1.15fr;gap:18px}.two .card{margin:0}}
footer{font-size:.82rem;color:#728078;padding-top:2px;padding-bottom:40px}
"""

RECIPES = [
{
"slug":"boursin-kip-oesterzwammen",
"name":"Romige Boursin-kip met oesterzwammen, broccoli en aardappelen",
"summary":"Een ruime pan kipdijfilet in een volle knoflook-kruidensaus, met oesterzwammen, veel broccoli en vastkokende aardappelen.",
"prep":"PT35M","cook":"PT40M","total":"PT1H15M",
"ingredients":[
"1 kg kipdijfilet","250 g oesterzwammen","1,5 kg broccoli, bij voorkeur diepvries",
"1 gele ui","4 tenen knoflook","1,5 kg vastkokende aardappelen",
"300 g Boursin knoflook en fijne kruiden","250 ml kippenbouillon","1 AH Houdbare halfvolle melk 6-pack (6 × 200 ml; gebruik 150 ml)",
"1 eetlepel mosterd","2 theelepels sojasaus","1 theelepel gedroogde tijm",
"1 eetlepel bakolie","1 theelepel citroensap","zwarte peper",
"1 eetlepel maizena, alleen als de saus te dun blijft"
],
"steps":[
"Was de aardappelen en halveer de grote. Snipper de ui en scheur de oesterzwammen. Snijd de kipdijfilet in stukken van 2-3 cm; gebruik hiervoor een schone plank. Meng in een maatbeker kippenbouillon, melk, mosterd, sojasaus en tijm.",
"Zet de aardappelen op in gezouten water en kook ze 15-22 minuten gaar. Giet af en houd warm.",
"Verhit olie in je grootste wijde hapjespan. Voeg alle kip toe en laat die in het begin even ongemoeid voor wat bruining. Bak circa 7-9 minuten en schep af en toe om. Als er veel vocht vrijkomt, laat dat op middelhoog tot hoog vuur deels verdampen.",
"Voeg ui en oesterzwammen toe. Bak 5-7 minuten mee; voeg vervolgens knoflook toe voor de laatste minuut.",
"Voeg het mengsel uit de maatbeker en de broccoli toe. Dek af en laat 10-15 minuten zachtjes garen, tot de broccoli zacht en de kip volledig gaar is.",
"Zet het vuur laag en roer de Boursin erdoor. Laat de saus rustig warm worden, zonder hard te koken. Verdik zo nodig geleidelijk met maizena die eerst is opgelost in koud water.",
"Proef en breng op smaak met zwarte peper, citroensap en eventueel wat extra mosterd of sojasaus. Serveer de aardappelen met veel kip, groenten en royaal saus."
],
"shop":"De persoonlijke Bonus-aanbiedingen voor 2 × 150 g Boursin, 250 g oesterzwammen en een zak 3 kg AH vastkokende aardappelen passen bij dit gerecht. Het recept gebruikt 1,5 kg aardappelen; de rest kan later op.",
"note":"In deze versie zijn de spruitjes weggelaten en vervangen door extra broccoli. Zo houd je het gemakkelijk en beter passend bij jullie smaak."
},
{
"slug":"tomaat-aubergine-ragu",
"name":"Dikke tomaat-auberginegehaktragù met courgette",
"summary":"Een krachtige, dik ingekookte gehakt-tomatensaus met veel aubergine en courgette; te serveren met een bescheiden portie volkoren pasta of bloemkoolrijst.",
"prep":"PT30M","cook":"PT40M","total":"PT1H10M",
"ingredients":[
"1 kg gemengd gehakt","1 aubergine, circa 350 g","3 courgettes, samen circa 900 g",
"2 gele uien","4 tenen knoflook","1 kg passata","800 g tomatenblokjes uit blik",
"70 g tomatenpuree","100 g zongedroogde tomaten op olie, uitgelekt",
"2 theelepels gedroogde oregano","1 theelepel gedroogde tijm",
"2 theelepels sojasaus","1 eetlepel balsamicoazijn","1 eetlepel olijfolie",
"200 g belegen of oude Goudse kaas",
"300 g volkoren spaghetti, totaal verdeeld over drie diners",
"800 g bloemkoolrijst, voor de koolhydraatarme porties",
"zout en zwarte peper"
],
"steps":[
"Snipper beide uien. Snijd de aubergine in blokjes van 1-1,5 cm en de courgettes in halve maantjes. Pureer de zongedroogde tomaten met 500 g passata in de blenderbeker tot een gladde, smaakvolle basis.",
"Verhit olijfolie in een ruime, wijde braadpan. Voeg het gehakt toe en bak 8-12 minuten, waarbij je het af en toe losmaakt. Laat overtollig vocht zoveel mogelijk verdampen.",
"Voeg ui en aubergine toe en bak 6-8 minuten. Voeg vervolgens courgette toe en bak 4 minuten mee.",
"Voeg de knoflook en tomatenpuree toe. Bak al roerend 1-2 minuten mee om de tomatensmaak te verdiepen.",
"Giet de gepureerde tomatenbasis, de andere 500 g passata en 800 g tomatenblokjes erbij. Voeg oregano, tijm en sojasaus toe. Laat 25-30 minuten zachtjes pruttelen met het deksel op een kier. Roer af en toe.",
"Breng op smaak met balsamicoazijn, zwarte peper en zout. Laat eventueel nog iets inkoken als de saus te dun is. Het resultaat moet rijk en dik zijn, maar nog royaal sauzig.",
"Kook per maaltijd pas de benodigde volkoren spaghetti of verwarm een portie bloemkoolrijst. Schep er veel ragù op en werk af met geraspte kaas. Bewaar overige ragù apart voor later."
],
"shop":"Voor het gehakt is de landelijke Bonus op twee pakken van 500 g gemengd gehakt gunstig. Passata en tomatenblokjes van het huismerk kunnen voordeliger zijn dan de merk-Bonus.",
"note":"De pasta is voor de liefhebber; gebruik voor je vriendin bloemkoolrijst of extra groenten zodat je niet twee aparte sauzen hoeft te maken."
},
{
"slug":"dikke-pompoen-spliterwtensoep",
"name":"Extra dikke pompoen-spliterwtensoep met rookworst",
"summary":"Een snert-achtige maaltijdsoep: heel dik, hartig, licht zoet van pompoen en helemaal glad wat wortel betreft, met royale plakjes rookworst.",
"prep":"PT30M","cook":"PT2H","total":"PT2H30M",
"ingredients":[
"500 g gedroogde groene spliterwten","900 g pompoenstukjes","500 g winterpeen",
"2 preien","1 knolselderij, circa 500-650 g na schillen",
"2 gele uien","2 tenen knoflook","2,0 liter water, indien nodig iets extra",
"bouillonblokjes volgens de dosering op de verpakking voor 2 liter",
"2 laurierblaadjes","1 theelepel gedroogde tijm","1 theelepel gerookt paprikapoeder",
"2 eetlepels mosterd","1 theelepel sojasaus","1 theelepel appelazijn of citroensap",
"3 rookworsten van circa 275 g per stuk","1 eetlepel bakolie","zwarte peper"
],
"steps":[
"Spoel de spliterwten. Schil winterpeen en knolselderij; was de preien grondig en snijd alle groenten grof. Snipper de uien en hak de knoflook. Nette kleine blokjes zijn niet nodig: alles wordt straks gepureerd.",
"Verhit de olie in een grote soeppan van minstens 7 liter. Fruit de ui 5 minuten, voeg de knoflook toe en bak 1 minuut mee.",
"Voeg spliterwten, pompoen, winterpeen, prei, knolselderij, 2 liter water, bouillonblokjes, laurier, tijm en gerookt paprikapoeder toe.",
"Breng rustig aan de kook, zet het vuur laag en laat met het deksel op een kier circa 90-110 minuten sudderen tot de spliterwten uit elkaar vallen. Roer elke 15-20 minuten en voeg alleen wat heet water toe als de soep dreigt aan te bakken.",
"Verwijder de laurierblaadjes en haal de pan van het vuur. Pureer de soep rechtstreeks in de pan met de staafmixer, totdat vooral de winterpeen volledig glad en onherkenbaar is.",
"Snijd de rookworsten in dikke plakken, voeg toe en verwarm volgens de aanwijzingen op de verpakking. Roer mosterd en sojasaus door de soep.",
"Proef; voeg peper en een klein beetje appelazijn of citroensap toe. Wees voorzichtig met zout vanwege bouillon en worst. De soep wordt tijdens afkoelen vanzelf dikker."
],
"shop":"Kooptip voor deze Bonusweek: een zak winterpeen van 1 kg. Je gebruikt circa 500 g en kunt de andere helft fijnsnijden en invriezen. Twee zakken bio-pompoenstukjes van 450 g leveren precies 900 g op.",
"note":"Deze soep is erg vullend, maar niet koolhydraatarm vanwege spliterwten en pompoen. Serveer je vriendin eventueel een kleinere portie met wat meer rookworst."
}
]


# Productnamen en verkoopeenheden zoals AH deze in zijn catalogus gebruikt.
# De echte receptporties blijven zes personen; aankoophoeveelheid kan groter zijn.
INGREDIENT_OVERRIDES={
  "boursin-kip-oesterzwammen": {
    "1 kg kipdijfilet": "2 pakken AH Scharrel kipdijfilet van ca. 480 g",
    "250 g oesterzwammen": "1 bak AH Biologisch Oesterzwammen van 250 g",
    "1,5 kg broccoli, bij voorkeur diepvries": "3 zakken AH Broccoliroosjes van 450 g, diepvries (1,35 kg totaal)",
    "1,5 kg vastkokende aardappelen": "1 zak AH Vastkokende aardappelen van 3 kg (gebruik 1,5 kg)",
    "300 g Boursin knoflook en fijne kruiden": "2 pakjes Boursin Knoflook & fijne kruiden van 150 g"
  },
  "tomaat-aubergine-ragu":{
    "1 kg gemengd gehakt":"2 pakken AH Gemengd gehakt van 500 g",
    "1 kg passata":"2 pakken AH Tomaten passata gezeefd van 500 g",
    "800 g tomatenblokjes uit blik":"2 blikken AH Tomatenblokjes van 400 g",
    "70 g tomatenpuree":"1 blikje AH Tomatenpuree van 70 g",
    "100 g zongedroogde tomaten op olie, uitgelekt":"1 pot AH Zongedroogde tomaten van 285 g (gebruik 100 g uitgelekt)",
    "200 g belegen of oude Goudse kaas":"1 stuk AH Goudse belegen 48+ stuk van ca. 425 g (gebruik 200 g)",
    "300 g volkoren spaghetti, totaal verdeeld over drie diners":"1 pak AH Biologisch Volkoren spaghetti van 500 g (gebruik 300 g)",
    "800 g bloemkoolrijst, voor de koolhydraatarme porties":"2 zakken AH Biologisch Bloemkoolrijst van 400 g, diepvries"
  },
  "dikke-pompoen-spliterwtensoep":{
    "500 g gedroogde groene spliterwten":"1 pak AH Terra Biologisch spliterwten van 500 g",
    "900 g pompoenstukjes":"2 zakken AH Biologisch Pompoen stukjes van 450 g",
    "500 g winterpeen":"1 zak AH Winterpeen van 1 kg (gebruik 500 g)",
    "3 rookworsten van circa 275 g per stuk":"3 stuks AH Gelderse rookworst van 275 g"
  }
}

# AH-productpagina's zijn gecontroleerd op assortimentstitel en verpakking.
# Een link helpt bij het handmatig "Wissel"-stapje wanneer AH verkeerd suggereert.
SHOPPING_LINKS={
 "boursin-kip-oesterzwammen":[
  ("AH Vastkokende aardappelen, zak 3 kg","https://www.ah.nl/producten/product/wi96050/ah-vastkokende-aardappelen"),
  ("AH Biologisch Oesterzwammen, bak 250 g","https://www.ah.nl/producten/product/wi588942/ah-biologisch-oesterzwammen"),
  ("AH Broccoliroosjes, diepvrieszak 450 g × 3","https://www.ah.nl/producten/product/wi226367/broccoliroosjes"),
  ("AH Scharrel kipdijfilet, circa 480 g × 2","https://www.ah.nl/producten/product/wi197231/ah-scharrel-kipdijfilet"),
  ("Boursin Knoflook & fijne kruiden, 150 g × 2","https://www.ah.nl/producten/product/wi1983/knoflook-en-fijne-kruiden"),
  ("AH Houdbare halfvolle melk 6-pack, 6 × 200 ml","https://www.ah.nl/producten/product/wi130270/ah-houdbare-halfvolle-melk")
 ],
 "tomaat-aubergine-ragu":[
  ("AH Gemengd gehakt, 500 g × 2","https://www.ah.nl/producten/product/wi561333/ah-gemengd-gehakt"),
  ("AH Goudse belegen 48+ stuk, circa 425 g","https://www.ah.nl/producten/product/wi59669/ah-goudse-belegen-48-stuk"),
  ("AH Biologisch Bloemkoolrijst, diepvries 400 g × 2","https://www.ah.nl/producten/product/wi582622/ah-biologisch-bloemkoolrijst")
 ],
 "dikke-pompoen-spliterwtensoep":[
  ("AH Biologisch Pompoen stukjes, 450 g × 2","https://www.ah.nl/producten/product/wi553673/ah-biologisch-pompoen-stukjes"),
  ("AH Winterpeen, zak 1 kg","https://www.ah.nl/producten/product/wi4076/ah-winterpeen"),
  ("AH Terra Biologisch spliterwten, 500 g","https://www.ah.nl/producten/product/wi469875/ah-biologisch-spliterwten")
 ]
}

for r in RECIPES:
    by_name=INGREDIENT_OVERRIDES[r["slug"]]
    existing=set(r["ingredients"])
    assert set(by_name)<=existing, (r["slug"],set(by_name)-existing)
    r["ingredients"]=[by_name.get(item,item) for item in r["ingredients"]]
    if r["slug"]=="boursin-kip-oesterzwammen":
        r["shop"]="Kook met 1,35 kg broccoli (3 diepvrieszakken à 450 g), niet met 3 verse stronken. De 3 kg vastkokende aardappelen en 250 g biologische oesterzwammen komen uit je persoonlijke Bonus. Controleer of AH de juiste verpakking voorstelt."
        r["note"]="De recepthoeveelheid aardappelen is 1,5 kg; koop de volledige Bonuszak van 3 kg en gebruik het restant later. Met drie zakken diepvriesbroccoli zijn de groenten nog steeds royaal."
    if r["slug"]=="tomaat-aubergine-ragu":
        r["shop"]="AH kan bij 'belegen kaas' jong belegen selecteren. Voor dit gerecht willen we écht belegen kaas, bijvoorbeeld AH Goudse belegen 48+ stuk. AH Biologisch Bloemkoolrijst is de bevroren variant, anders dan de verse 400 g verpakking die tijdelijk uitverkocht kan zijn."
    if r["slug"]=="dikke-pompoen-spliterwtensoep":
        r["shop"]="AH Biologisch Pompoen stukjes 450 g, twee stuks, is gunstiger dan drie pakken van 400 g muskaatpompoen. De AH Winterpeen is een zak van 1 kg, geen losse wortel; gebruik de helft en vries het restant in. De biologische AH Terra-spliterwten zijn met AH Premium voordeliger dan het gewone HAK-pak."

def product_validation(r):
    items=SHOPPING_LINKS.get(r["slug"],[])
    return ('<section class="card"><h2>Controleer deze AH-producten</h2>'
            '<p>De AH-receptimporter maakt zelf productsuggesties; zelfs bij een exacte naam kan een verkeerde verpakking worden geselecteerd. '
            'Gebruik zo nodig <strong>Wissel</strong> in AH om een van deze exacte artikelen te kiezen. '
            'Controleer ook persoonlijke Bonus Box-aanbiedingen en de beschikbaarheid.</p><ul>'
            +''.join(f'<li><a href="{escape(url,quote=True)}">{escape(name)}</a></li>' for name,url in items)
            +'</ul></section>')

def page(r):
    url = PUBLIC + "recepten/" + r["slug"] + ".html"
    ld = {
        "@context":"https://schema.org",
        "@type":"Recipe",
        "name":r["name"],
        "description":r["summary"],
        "url":url,
        "inLanguage":"nl-NL",
        "recipeCuisine":"Huisgemaakt",
        "recipeCategory":"Hoofdgerecht",
        "recipeYield":"6 personen",
        "prepTime":r["prep"],
        "cookTime":r["cook"],
        "totalTime":r["total"],
        "recipeIngredient":r["ingredients"],
        "recipeInstructions":[{"@type":"HowToStep", "position":i, "text":s} for i,s in enumerate(r["steps"],1)]
    }
    jsonld = json.dumps(ld,ensure_ascii=False).replace("<","\\u003c")
    return (
        '<!doctype html><html lang="nl"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<title>{escape(r["name"])} | Ons Weekmenu</title>'
        f'<meta name="description" content="{escape(r["summary"],quote=True)}">'
        f'<link rel="canonical" href="{escape(url,quote=True)}">'
        f'<meta property="og:title" content="{escape(r["name"],quote=True)}">'
        f'<meta property="og:description" content="{escape(r["summary"],quote=True)}">'
        f'<meta property="og:url" content="{escape(url,quote=True)}">'
        f'<script type="application/ld+json">{jsonld}</script>'
        f'<style>{CSS}</style></head><body>'
        f'<header><div class="wrap"><span class="tag">Ons Weekmenu • Recept voor 6 personen</span>'
        f'<h1>{escape(r["name"])}</h1><p class="intro">{escape(r["summary"])}</p></div></header>'
        '<main>'
        '<nav class="topnav"><a href="../">← Alle recepten & weekboodschappen</a>'
        '<a href="https://www.ah.nl/allerhande/favorieten">Mijn AH recepten</a></nav>'
        f'<p class="notice"><strong>Importeren in AH:</strong> Open Mijn Allerhande favorieten → + → <strong>Extern recept</strong> '
        f'en plak de URL van deze pagina. Controleer de herkende AH-producten en hoeveelheden voordat je ze toevoegt.</p>'
        '<div class="two"><section class="card"><h2>Ingrediënten</h2>'
        f'<p class="sublabel">Voor 6 royale porties • {escape(r["total"])}</p>'
        '<ul>' + "".join(f"<li>{escape(x)}</li>" for x in r["ingredients"]) + '</ul></section>'
        '<section class="card"><h2>Bereiding</h2><ol>'
        + "".join(f"<li>{escape(x)}</li>" for x in r["steps"])
        + '</ol></section></div>'
        f'<section class="card"><h2>Handige opmerkingen</h2><p>{escape(r["note"])}</p>'
        f'<p class="notice"><strong>Kooptip:</strong> {escape(r["shop"])}</p></section>'
        + product_validation(r) + '</main><footer>Onafhankelijk recept, niet verbonden aan Albert Heijn. De import '
        'van specifieke AH-artikelen en Bonusprijzen kan per week verschillen.</footer></body></html>'
    )

for r in RECIPES:
    p = REC / (r["slug"]+".html")
    p.write_text(page(r),encoding="utf-8")
    # Validate that each generated page has exactly one Recipe and one correct ingredient array
    text = p.read_text(encoding="utf-8")
    block = re.search(r'<script type="application/ld\+json">(.*?)</script>',text,re.S)
    parsed = json.loads(block.group(1))
    assert parsed["@type"]=="Recipe" and parsed["recipeYield"]=="6 personen"
    assert len(parsed["recipeIngredient"])>=15 and len(parsed["recipeInstructions"])>=6
    print(f"OK {p.name} ingredients={len(parsed['recipeIngredient'])} steps={len(parsed['recipeInstructions'])}")

index_path = ROOT / "index.html"
old = index_path.read_text(encoding="utf-8")
start = old.find('<section><h2>Gecombineerde boodschappenlijst</h2>')
assert start!=-1, "Cannot find combined grocery list section on landing page"
entries = "".join(
    f'<li><strong><a href="recepten/{escape(r["slug"])}.html">{escape(r["name"])}</a></strong>'
    f'<br><small>{escape(r["summary"])}</small></li>' for r in RECIPES
)
nav = ('<section><h2>Elk recept apart importeren in Albert Heijn</h2>'
       '<p>AH heeft de drie gerechten op de oude verzamelpagina als één recept voor 18 personen geïmporteerd. '
       'Gebruik liever deze losse recepten: ieder met <strong>eigen ingrediënten, kookinstructies en 6 personen</strong>.</p>'
       '<ol>'+entries+'</ol>'
       '<p>Open het gewenste recept, kopieer de URL en gebruik <strong>AH → Koken → Mijn recepten → + → Extern recept</strong>.'
       ' Je vindt de gecombineerde boodschappenlijst hieronder, als naslag.</p></section>')
if 'Elk recept apart importeren in Albert Heijn' not in old:
    old=old[:start]+nav+old[start:]
    index_path.write_text(old,encoding="utf-8")
    print("OK updated root landing page")
else:
    print("Root landing page already has links")
