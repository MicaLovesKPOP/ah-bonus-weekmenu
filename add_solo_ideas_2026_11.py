from pathlib import Path
import json
from html import escape

ROOT=Path(r"D:\Projects\AH-Recipes")
BASE="https://micaloveskpop.github.io/ah-bonus-weekmenu/"
RDIR=ROOT/"recepten"
RDIR.mkdir(parents=True,exist_ok=True)
CSS="""
:root{font-family:system-ui,-apple-system,Segoe UI,sans-serif;color:#1c3328;background:#f5f7f4}
body{margin:0}header{background:#fff;border-bottom:4px solid #188347;padding:30px 22px}
header>div,main,footer{max-width:880px;margin:auto}
main{padding:0 16px}h1{font-size:clamp(1.8rem,5vw,2.7rem);line-height:1.15}
h2{font-size:1.35rem}.card{background:#fff;border:1px solid #dae5dd;border-radius:14px;padding:22px;margin:16px 0}
p,li{line-height:1.55}li{margin:5px 0}a{color:#08753b}
small,.muted{color:#5c6f63}.pill{background:#e2f3e7;border-radius:18px;padding:6px 10px}
.note{background:#eaf4eb;border-left:4px solid #188347;padding:14px;border-radius:8px}
footer{padding:20px 16px;font-size:.8rem;color:#5c6f63}
"""
RECIPES=[
{
"slug":"bistrokrieltjes-champignons-tuinerwten-ei",
"name":"Romige bistrokrieltjes met kastanjechampignons, tuinerwten en ei",
"summary":"Een makkelijke eenpansmaaltijd met hartige champignons, gekruide aardappeltjes, eieren en een kaas-mosterdsaus.",
"prep":"PT5M","cook":"PT22M","total":"PT27M","mass":"Circa 900-1000 g op het bord",
"ingredients":[
"1 verpakking AH Mini krieltjes bistro 450 g (gebruik 350 g)",
"1 bak AH Kastanjechampignons gesneden 250 g (gebruik de hele bak)",
"1 zak AH Tuinerwten fijn diepvries 450 g (gebruik 200 g)",
"2 eieren",
"40 g belegen of oude Goudse kaas, geraspt",
"70 ml halfvolle melk",
"1 theelepel mosterd",
"1 theelepel sojasaus",
"1/2 theelepel knoflookpoeder",
"1 theelepel bakolie",
"zwarte peper"
],
"steps":[
"Zet een brede koekenpan of hapjespan op middelhoog vuur. Voeg 1 theelepel olie en de voorgesneden kastanjechampignons toe. Bak 4-5 minuten; roer af en toe.",
"Voeg 350 g voorgekookte bistrokrieltjes toe. Bak ongeveer 8-10 minuten totdat ze lekker kleuren. Roer af en toe.",
"Voeg 200 g bevroren tuinerwten en een klein scheutje water toe. Dek de pan af en verwarm 4 minuten, of totdat de erwtjes heet en gaar zijn.",
"Roer 70 ml halfvolle melk, mosterd, sojasaus en knoflookpoeder door de pan. Strooi 40 g geraspte belegen kaas erover.",
"Maak twee kuiltjes en breek er twee eieren in. Zet het vuur laag, dek af en laat circa 4-6 minuten stollen tot het eiwit volledig gaar is. Breng op smaak met peper."
],
"shop":"Gebruikt 350 van 450 g bistrokrieltjes en 200 van 450 g diepvrieserwten. De ongebruikte diepvrieserwten blijven in de vriezer; gebruik de overige krieltjes tijdig volgens het etiket.",
"tip":"Van de 250 g champignons verdampt wat vocht, dus het eindgewicht is iets lager dan het ruwe totaal. Je kunt extra oude kaas toevoegen voor meer umami.",
"links":[
("AH Mini krieltjes bistro, 450 g","https://www.ah.nl/producten/product/wi525254/ah-mini-krieltjes-bristo"),
("AH Kastanjechampignons gesneden, 250 g","https://www.ah.nl/producten/product/wi378694/ah-gesneden-kastanjechampignons"),
("AH Tuinerwten fijn, diepvries 450 g","https://www.ah.nl/producten/product/wi788/ah-tuinerwten-fijn")
]},
{
"slug":"koreaanse-pindakikkererwten-broccoli",
"name":"Koreaanse pindakikkererwten met broccoli en basmatirijst",
"summary":"Makkelijk en rijkelijk gesausd: kikkererwten en broccoli in een hartige pinda-ssamjangsaus, met slechts een beetje rijst.",
"prep":"PT4M","cook":"PT12M","total":"PT16M","mass":"Circa 950-1000 g",
"ingredients":[
"1 blik AH Terra Kikkererwten 400 g (265 g uitgelekt)",
"1 zak AH Broccoliroosjes diepvries 450 g (gebruik 350 g)",
"1 zak AH Kant-en-klaar basmatirijst 250 g (gebruik 200 g)",
"40 g pindakaas",
"2 theelepels sojasaus",
"1 theelepel ssamjang",
"1/2 theelepel knoflookpoeder",
"1 snufje gemalen gember",
"100 tot 150 ml water",
"eventueel wat sesamzaad"
],
"steps":[
"Schep 350 g bevroren broccoliroosjes in een hapjespan met 100 ml water. Dek de pan af en verhit op middelhoog vuur 7-9 minuten, totdat de broccoli gaar is.",
"Spoel en laat het blik kikkererwten uitlekken. Roer pindakaas, ssamjang, sojasaus, knoflookpoeder en gember met een beetje warm water tot een gladde, dikke saus.",
"Voeg de kikkererwten en pindasaus toe aan de broccoli. Laat 2-3 minuten zachtjes pruttelen en roer voorzichtig. Voeg zo nodig nog een scheutje water toe; het moet smeuïg blijven.",
"Verwarm 200 g AH kant-en-klare rijst volgens de verpakking in de magnetron, of roer die de laatste minuten door de pan. Serveer de rijst met royale hoeveelheden broccoli, kikkererwten en saus. Werk eventueel af met sesam."
],
"shop":"Met een blik kikkererwten, een zak broccoli en een verpakking kant-en-klare rijst kom je bij de productprijzen rond 4 euro aan AH-aankopen, exclusief de pindasaus uit voorraad.",
"tip":"Geen gochujang en geen falafel. De ssamjang blijft een hartige achtergrondnoot; meer pindakaas maakt de saus voller. Een restje gekookte rijst uit de koelkast kan in plaats van magnetronrijst, mits veilig gekoeld bewaard.",
"links":[
("AH Terra Kikkererwten, 400 g","https://www.ah.nl/producten/product/wi167873/kikkererwten"),
("AH Broccoliroosjes diepvries, 450 g","https://www.ah.nl/producten/product/wi226367/broccoliroosjes"),
("AH Kant-en-klaar basmatirijst, 250 g","https://www.ah.nl/producten/product/wi613349/ah-kant-en-klaar-basmatirijst")
]},
{
"slug":"kip-cordon-bleu-krieltjes-sperziebonen",
"name":"Kip cordon bleu met krieltjes, sperziebonen en knoflook-mosterdsaus",
"summary":"Bijna volledig hands-off: krokante cordon bleus en krieltjes uit airfryer of oven, sperziebonen uit de magnetron, frisse romige saus erbij.",
"prep":"PT4M","cook":"PT20M","total":"PT24M","mass":"Circa 900-1000 g op het bord",
"ingredients":[
"1 verpakking AH Scharrel kip cordon bleu 2 stuks 250 g",
"1 verpakking AH Mini krieltjes 450 g (gebruik 400 g)",
"1 zak AH Sperziebonen gebroken diepvries 450 g (gebruik 280 g)",
"60 g naturel yoghurt of skyr",
"1 theelepel mosterd",
"1/2 theelepel knoflookpoeder",
"zwarte peper"
],
"steps":[
"Verwarm de airfryer of oven voor en leg de twee cordon bleus en 400 g mini krieltjes erin. Gebruik voldoende ruimte; bij een kleine airfryer liever één bakplaat in de oven dan twee bakbeurten. Volg voor de cordon bleus het etiket en zorg dat ze door en door heet zijn.",
"Verwarm ondertussen 280 g bevroren sperziebonen in een afgedekte magnetronbestendige schaal met een klein laagje water. Roer halverwege en verhit tot ze gaar en goed heet zijn; volg indien mogelijk het etiket.",
"Meng in een kommetje 60 g naturel yoghurt of skyr, mosterd, knoflookpoeder en peper. Serveer als dip of saus bij de cordon bleus en aardappeltjes.",
"Serveer de twee cordon bleus met krieltjes, alle sperziebonen en de saus. Bewaar eventuele ongebruikte diepvriesbonen in de vriezer."
],
"shop":"Drie hoofdproducten kosten samen circa 5,53 euro aan hele verpakkingen op basis van geobserveerde AH-prijzen; yoghurt en mosterd komen uit voorraad. Slechts een deel van de sperziebonen wordt gebruikt.",
"tip":"De cordon bleus zijn voorgegaard maar moeten nog volledig worden verhit. Dit is de minst voedzame van de drie opties door de panade; de royale portie sperziebonen compenseert een deel daarvan.",
"links":[
("AH Scharrel kip cordon bleu 2 stuks, 250 g","https://www.ah.nl/producten/product/wi531867/ah-scharrel-kip-cordon-bleu-2-stuks"),
("AH Mini krieltjes, 450 g","https://www.ah.nl/producten/product/wi476241/mini-krieltjes"),
("AH Sperziebonen gebroken diepvries, 450 g","https://www.ah.nl/producten/product/wi226498/ah-sperziebonen-gebroken")
]}]

