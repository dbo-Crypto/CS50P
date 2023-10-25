   # THE HANGMAN GAME
   ### Video Demo:  <https://youtu.be/I2gnpcwBfEA>
   ### Description:

* **Introduction:**

To validate the module CS50P, I have chosen my capstone project to be a multilingue version of the game "The Hangman", where the player has to guess a mistery word in a limited amount of attempts.

* **How to play:**

This version of the game will follow the classic rules of the game.

After the preffered language and the difficulty of the game set by the player, the player will have ten attempts to guess the mistery word taking guesses letter by letters.

At the beginning of the game the mistery word will be completely hidden with a number of '*' equal to the lenght of the word.

The game will take place turn by turn. Each turn, the player is going to input a letter in the game and the game will discover the letter(s) corresponding in the mistery word, or decrease the maximum of possible attempt by one.

If the maximum of possible of attempts reaches zero, then the player lose.
If the player guesses the word before that, he/she wins.

In any case, win or loss, if the selected language is english, a definition, if it exists on the website 'dictionaryapi.dev' will be displayed.

Then the program exit.


* **Files:**

At the root of the folder `/project/`, you will find ten files.

Five of them named : **english.txt**, **french.txt**, **german.txt**, **italian.txt** and **spanish.txt* will be the words list used by the game in different languages.

The file **requirement.txt** will be the python packages installed when the game was developped.

The file **project.py** is the main file of the program that will run the game.

The file **test_project.py** is the pytest file used to test the different modules of the game.

The file **word_list.txt** is a temp file that will be used for the testing to compare the loaded dictionnary to what it needs to be. To test `load_dict()` function.

The file **README.md** is a simple .md file to explain the project.


* **Functions:**

As per the documentation already included in the code itself, hereunder a summary of the program functions.

**get_language() -> str**
Return a string containing the prefered language for the player.

**load_dict(language: str) -> list:**
Load the dictionnary related to the selected language.
Return a list of workd in the preffered language.

**select_level() -> list:**
Ask the user to select the difficulty level.
Return a list of possible hidden word lenght corresponding to the level of difficulty.

**select_word(word_list, lenght) -> str:**
Randomly select a word in the word list corresponding to the selected lenght.
Return a word as a str.

**check_letter(letter, word, tries) -> str:**
Check if the letter given by the player is in the hidden word. If yes, discover it, if not, decrease the number of attemptds by 1.

**start_game(word):**
Function to start the game itself.

**get_definition(word) -> str:**
Get the definition (if possible) of the hidden word, either the player won or lost.


* **Conclusion:**

A personnal word to conlude this capstone project, you guys at CS50 are doing a great job to teach and make programming interresting.
During my universities year, I drifted away from the software development because of bad teachers.
Ten years after, I've found CS50 and my spark for development came back up, and I'm really excited to keep folloing your courses.
Thanks a lot, and keep the great work going.

This was CS50p.