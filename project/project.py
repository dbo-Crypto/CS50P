import random
import sys
import requests
from pyfiglet import Figlet


def get_language() -> str:
    """
    Get the user prefered language from the menu.

    :raise ValueError: If user choice is not in the displayed menu
    :rtype: str
    """

    print("Please select the language for the game")
    lang_list: str = ["english", "french", "german", "italian", "spanish"]
    for i in range(len(lang_list)):
        print(f"{int(i)+1}. {lang_list[i]}")
    while True:
        choice: int = int(input("Type choice number: "))
        if choice in range(1, 6):
            choice = lang_list[choice - 1]
            return choice
        else:
            raise ValueError("Invalid choice")


def load_dict(language: str) -> list:
    """
    Load a word list in the language selected by the user.
    Also, create a file named "word_list.txt" that will be used by the testing module.

    :param language: Preferred language selected by user.
    :type language: str
    :raise FileNotFoundError: If unadvertently, the user select a language that is not in the list.
    :return: A list of words in the selected language.
    :rtype: list
    """

    try:
        with open(f"{language}.txt", "r", encoding="utf-8") as file:
            word_list = []
            for lines in file:
                lines = lines.replace("\n", "")
                if "�" not in lines:
                    word_list.append(lines)
            with open(f"word_list.txt", "w", encoding="utf-8") as fp:
                for i in word_list:
                    fp.write(i + "\n")
            return word_list
    except FileNotFoundError:
        sys.exit("Dictionnary not found!")


def select_level() -> list:
    """
    Get the user preferred level of difficulty.
    1 -> Words two to three letters long.
    2 -> Words four to six letters long.
    3 -> Words seven to nine letters long.

    :raise: ValueError: If the user inputs an undefined difficulty.
    :return: A list of possible lenght for the word.
    :rtype: list
    """

    level: int = int(input("Select the difficulty (1, 2 or 3): "))
    if level == 1:
        length = [2, 3]
    elif level == 2:
        length = [4, 5, 6]
    elif level == 3:
        length = [7, 8, 9]
    else:
        raise ValueError
    return length


def select_word(word_list, lenght) -> str:
    """
    Select a word in the word list with the defined length.

    :param word_list: List of word in the selected language.
    :param lenght: Selected lenght of the word.
    :type word_list: list
    :type lenght: list
    :return : A single word.
    :rtype: str
    """

    while True:
        word = random.choice(word_list)
        if len(word) not in lenght:
            pass
        else:
            return word


def check_letter(letter, word, tries, hang_counter) -> str:
    """
    Check if each character of the selected word correspond to the user input.
    If it correspond, replace the masked character '*' by the letter itself.

    :param letter: User input to know if this letter is in the hidden word.
    :param word: Randomly selected word.
    :param tries: State of the search of the hidden word by the user.
    :type letter: str
    :type word: str
    :type tries: str

    """
    splited_word = [*word]
    splited_tries = [*tries]
    for i in range(len(word)):
        if letter == splited_word[i]:
            splited_tries[i] = letter
            tries = "".join([str(item) for item in splited_tries]).replace(" ", "")
    if letter not in splited_word:
        hang_counter -= 1
        print(f"You have {hang_counter} more try to guess the hidden word")
        pass

    return tries, hang_counter


def start_game(word):
    """
    Initate a new game. Hide the randomly seletec word and ask the user to find the letters.

     :param word: Randomly selected word.
     :type :word str
     :return: Anything as the function will loop until the user find the hidden word.

    """
    tries = f"{'*' * len(word)}"
    print(
        f"The game is starting, the word you need to find is {len(word)} letters long."
    )
    hang_counter = 10
    while True:
        if hang_counter == 0:
            print(
                f"You are hanged and you lost the game, the hidden word was {word}..."
            )
            again = input("Do you want to play again? (y/n): ")
            if again == "y":
                main()
            else:
                sys.exit("Bye-bye, thanks for playing!")
        else:
            user_letter = input("What letter do you want to try?: ")
            tries, hang_counter = check_letter(user_letter, word, tries, hang_counter)
            print(f"tries: {tries}")
            if "*" not in tries:
                print(f"You won, the word was {word}!!!!!")
                break


def get_definition(word) -> str:
    """
    Once the user found the hidden word, look-up the definitions of the word using "api.dictionaryapi.dev".

    :param word: Randomly selected word.
    :type :word str
    :raise: Exception if no definitions is found.
    :return: The definition(s) of the word.
    :rtype: str
    """

    print(
        f"Hereunder, are known definitions of the word: {word}. If it exists in the selected dictionnary.\nDefinitions only available for english words.\n"
    )
    try:
        x = requests.get(
            f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        ).json()
        x = x[0]["meanings"][0]["definitions"]
        try:
            for i in x:
                print(i["definition"] + "\n")
        except:
             print("No Definitions Found\n")
        again = input("Do you want to play again? (y/n): ")
        if again == "y":
            main()
        else:
            sys.exit("Bye-bye, thanks for playing!")

    except:
        sys.exit("Bye-bye, thanks for playing!")


def main():
    """
    Main function that will call all the previously detailled functions.
    1. Get the preffered user language for the game.
    2. Load the associated dictionnary.
    3. User select the difficulty of the game.
    4. Game selects a random word corresponding to the difficulty for the user to guess.
    5. Game starts.
    """

    f = Figlet(font="big")
    print(f"{f.renderText('The Hangman game!!!')}")
    language = get_language()
    word_list = load_dict(language)
    level = select_level()
    word = select_word(word_list, level)
    word = "outsourcing"
    #word = "flower"
    start_game(word)
    get_definition(word)


if __name__ == "__main__":
    main()