def html_for(r):
    url=BASE+"recepten/"+r["slug"]+".html"
    data={"@context":"https://schema.org","@type":"Recipe","name":r["name"],"description":r["summary"],"url":url,
      "inLanguage":"nl-NL","recipeYield":"1 persoon","prepTime":r["prep"],"cookTime":r["cook"],"totalTime":r["total"],
      "recipeIngredient":r["ingredients"],
      "recipeInstructions":[{"@type":"HowToStep","position":i,"text":t} for i,t in enumerate(r["steps"],1)]}
    ld=json.dumps(data,ensure_ascii=False).replace("<","\\u003c")
    return (f'<!doctype html><html lang="nl"><head><meta charset="utf-8">'
        f'<meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(r["name"])} | Ons Weekmenu</title>'
        f'<meta name="description" content="{escape(r["summary"],quote=True)}">'
        f'<link rel="canonical" href="{escape(url,quote=True)}">'
        f'<script type="application/ld+json">{ld}</script><style>{CSS}</style></head><body>'
        f'<header><div><span class="pill">Eenpersoonsmaaltijd • {escape(r["mass"])}</span>'
        f'<h1>{escape(r["name"])}</h1><p>{escape(r["summary"])}</p></div></header>'
        f'<main><div class="card"><a href="../">← Alle recepten en gecombineerd weekmenu</a> · '
        f'<a href="../gemaksmaaltijden-2026-11/">Bekijk de drie gemaksmaaltijden</a></div>'
        f'<section class="card"><p class="note"><strong>Importeren:</strong> Open AH → Koken → Mijn recepten '
        f'→ + → Extern recept en plak de URL van deze pagina. Controleer de AH-productsuggesties.</p>'
        f'<h2>Ingrediënten voor één royale maaltijd</h2><ul>'
        +''.join(f'<li>{escape(x)}</li>' for x in r["ingredients"])
        +f'</ul></section><section class="card"><h2>Zo maak je het</h2><ol>'
        +''.join(f'<li>{escape(x)}</li>' for x in r["steps"])
        +f'</ol></section><section class="card"><h2>Handig</h2><p>{escape(r["tip"])}</p>'
        f'<p>{escape(r["shop"])}</p><h2>Exacte AH-producten</h2><ul>'
        +''.join(f'<li><a href="{escape(u,quote=True)}">{escape(n)}</a></li>' for n,u in r["links"])
        +'</ul></section></main><footer>Onafhankelijk recept, niet verbonden met Albert Heijn. '
        'Prijzen en beschikbaarheid veranderen; controleer wat AH werkelijk in je lijst zet.</footer></body></html>')

