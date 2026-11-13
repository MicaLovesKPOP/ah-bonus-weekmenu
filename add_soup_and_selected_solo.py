from pathlib import Path
from html import escape
import json, re

ROOT=Path(r"D:\Projects\AH-Recipes")
BASE="https://micaloveskpop.github.io/ah-bonus-weekmenu/"
REC=ROOT/"recepten"
FOLDER=ROOT/"gekozen-solo-2026-11"
REC.mkdir(parents=True,exist_ok=True); FOLDER.mkdir(parents=True,exist_ok=True)

CSS="""*{box-sizing:border-box}body{margin:0;font-family:system-ui,-apple-system,Segoe UI,sans-serif;background:#f5f8f4;color:#183327}
header{background:white;padding:28px 20px;border-bottom:4px solid #18834b}
header>div,main,footer{max-width:850px;margin:auto}main{padding:0 18px}h1{font-size:clamp(1.8rem,5vw,2.6rem);line-height:1.14;margin:.4em 0}
h2{font-size:1.4rem}p,li{line-height:1.55}li{padding:4px 0}a{color:#066d3b}
.card{padding:22px;margin:16px 0;border:1px solid #dde5df;border-radius:14px;background:white}
.muted{color:#57695e}.note{padding:14px 16px;border-left:4px solid #18834b;background:#eaf5ee;border-radius:7px}
footer{padding:20px;font-size:.82rem;color:#647368}
"""
PAGES=[
  dict(
    slug="romige-paddenstoelensoep-kruidenboterbrood",
    name="Snelle romige paddenstoelensoep met extra champignons",
    desc="Kant-en-klare romige paddenstoelensoep met panklare kastanjechampignons, een beetje belegen kaas en het halve kruidenboterstokbrood dat al in je vriezer ligt.",
    time="PT13M",
    ingredients=[
      "1 pak AH Gebonden paddenstoelensoep 570 ml",
      "1 bak AH Kastanjechampignons gesneden 250 g",
      "40 g belegen Goudse kaas uit je voorraad, optioneel",
      "1 theelepel olie",
      "snufje gedroogde tijm en zwarte peper"
    ],
    steps=[
      "Verwarm je halve kruidenboterstokbrood uit de vriezer in oven of airfryer volgens de verpakking. Dit stokbrood heb je al; het staat daarom niet op de boodschappenlijst.",
      "Verhit 1 theelepel olie in één soeppan of hapjespan. Bak de 250 g voorgesneden kastanjechampignons circa 4-5 minuten op middelhoog tot hoog vuur.",
      "Schenk het hele pak AH Gebonden paddenstoelensoep (570 ml) erbij. Roer en verwarm zachtjes circa 3-4 minuten, zonder hard te koken.",
      "Roer eventueel 40 g belegen kaas erdoor en voeg een snuf tijm en wat zwarte peper toe. Proef voor je extra zout toevoegt: de soep is al gezouten.",
      "Serveer direct met het opgewarmde halve kruidenboterstokbrood. Je hebt maar één pan gebruikt."
    ],
    shopping=[
      ("AH Gebonden paddenstoelensoep 570 ml", "https://www.ah.nl/producten/product/wi400129/ah-gebonden-paddenstoelensoep"),
      ("AH Kastanjechampignons gesneden 250 g","https://www.ah.nl/producten/product/wi378694/ah-gesneden-kastanjechampignons")
    ],
    other="Uit voorraad: 40 g belegen kaas, tijm, zwarte peper en een beetje olie. Half kruidenboterstokbrood ligt al in de vriezer; niet bijbestellen.",
    cost="Richtprijs AH voor de twee verpakkingen samen: €4,84 (€2,65 soep + €2,19 champignons). Kaas/olie uit voorraad en het brood uit je vriezer zitten niet in dat kassabedrag.",
    mass="Soep + champignons circa 820 g vóór inkoken, plus brood ongeveer 100–150 g afhankelijk van je stokbrood; grofweg 900–1000 g."
  ),
  dict(
    slug="romige-aardappelgratin-spinazie-ei",
    name="Romige aardappelgratin met spinazie à la crème en ei",
    desc="Een zeer makkelijke solo-avondmaaltijd: aardappelgratin uit de oven, romige spinazie uit de magnetron en twee eieren uit één koekenpan.",
    time="PT30M",
    ingredients=[
      "1 verpakking AH Aardappelgratin naturel 500 g",
      "1 zak AH Spinazie à la crème diepvries 450 g",
      "2 eieren",
      "1 theelepel bakolie",
      "snufje nootmuskaat en knoflookpoeder",
      "1 theelepel mosterd, optioneel",
      "20 g belegen of oude Goudse kaas uit voorraad, optioneel"
    ],
    steps=[
      "Verwarm de AH aardappelgratin volgens de verpakking in de oven of airfryer tot door en door heet en bovenop goudbruin.",
      "Verwarm tegelijkertijd de AH Spinazie à la crème in een afgedekte magnetronbestendige schaal volgens de verpakking; roer halverwege goed om.",
      "Bak vlak voor het einde twee eieren in één koekenpan met een theelepel olie; gaar het eiwit goed.",
      "Voeg een snuf nootmuskaat en knoflookpoeder aan de spinazie toe en eventueel een beetje mosterd of belegen kaas voor extra hartigheid.",
      "Serveer de gratin naast de romige spinazie en de twee eieren. Dit is een flinke solo-portie zonder hakwerk."
    ],
    shopping=[
      ("AH Aardappelgratin naturel 500 g","https://www.ah.nl/producten/product/wi202678/ah-aardappelgratin-naturel"),
      ("AH Spinazie à la crème 450 g","https://www.ah.nl/producten/product/wi777/ah-spinazie-la-creme")
    ],
    other="Controleer voorraad: 2 eieren, nootmuskaat, knoflookpoeder, mosterd, kaas, olie.",
    cost="Gratin en spinazie zijn samen doorgaans enkele euro's; de actuele winkelmandprijs hangt af van de AH-productmatch. De twee eieren zijn extra als je die niet in huis hebt.",
    mass="500 g gratin + 450 g spinazie + circa 110 g ei = rond 1,06 kg, dus iets boven je gebruikelijke 800–1000 g."
  )
]
for r in PAGES:
  url=BASE+"recepten/"+r["slug"]+".html"
  ld={"@context":"https://schema.org","@type":"Recipe","name":r["name"],"description":r["desc"],
      "url":url,"recipeYield":"1 persoon","totalTime":r["time"],"inLanguage":"nl-NL",
      "recipeIngredient":r["ingredients"],
      "recipeInstructions":[{"@type":"HowToStep","position":i,"text":t} for i,t in enumerate(r["steps"],1)]}
  block=json.dumps(ld,ensure_ascii=False).replace("<","\\u003c")
  html=(f'<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    f'<title>{escape(r["name"])}</title><meta name="description" content="{escape(r["desc"],quote=True)}">'
    f'<script type="application/ld+json">{block}</script><style>{CSS}</style></head><body>'
    f'<header><div><small>Eenpersoons gemaksmaaltijd • {escape(r["time"])}</small><h1>{escape(r["name"])}</h1>'
    f'<p>{escape(r["desc"])}</p></div></header><main><section class="card"><p><a href="../gekozen-solo-2026-11/">← Boodschappenlijst van de gekozen solomaaltijden</a></p>'
    f'<p class="note"><strong>In AH importeren:</strong> AH → Koken → Mijn recepten → + → Extern recept; plak de URL van deze pagina. '
    f'Controleer AH-productkeuze en hoeveelheden voordat je toevoegt.</p>'
    f'<h2>Ingrediënten</h2><ul>'+''.join(f'<li>{escape(i)}</li>' for i in r["ingredients"])
    +'</ul></section><section class="card"><h2>Bereiding</h2><ol>'
    +''.join(f'<li>{escape(i)}</li>' for i in r["steps"])
    +f'</ol></section><section class="card"><h2>Wat kost het?</h2><p>{escape(r["cost"])}</p><p>{escape(r["mass"])}</p>'
    +f'<p>{escape(r["other"])}</p><h2>Juiste AH-artikelen</h2><ul>'
    +''.join(f'<li><a href="{escape(u,quote=True)}">{escape(n)}</a></li>' for n,u in r["shopping"])
    +'</ul></section></main><footer>Onafhankelijke receptenpagina, niet verbonden aan AH. Controleer beschikbaarheid en prijzen in je eigen winkelmand.</footer></body></html>')
  target=REC/(r["slug"]+".html")
  target.write_text(html,encoding="utf-8")
  check=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',html,re.S).group(1))
  assert check["recipeYield"]=="1 persoon" and len(check["recipeInstructions"])>=4
  print("OK",target.name)

