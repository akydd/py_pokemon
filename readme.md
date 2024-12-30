# py_pokemon

```sh
usage: py_pokemon.py [-h] file high low

Given a json data file and the high and low placements, return the deck types ordered by percentage used.

positional arguments:
  file        JSON data file to process
  high        highest placing
  low         lowest placing

options:
  -h, --help  show this help message and exit
```

## How to run
1. Ensure you have python installed on your system. You shoud be able to do somsething like this at the command prompt. Your command to run python will vary. If `python3` doesn't work, try `python`.
```sh
python3 --version
Python 3.13.0
```
2. Download both the script (`py_pokemon.py`) and the data file (`data.json`) into the same directory.
3. Pick the range of placements you want to analyse. For example, players ranked 200th to 300th place.
4. Run the script:
```sh
python3 py_pokemon.py data.json 200 300


Charmander                     10.00%
Ralts                          7.00%
Klawf                          6.00%
Regidrago V                    6.00%
Dreepy                         5.00%
Terapagos ex                   5.00%
Comfey                         5.00%
Lugia V                        4.00%
Roaring Moon ex                4.00%
Snorlax                        4.00%
Raging Bolt ex                 4.00%
Gardevoir ex                   3.00%
Lumineon V                     3.00%
Charizard ex                   3.00%
Iron Thorns ex                 3.00%
Pidgeot ex                     2.00%
Pidgey                         2.00%
Cleffa                         2.00%
Hoothoot                       2.00%
Cornerstone Mask Ogerpon ex    1.00%
Sableye                        1.00%
Scream Tail                    1.00%
Mimikyu                        1.00%
Roaring Moon                   1.00%
Magneton                       1.00%
Regidrago VSTAR                1.00%
Archaludon ex                  1.00%
Archeops                       1.00%
Raikou V                       1.00%
Mew ex                         1.00%
Origin Forme Palkia V          1.00%
Gholdengo ex                   1.00%
Drakloak                       1.00%
Miraidon ex                    1.00%
Origin Forme Dialga V          1.00%
Deino                          1.00%
Latias ex                      1.00%
Magnemite                      1.00%
Arceus V                       1.00%
```
