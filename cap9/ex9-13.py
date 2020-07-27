from collections import OrderedDict

glossary = OrderedDict()

glossary['variable'] = 'A piece of data'
glossary['function'] = 'A code subroutine'
glossary['program'] = 'Set of algorithms generally written in a programming language to solve a problem'

for word, meaning in glossary.items():
    print(word.title() + " = " +meaning)
    