for r in RECIPES:
    p=RDIR/(r["slug"]+".html")
    content=html_for(r);p.write_text(content,encoding="utf-8")
    parsed=json.loads(content.split('<script type="application/ld+json">',1)[1].split('</script>',1)[0])
    assert parsed["@type"]=="Recipe" and parsed["recipeYield"]=="1 persoon" and len(parsed["recipeInstructions"])>=4
    print("Validated",p.name,len(parsed["recipeIngredient"]),len(parsed["recipeInstructions"]))

folder=ROOT/"gemaksmaaltijden-2026-11"
folder.mkdir(exist_ok=True)
list_items=[
 ("Bistrokrieltjes met champignons en ei",RECIPES[0]["slug"]),
 ("Koreaanse pindakikkererwten",RECIPES[1]["slug"]),
 ("Kip cordon bleu met krieltjes en sperziebonen",RECIPES[2]["slug"])
]
detailed=[
"1 pak AH Mini krieltjes bistro, 450 g",
"1 bak AH Kastanjechampignons gesneden, 250 g",
"1 zak AH Tuinerwten fijn diepvries, 450 g",
"2 eieren",
"1 blik AH Terra Kikkererwten, 400 g",
"1 zak AH Broccoliroosjes diepvries, 450 g",
"1 verpakking AH Kant-en-klaar basmatirijst, 250 g",
"1 verpakking AH Scharrel kip cordon bleu 2 stuks, 250 g",
"1 pak AH Mini krieltjes, 450 g",
"1 zak AH Sperziebonen gebroken diepvries, 450 g"
]
pantry=["Belegen of oude Goudse kaas, circa 40 g","Halfvolle melk, circa 70 ml","Pindakaas, circa 40 g","Ssamjang, sojasaus en knoflookpoeder","Mosterd, circa 2 theelepels","Naturel yoghurt of skyr, 60 g","Bakolie en peper"]
body=(f'<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
      f'<title>Drie makkelijke solo-avondmaaltijden | Ons Weekmenu</title><style>{CSS}</style></head>'
      f'<body><header><div><span class="pill">Drie gemaksmaaltijden</span><h1>Drie makkelijke maaltijden voor één</h1>'
      f'<p>Circa 800–1000 g per maaltijd, maximaal één pan en volop smaak. Dit zijn <strong>drie keuzes</strong>, geen verplichte extra boodschappen.</p>'
      f'</div></header><main><section class="card"><h2>Losse recepten voor AH</h2><ol>'
      +''.join(f'<li><a href="../recepten/{slug}.html">{escape(name)}</a></li>' for name,slug in list_items)
      +'</ol><p>Importeer de recepten afzonderlijk via AH <strong>Extern recept</strong>. Deze verzamelpagina is een gewone boodschappenlijst, géén recept voor drie personen.</p></section>'
      +'<section class="card"><h2>Gecombineerde boodschappen (alle drie opties)</h2><p>Koop alleen de producten die je nodig hebt. Bekijk eerst je eigen voorraad.</p><ul>'
      +''.join(f'<li>{escape(x)}</li>' for x in detailed)
      +'</ul><h2>Uit je voorraad</h2><ul>'
      +''.join(f'<li>{escape(x)}</li>' for x in pantry)
      +'</ul></section></main><footer>Niet verbonden aan AH. Niet bedoeld om alle drie maaltijden als één recept te importeren.</footer></body></html>')
(folder/"index.html").write_text(body,encoding="utf-8")
print("Validated combined solo shopping list",len(detailed),"products")

home=ROOT/"index.html"
root_text=home.read_text(encoding="utf-8")
if "Solo-gemaksmaaltijden" not in root_text:
    section='<section><h2>Solo-gemaksmaaltijden</h2><p>Drie makkelijke avondmaaltijden rond 800–1000 g, afzonderlijk te importeren in AH. <a href="gemaksmaaltijden-2026-11/">Bekijk de drie recepten en de gecombineerde boodschappenlijst</a>.</p></section>'
    assert "</main>" in root_text
    root_text=root_text.replace("</main>",section+"</main>",1)
    home.write_text(root_text,encoding="utf-8")
    print("Updated homepage")
else: print("Homepage already linked")
