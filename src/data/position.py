class UnableToReadLetter(Exception):
    pass

class UnableToWriteLetter(Exception):
    pass

class Position():
    def __init__(self, num_line: int, num_column: int) -> None:
        self.line = num_line
        self.column = num_column

    @classmethod
    def column_letters(self, num_column: int):
        # TODO IMPROVE ALGORITHM TO PERFORM MORE THAN 26 COLUMNS
        if num_column > 26:
            raise UnableToWriteLetter("Sorry, the system is unable to do this action for now.")
        line_letters = chr(num_column + 97)
        return line_letters.title()

    @classmethod
    def line_letters(self, num_line: str):
        column_letters_int = int(num_line) + 1
        return str(column_letters_int)

    def letters(self):
        return f"{Position.column_letters(self.column)}{Position.line_letters(self.line)}"
    
    @classmethod
    def init_by_letters(cls, letters: str):
        letter_size = len(letters)
        if letter_size < 2:
            raise UnableToReadLetter("Letter position should be more than 1 chars")

        ends_alpha_in = None
        ends_numeric_in = None
        starts_alpha_in = None
        starts_numeric_in = None
        for index, letter in enumerate(letters):
            if letter.isalpha():
                if ((ends_alpha_in != None) and (ends_alpha_in != index - 1)):
                    raise UnableToReadLetter(f"There is a lost char \"{letter}\" on the letters")
                starts_alpha_in = index if starts_alpha_in == None else starts_alpha_in
                ends_alpha_in = index
            elif letter.isnumeric():
                if ((ends_numeric_in != None) and (ends_numeric_in != index - 1)):
                    raise UnableToReadLetter(f"There is a lost char \"{letter}\" on the letters")
                starts_numeric_in = index if starts_numeric_in == None else starts_numeric_in
                ends_numeric_in = index
            else:
                raise UnableToReadLetter(f"The character {letter} is not alpha or numeric")

        # A = 0
        # B = 1
        # AA = 26
        # BB = (26 * 2) + 1
        # AAA = (26 * 26 * 1)
        # BAA = (26 * 26 * 2)
        # BCA = (26 * 26 * 2) + (26 * 3)
        column_num = 0
        for i in range(starts_alpha_in, ends_alpha_in + 1):
            index = (ends_alpha_in - i)
            letter_int = ord(letters[index].lower()) - 96
            column_num += (letter_int * (26**i))

        line_num = int(letters[starts_numeric_in:ends_numeric_in+1])
        return cls(line_num - 1, column_num - 1)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.line == other.line) and (self.column == other.column)
        else:
            return False