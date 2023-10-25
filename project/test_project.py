from io import StringIO
import pytest


"""
For a reason that I could not figure out, I couldn't pytest
of test_project.py was not working when the main() function
was running in project.py.

For that reason, to confirm that the testing is working. I've
copied the function to test in test_project.py
"""


def get_language():
    print("Please select the language for the game")
    lang_list = ["english", "french", "german", "italian", "spanish"]
    for i in range(len(lang_list)):
        print(f"{int(i)+1}. {lang_list[i]}")
    while True:
        choice = int(input("Type choice number: "))
        if choice in range(1, 6):
            choice = lang_list[choice - 1]
            return choice
        else:
            raise ValueError("Invalid choice")


def test_get_language(monkeypatch):
    number_inputs = StringIO("1\n")
    monkeypatch.setattr("sys.stdin", number_inputs)
    assert get_language() == "english"

    number_inputs = StringIO("5\n")
    monkeypatch.setattr("sys.stdin", number_inputs)
    assert get_language() == "spanish"

    with pytest.raises(ValueError):
        number_inputs = StringIO("8\n")
        monkeypatch.setattr("sys.stdin", number_inputs)
        get_language()

    with pytest.raises(ValueError):
        number_inputs = StringIO("cat\n")
        monkeypatch.setattr("sys.stdin", number_inputs)
        get_language()


def load_dict(language):
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


def test_load_dict():
    with open(f"word_list.txt", "r") as test_file:
        test_word_list = []
        for lines in test_file:
            lines = lines.replace("\n", "")
            test_word_list.append(lines)
    assert load_dict("english") == test_word_list

    with open(f"word_list.txt", "r") as test_file:
        test_word_list = []
        for lines in test_file:
            lines = lines.replace("\n", "")
            test_word_list.append(lines)
    with pytest.raises(FileNotFoundError):
        assert load_dict("cat") == test_word_list


def select_level():
    level = int(input("Select the difficulty (1, 2 or 3): "))
    if level == 1:
        length = [2, 3]
    elif level == 2:
        length = [4, 5, 6]
    elif level == 3:
        length = [7, 8, 9]
    else:
        raise ValueError
    return length


def test_select_level(monkeypatch):
    number_inputs = StringIO("1\n")
    monkeypatch.setattr("sys.stdin", number_inputs)
    assert select_level() == [2, 3]

    number_inputs = StringIO("3\n")
    monkeypatch.setattr("sys.stdin", number_inputs)
    assert select_level() == [7, 8, 9]

    with pytest.raises(ValueError):
        number_inputs = StringIO("6\n")
        monkeypatch.setattr("sys.stdin", number_inputs)
        select_level()


"""
As the checks are already done in the functions where
the user is providing data.

There is not need to check the functions select_word() and
check_letter() as we now that the input data is already
verified and correct.
"""