# The selected three solo meals are independent: the first two came from the
# user's own selection; soup is the third. This is NOT an AH recipe for 3 people.
selected=[
 ("Romige aardappelgratin, spinazie à la crème en ei","romige-aardappelgratin-spinazie-ei"),
 ("Koreaanse pindakikkererwten met broccoli en rijst","koreaanse-pindakikkererwten-broccoli"),
 ("Romige paddenstoelensoep met extra champignons en kruidenboterstokbrood","romige-paddenstoelensoep-kruidenboterbrood")
]
needed=[
 ("AH Aardappelgratin naturel","1 × 500 g"),
 ("AH Spinazie à la crème (diepvries)","1 × 450 g"),
 ("Eieren","2 stuks, tenzij uit voorraad"),
 ("AH Terra Kikkererwten","1 blik 400 g"),
 ("AH Broccoliroosjes diepvries","1 zak 450 g (gebruik 350 g)"),
 ("AH Kant-en-klaar basmatirijst","1 pak 250 g (gebruik ca. 200 g)"),
 ("AH Gebonden paddenstoelensoep","1 pak 570 ml"),
 ("AH Kastanjechampignons gesneden","1 bak 250 g")
]
pantry=[
 "Pindakaas, ssamjang, sojasaus, knoflookpoeder en gemalen gember",
 "Mosterd, nootmuskaat, belegen of oude Goudse kaas, bakolie en zwarte peper",
 "Een half kruidenboterstokbrood ligt al in de vriezer — bewust NIET op de boodschappenlijst"
]
html=(f'<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
  f'<title>Gecombineerde boodschappenlijst — 3 gekozen solomaaltijden</title><style>{CSS}</style></head><body>'
  f'<header><div><h1>Drie gekozen solomaaltijden</h1><p>Gecombineerde AH-boodschappenlijst voor aardappelgratin, pindakikkererwten en paddenstoelensoep met je eigen kruidenboterstokbrood.</p></div></header><main>'
  f'<section class="card"><h2>Drie losse importrecepten</h2><p>Importeer elk recept apart via AH Extern recept, niet deze gecombineerde pagina.</p><ol>'
  +''.join(f'<li><a href="../recepten/{escape(slug)}.html">{escape(title)}</a></li>' for title,slug in selected)
  +'</ol></section><section class="card"><h2>Gecombineerde boodschappenlijst</h2><ul>'
  +''.join(f'<li><strong>{escape(name)}</strong> — {escape(qty)}</li>' for name,qty in needed)
  +'</ul><h2>Controleer eerst je voorraad</h2><ul>'
  +''.join(f'<li>{escape(x)}</li>' for x in pantry)
  +'</ul></section></main><footer>De prijzen, voorraad en AH-productmatches moet je vóór bestellen in je eigen app controleren.</footer></body></html>')
(FOLDER/"index.html").write_text(html,encoding="utf-8")
print("OK combined",FOLDER/"index.html")

# Stable homepage navigation; do not rewrite the original recipes or their schema.
home=ROOT/"index.html"
txt=home.read_text(encoding="utf-8")
key="gekozen-solo-2026-11/"
if key not in txt:
  assert "</main>" in txt
  txt=txt.replace("</main>",'<section><h2>Mijn gekozen solo-gemaksmaaltijden</h2><p><a href="gekozen-solo-2026-11/">Bekijk de gecombineerde boodschappenlijst voor aardappelgratin, pindakikkererwten en paddenstoelensoep</a>.</p></section></main>',1)
  home.write_text(txt,encoding="utf-8")
print("OK homepage navigation")
