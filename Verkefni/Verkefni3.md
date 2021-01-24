## Verkefni 3 (14%)

---

#### 3.1 Að búa til JSON (5%)

1. Búðu til eftirfarandi Json skrá `frettir.json`:

```JSON
{
 "frettir": [
	{
        "id":"0",
        "titill":"Fyrirsögn",
        "innihald":"Meginmálstexti",
        "hofundur":"Guðmundur",
        "netfang": "GG@tskoli.is",
        "mynd": "/Gudmundur.png"
    }
 ] 
}
```
Bættu einni fréttafærslu til viðbótar beint í Json skránna.

2. Útfærðu app í Flask sem bætir við tveimur fréttafærslum í `frettir.json`.


#### 3.2 Að lesa JSON skrá í Flask app. (9%)

- Búðu til app með Flask sem birtir allar fréttafærslur (fyrirsögn, innihald, höfundur, netfang og slóð á mynd) úr JSON skrá  `frettir.json` sem þú bjóst í lið 3.1.

- Notaðu `routing` útfærslu, `template`, CSS stílsíðu, ljósmyndir og útfærðu HTTP error síðu til að ná þessu fram.

---

### Námsmat og skil
Gefið er hálft fyrir lið sem er ábótavant.

- 3.1. 
    - að búa til JSON skrá (1%)
    - að skrifa í JSON skrá (4%)
- 3.2
    - að lesa úr JSON skrá (5%)
    - routing útfærsla (2%)
    - templates (1%)
    - CSS og myndir (1%)

Skilaðu á Innu e. private Github tengil sem innheldur kóðaskrár og gögn. Engin sein skil eru í boði.

Gangi þér vel! 
