![IBM 1620](ibm.png "IBM 1620")

## Running the 1960s Burgeson baseball game in an IBM 1620 emulator

You will need either [OpenSIMH](https://opensimh.org/) or a recent version of [SIMH](http://simh.trailing-edge.com/). Alternatively, my own [IBM 1620 emulator in Python](https://github.com/mdoege/Py1620) can also run the baseball game, so that is another option.

When using SIMH:

* Get the i1620 binary for your platform:
    * Windows: Download SIMH and extract the i1620 binary: [Windows builds of SIMH](https://github.com/simh/Win32-Development-Binaries)
    * Linux, Mac: Build SIMH from source. Use ```make i1620``` to only build that binary.
* Run ```i1620 base.simh```. The game should start. Enter date, time and the names of nine players (or just a random first letter instead). Then the simulation will run.
* To quit SIMH, press Ctrl-E and then enter q and press Return.

### Roster of players

The game includes a roster of 90 players:
```
ANSON           DELAHANTY       HEGAN           LOMBARDI        RUFFING
APPLING         DICKEY          HEILMANN        L WANER         RUTH
AVERILL         DIMAGGIO        HENRICH         MACK            SEWELL
BAKER           DUFFY           HERMAN          M. BURG         SIMMONS
BENSON          E COLLINS       HORNSBY         MCGRAW          SISLER
BERRA           FELLER          HUBBELL         MEDWICK         SPAHN
BOUDREAU        FOXX            JACKSON         MIZE            SPEAKER
BROUTHERS       FRISCH          J. BURG         MUSIAL          TERRY
BURKETT         GEHRIG          J COLLINS       NEWHOUSER       TRAVIS
C. BURG         GEHRINGER       JENNINGS        O DOUL          TRAYNOR
COBB            GORDON          JOHNSON         O ROURKE        TROSKY
COCHRANE        GREENBERG       KAMM            OTT             TUMBLIN
CRAWFORD        GROH            KEELER          P WANER         VAUGHAN
CRONIN          GROVE           KELL            RADBOURNE       WAGNER
CROSETTI        HACK            KELLY           RADCLIFF        WHEAT
CUYLER          HAMILTON        KELTNER         REISER          WILLIAMS
DANNING         HARTNETT        LAJOIE          RICE            YORK
D DEAN          HAYES           LAZZERI         ROBINSON        YOUNG
```

### IBM 1620 software catalog entry (1971)

![catalog](software_catalog_1971.png "1971 software catalog")

### Files

#### Games

* Baseball
    * 11.0.032_BBC_Baseball_Simulation_and_Demonstrator.pdf: *1620 General Program Library: B B C Baseball Simulation and Demonstrator*
    * 1620_11.0.032_bbc_baseball.crd: Baseball game (CRD format)
    * 1620_baseball.pdf: Original baseball game instructions
    * base.log.txt: Log of a sample program run
    * base.simh: Baseball game emulator script
    * base.txt: Baseball game (newer version 11.0.032; TXT format)
    * bbc1.txt: Baseball game (older version "BBC VERSION 1K 8/14/61" 11.0.007, same as the sample run in the manual; TXT format)
* Tic-tac-toe (2D)
    * 1620_11.0.013_tic_tac_toe.crd: Tic-tac-toe game (CRD format)
    * tic.simh: Tic-tac-toe game (emulator script)
    * tic.txt: Tic-tac-toe game on a 3x3 grid (TXT format)
* Tic-tac-toe (3D)
    * tic3d.simh: 3D tic-tac-toe game (emulator script)
    * tic3d.txt: 3D tic-tac-toe game on a 4x4x4 grid (TXT format)

#### GOTRAN

GOTRAN is a FORTRAN-like interactive programming language for the IBM 1620. The user enters a program and then after a final "END" line, the machine halts. Starting the computer with "c" runs the GOTRAN program. GOTRAN features some extra commands not present in standard FORTRAN, such as PLOT.

* C26-5594-1_IBM_1620_GOTRAN_Interpretive_Programming_System_1961.pdf: GOTRAN manual
* gotran.simh: emulator script
* gotran.txt: card deck
* gotran_demo.txt: GOTRAN demo run (see Fig. 16 in manual)

#### Other files

* cb2asc.py: Convert CHM column binary format to SIMH ASCII
* crd2asc.py: Convert CRD binary format to SIMH ASCII
* crd_format_hex.txt: Explanation of CRD file encoding (two bytes per punched card character)
* dis1620.py: Disassemble 1620 TXT file
* X26-5743-2_1620_Model_1_Reference_Card.pdf: IBM 1620 Model 1 reference card
* X26-5852-2_1620_Model_2_Reference_Card.pdf: IBM 1620 Model 2 reference card

### YouTube videos about the 1620 baseball game

* [The Story of the First Baseball Video Game Ever Made | Friday Night Arcade](https://www.youtube.com/watch?v=IbH7UZ83kzY)
* IBM 1620 Software Library: at <https://www.youtube.com/watch?v=N12pQBiRd7A&t=2208> and later in the same video at <https://www.youtube.com/watch?v=N12pQBiRd7A&t=3813>

### Links

* [IBM 1620 games (CRD format)](http://bitsavers.informatik.uni-stuttgart.de/bits/IBM/1620/games/) from Bitsavers
* [IBM 1620 image](https://commons.wikimedia.org/wiki/File:IBM_1620.jpg) by Todd Dailey, CC BY-SA 2.0 <https://creativecommons.org/licenses/by-sa/2.0>, via Wikimedia Commons

