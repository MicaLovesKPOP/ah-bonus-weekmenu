from pathlib import Path
from html import escape
import json, re

root=Path(r"D:\Projects\AH-Recipes")
gen=root/"publish_individual_recipes.py"
text=gen.read_text(encoding="utf-8")
marker="def page(r):"
assert text.count(marker)==1

inject=r'''
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
    "500 g gedroogde groene spliterwten":"1 pak Hak Spliterwten gedroogd van 500 g",
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
  ("Boursin Knoflook & fijne kruiden, 150 g × 2","https://www.ah.nl/producten/product/wi1983/knoflook-en-fijne-kruiden")
 ],
 "tomaat-aubergine-ragu":[
  ("AH Gemengd gehakt, 500 g × 2","https://www.ah.nl/producten/product/wi561333/ah-gemengd-gehakt"),
  ("AH Goudse belegen 48+ stuk, circa 425 g","https://www.ah.nl/producten/product/wi59669/ah-goudse-belegen-48-stuk"),
  ("AH Biologisch Bloemkoolrijst, diepvries 400 g × 2","https://www.ah.nl/producten/product/wi582622/ah-biologisch-bloemkoolrijst")
 ],
 "dikke-pompoen-spliterwtensoep":[
  ("AH Biologisch Pompoen stukjes, 450 g × 2","https://www.ah.nl/producten/product/wi553673/ah-biologisch-pompoen-stukjes"),
  ("AH Winterpeen, zak 1 kg","https://www.ah.nl/producten/product/wi4076/ah-winterpeen"),
  ("Hak Spliterwten gedroogd, 500 g","https://www.ah.nl/producten/product/wi163791/hak-spliterwten-gedroogd")
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
        r["shop"]="AH Biologisch Pompoen stukjes 450 g, twee stuks, is gunstiger dan drie pakken van 400 g muskaatpompoen. De AH Winterpeen is een zak van 1 kg, geen losse wortel; gebruik de helft en vries het restant in. 'Hak Spliterwten gedroogd' is een herkenbaar product in AH's assortiment."

def product_validation(r):
    items=SHOPPING_LINKS.get(r["slug"],[])
    return ('<section class="card"><h2>Controleer deze AH-producten</h2>'
            '<p>De AH-receptimporter maakt zelf productsuggesties; zelfs bij een exacte naam kan een verkeerde verpakking worden geselecteerd. '
            'Gebruik zo nodig <strong>Wissel</strong> in AH om een van deze exacte artikelen te kiezen. '
            'Controleer ook persoonlijke Bonus Box-aanbiedingen en de beschikbaarheid.</p><ul>'
            +''.join(f'<li><a href="{escape(url,quote=True)}">{escape(name)}</a></li>' for name,url in items)
            +'</ul></section>')
'''

if "INGREDIENT_OVERRIDES={" not in text:
    text=text.replace(marker,inject+"\n"+marker)
# inject direct links before closing main in page()
assert "product_validation(r)" in text or "'</main><footer>" in text
if "product_validation(r)" not in text.split("def page(r):",1)[1]:
    text=text.replace(
      "'</main><footer>Onafhankelijk recept, niet verbonden aan Albert Heijn.",
      "product_validation(r) + '</main><footer>Onafhankelijk recept, niet verbonden aan Albert Heijn."
    )
gen.write_text(text,encoding="utf-8")

# Regenerate the three individual recipe pages from the updated source.
import subprocess,sys
subprocess.run([sys.executable,str(gen)],check=True)

# Reuse the same verified AH product URLs as the recipe generator.
import runpy
SHOPPING_LINKS = runpy.run_path(str(gen))["SHOPPING_LINKS"]

