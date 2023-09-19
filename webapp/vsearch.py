def search4vowels(phrase: str) -> set:
    """Return any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    '''A default value has been assigned to the “letters”argument
    and will be used whenever the calling code doesn’t provide an
    alternate value.'''
    """Return a set of letters found in a supplied phrase."""
    letter = set(letters)
    return letter.intersection(set(phrase))
