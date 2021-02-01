## Running the 1960s Burgeson baseball game in an IBM 1620 emulator

You will need [SIMH](https://github.com/simh/simh) 4, as the 1620 emulation in SIMH 3 is incomplete and cannot run the game.

* Get the i1620 binary for your platform:
    * Windows: Download SIMH and extract the i1620 binary: [Windows builds of SIMH](https://github.com/simh/Win32-Development-Binaries)
    * Linux, Mac: Build SIMH 4 from source. Use ```make i1620``` to only build that binary.
* Run ```i1620 base.simh```. The game should start. Enter date, time and the names of nine players (or just a random first letter instead). Then the simulation will run.
* To quit SIMH, press Ctrl-E and then enter q and press Return.

### Files

#### Games

* 1620_11.0.013_tic_tac_toe.crd: Tic-tac-toe game (CRD format)
* 1620_11.0.032_bbc_baseball.crd: Baseball game (CRD format)
* 1620_baseball.pdf: Original baseball game instructions
* base.log.txt: Log of a sample program run
* base.simh: Baseball game emulator script
* base.txt: Baseball game (TXT format)
* tic.simh: Tic-tac-toe game emulator script
* tic.txt: Tic-tac-toe game (TXT format)

#### Other files

* crd2asc.py: Convert CRD to TXT format for running in SIMH
* crd_format_hex.txt: Explanation of CRD file encoding (two bytes per punched card character)
* dis1620.py: Disassemble 1620 TXT file
* X26-5852-2_1620_Model_2_Reference_Card.pdf: IBM 1620 Model 2 reference card

### YouTube videos about the 1620 baseball game

* [The Story of the First Baseball Video Game Ever Made | Friday Night Arcade](https://www.youtube.com/watch?v=IbH7UZ83kzY)
* [IBM 1620 Software Library](https://www.youtube.com/watch?v=N12pQBiRd7A&t=2208)

### Links

* [IBM 1620 games (CRD format)](http://bitsavers.informatik.uni-stuttgart.de/bits/IBM/1620/games/) from Bitsavers