# The combined page is a reference shopping list, NOT a recipe to reimport.
index=root/"index.html"
raw=index.read_text(encoding="utf-8")
updates={
"1 kg kipdijfilet":"2 pakken AH Scharrel kipdijfilet van ca. 480 g",
"1 zak AH vastkokende aardappelen van 3 kg":"1 zak AH Vastkokende aardappelen van 3 kg",
"1 bak AH biologische oesterzwammen van 250 g":"1 bak AH Biologisch Oesterzwammen van 250 g",
"1,5 kg broccoli, bij voorkeur diepvries":"3 zakken AH Broccoliroosjes van 450 g (diepvries, totaal 1,35 kg)",
"200 g belegen of oude Goudse kaas":"1 stuk AH Goudse belegen 48+ stuk (ca. 425 g, gebruik 200 g)",
"1 zak winterpeen van 1 kg (500 g gebruiken)":"1 zak AH Winterpeen van 1 kg (gebruik 500 g)",
"2 zakken pompoenstukjes van 450 g":"2 zakken AH Biologisch Pompoen stukjes van 450 g",
"500 g groene spliterwten":"1 pak Hak Spliterwten gedroogd van 500 g",
"2 pakken bloemkoolrijst van 400 g":"2 pakken AH Biologisch Bloemkoolrijst van 400 g (diepvries)",
"300 g volkoren spaghetti":"1 pak AH Biologisch Volkoren spaghetti 500 g (gebruik 300 g)",
}
for before,after in updates.items():
    hits=raw.count(before)
    assert hits>0,("combined page missing",before)
    raw=raw.replace(before,after)
    print(f"combined update {before}: {hits}")
start=raw.find('<main><section><h2>Importeren in de AH-app</h2>')
if start>=0:
    end=raw.find('</section>',start)
    assert end>0
    notice=('<main><section><h2>Gebruik de losse recepten in de AH-app</h2>'
       '<p class="note"><strong>Let op:</strong> importeer niet opnieuw het gecombineerde weekmenu als één recept '
       '(AH maakt er dan 12 of 18 personen van). Gebruik hieronder de drie losse receptlinks, '
       'ieder voor zes personen. Het gezamenlijke boodschappenoverzicht is uitsluitend naslag.</p></section>')
    raw=raw[:start]+notice+raw[end+len('</section>'):]
    print("combined page: replaced misleading single-recipe import instructions")

# Add links to exact AH catalog items and an explanation why the automatic importer
# might still match a wrong size despite correct wording.
check='<section><h2>Productmatches die belangrijk zijn</h2><p>AH maakt automatische suggesties; controleer vóór toevoegen bij twijfel de juiste variant via de productlinks. Exacte namen vergroten de kans op goede matches, maar garanderen geen juiste SKU.</p><ul>'
for name,url in [
  ("3 kg AH Vastkokende aardappelen",SHOPPING_LINKS["boursin-kip-oesterzwammen"][0][1]),
  ("250 g AH Biologisch Oesterzwammen",SHOPPING_LINKS["boursin-kip-oesterzwammen"][1][1]),
  ("Diepvries AH Broccoliroosjes 450 g",SHOPPING_LINKS["boursin-kip-oesterzwammen"][2][1]),
  ("AH Goudse belegen 48+ stuk",SHOPPING_LINKS["tomaat-aubergine-ragu"][1][1]),
  ("AH Biologisch Bloemkoolrijst 400 g",SHOPPING_LINKS["tomaat-aubergine-ragu"][2][1]),
  ("AH Biologisch Pompoen stukjes 450 g",SHOPPING_LINKS["dikke-pompoen-spliterwtensoep"][0][1]),
  ("AH Winterpeen 1 kg",SHOPPING_LINKS["dikke-pompoen-spliterwtensoep"][1][1]),
  ("Hak Spliterwten gedroogd 500 g",SHOPPING_LINKS["dikke-pompoen-spliterwtensoep"][2][1])
]: check+=f'<li><a href="{escape(url,quote=True)}">{escape(name)}</a></li>'
check+='</ul></section>'
if "Productmatches die belangrijk zijn" not in raw:
    at=raw.find('</main>')
    assert at>=0
    raw=raw[:at]+check+raw[at:]
index.write_text(raw,encoding="utf-8")

# validate each recipe and the combined list with Schema.org JSON-LD
for p in [index,*sorted((root/"recepten").glob("*.html"))]:
    blob=p.read_text(encoding="utf-8")
    js=re.search(r'<script type="application/ld\+json">(.*?)</script>',blob,re.S)
    assert js, p
    parsed=json.loads(js.group(1))
    if p.parent.name=="recepten":
        assert parsed.get("recipeYield")=="6 personen"
        assert all("||" not in i for i in parsed["recipeIngredient"])
        assert len(parsed["recipeInstructions"])>=6
        assert "Controleer deze AH-producten" in blob
    print("verified",p.name,len(parsed["recipeIngredient"]))
