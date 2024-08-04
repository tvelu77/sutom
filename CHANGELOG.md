# v4.5 (18/04/2023)

## Fixes

- Fixed an option (f3b2af7327c1812778aa2f6e54740b42eebb61cb).

## Changes

- Refactoring of the code (0d9a6cd956d3ad7bbb0fbbcc29b2896fc0dabcc3).

---

# v4.4 (18/04/2023)

## Changes

- Better package system (8373cff5b7bc90432c4d6675288e00f3885e5715).

---

# v4.3 (18/04/2023)

## Fixes

- Better debug handling (3c8f8427da4c2212471f518923029a29d786bd99).
- Limit bug is now fixed (closes issue #12).

## Changes

- The "losing" message shows the word to guess (closes issue #11).

---

# v4.2 (11/04/2023)

## Features

- The player can now choose to set two limits, max and min for the number of characters (1ef8e771922f277cacaf12391035d466665eb7f8).

## Changes

- Cleaning packages.

---

# v4.1 (04/04/2023)

## Changes

- The game now shows the seed and set a default seed if not given (909861ba7e8c5ca51f87538d10ffc3dc94bbf021).

---

# v4.0 (04/04/2023)

## Features

- The game has a new option (--seed) to set the seed for the random word (3611f083e234475e645acf8f79c0667ca9078f76).

## Changes

- Refactoring of constant value (433826b92dba3d1487a7e30881456ba39af93faf).
- Removed unnecessary import in the __init__.py (81e276b0070025989b3d4abc39df7ffdce770c6a and 7facca1dbed7678bbc638c2efae9062dc714d76f).
- Removed useless functions after the constant refactoring (65226435bb4b7a538a88971a2aa82cf9db0320ec).
- Changed functions calls (382acf6eeea84e19aa3e8ad7535f10eaa975baf5).
- Updated debug_tools.py to be independent of other packages (32bec0a3a6c17cf833582e2a8349d6710e20b44a).
- Removed debug_tools_const.py (24d02bb9cd2c7f16f7e3ecab9c1db0bd45acbe7b).

## Fixes

- The user's input is now in lower case in case that the user has written in upper case (0e4df5cf7d44b967bf697413bba6eab9d9ef6099).
- Fixed a bug where the program would crash if the config file is incorrectly formatted (bf1e3d2f2d3a6702cfc3a6a891b2bc50d8ceddd6).
- Fixed and closed issue #6.
- Fixed and closed issue #7.
- Fixed and closed issue #8.
- Fixed and closed issue #9.

---

# v3.6 (27/03/2023)

## Features

- The game has a new option (--target/t) to set the word to guess (25f0caf835289dab3ae1c947032cfb4f17be9f80).

## Fixes

- Fixed a bug (a8e2e3a17d5487fd6eddcda2cad884fe256a5685).

---

# v3.5 (26/03/2023)

## Features

- The game shows if a character exist but is wrongly placed (a7a3bb0c506427c7c3d7efd5805599cd46e559e1).

---

# v3.4 (21/03/2023)

## Changes

- The game shows special characters like "-" (e83066ecbe7cb2680b0ae005efdc3d063f0af93e).
- Now, the loading message is deleted after the game has finished to load (e83066ecbe7cb2680b0ae005efdc3d063f0af93e).

## Fixes

- Fixed and closed issue #3.

---

# v3.3 (21/03/2023)

## Changes

- Replaced the winning message with cleaner message (7b8a4e91b27eb0433fcde8f25ccaa6c6754f9fa1).

## Fixes

- Fixed and closed issue #2.

---

# v3.2 (21/03/2023)

## Features

- Added exception handling in case of FileNotFoundError (fb1d4cb2810f5865fa474c1bb3a5007f5066a342).
- Added a dictionary to hold all the config file information (76b4da79eec78444f612c708b0039321ad6a065a).

## Fixes

- Fixed a typo in config file (fb446352974304dcb1051e4018636140ed9ae091).
- Fixed and closed issue #4.

---

# v3.1 (20/03/2023)

## Fixes

- Removed useless debug line where the game would show the hidden word at the start of the game (cc69c913cc7d8804fbfdac2b5b430607a73206c8).

---

# v3.0 (17/03/2023)

## Features

- Nearly added ability to change the words file with the config.txt (a6e5b4ab0a78c9f6859b890bc2da2e404b51d469).
- Prepared to add refactoring for user's input (7b65c490b020ff384e2c5aa08bed6e42da4726ce).

## Changes

- Package refactoring (7b076c7664260eb6fe7eaac409dcf6ca941dc397).
- Better import management thanks to __init__ files (452734f8e63903e59155d2a69adc62204153a691).

---

# v2.0 (14/03/2023)

## Features

- Word generation with a file is added (38e7b43a514f11f980f150d9c8a1bb913079b4cf).
- Added Lexique383.tsv file (2b28e15294f2881a86940c6bcb4ed43786913ea0).

## Changes

- PyCharm migration as well as checkstyle improvement (6c0e3cfeab672b8c85040b5ccfafddd38639d0f7).

---

# v1.3 (14/03/2023)

## Features

- Added gitignore (bb5cbffb21fc348974b48797910fc082ebbfb023).

## Fixes

- Added a return to avoid any problem (816730e31d4425259631631af1f9828be53f421e).

---

# v1.2 (14/03/2023)

## Fixes

- Changed spaces by dots to help the user (db51351919fc06b7c4aef018a0658685a065c844)

---

# v1.1 (14/03/2023)

## Fixes

- Removed an useless print (1d8d5f91d5c5711c65233a1cbbdf48244a49c97b)

---

# v1.0 (14/03/2023)

## Features

- Added a changelog file to list all the changes (7a6d0ebcbaac3dccccd2f4eb88fbab2fc418ea91).
- Added a main.py (262cd8b94444896eeb6fdeb8eeef8f586e460efb).
- Added a winning and losing condition to the game (48cdceb262daea5bd647636e407919e4e23a363b).
- Added words comparaison to help the user (4303dbe1f387b1c099bcb273abcc8b702b615db5).