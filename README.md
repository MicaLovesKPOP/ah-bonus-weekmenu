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

Deze repo is onafhankelijk van Albert Heijn.