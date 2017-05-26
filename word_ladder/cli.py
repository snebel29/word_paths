"""
Word ladder

Usage:
  word_ladder from <from> using <dict_file> [-a]
  word_ladder from <from> to <to> using <dict_file> [-a]
  word_ladder -h | --help
  word_ladder -v | --version

Subcommands:
  from              The initial word
  to                The word to stop [Optional]

Options:
  -a, --all-paths    Print all paths
  -h, --help         Show this screen
  -v, --version      Show version

Examples:
  word_ladder from word1 using /english.dict
  word_ladder from word1 using /english.dict --all-paths
  word_ladder from word1 to word2 using /english.dict -a
"""

from docopt import docopt
from word_ladder import WordLadder, __version__

def run_ladder(args):
    result = WordLadder(
        args['<dict_file>'], bool(len(args['<from>']) != len(args['<to>']))).find_path(
            args['<from>'],
            args['<to>'],
            bool(args['--all-paths']
        )
    )

    print('path: {0}'.format(result))

def main():
    run_ladder(docopt(__doc__, version=__version__))

if __name__ == '__main__':
    main()
