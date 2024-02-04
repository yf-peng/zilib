#!/usr/bin/env python3

from pylib import latin as lib
import zilib
import unittest
import bz2
import csv


class StemmerTest(unittest.TestCase):
    def stem(self, word):
        self.assertEqual(lib.american_english_stem(word), zilib.american_english_stem(word), f'Failed to stem {word}')

    def test_degenerate(self):
        self.stem('')
        self.stem('!')
        self.stem('\n')
        self.stem('\r\n')
        self.stem(' ')
        self.stem('  ')
        self.stem(' latinize ')
        self.stem('latinize greatest')
        self.stem('greatest latinize')

        # These are discrepancies between unicodedecode and stripping away non-ascii characters
        self.assertEqual('gretestlatin', zilib.american_english_stem('greätest latinize'))
        self.assertEqual('latinizegreatest', zilib.american_english_stem('latinize 我 greatest'))
        self.assertEqual('latinizegreatest', zilib.american_english_stem('我latinize我greatest我'))
        self.assertEqual('greatestlatin', zilib.american_english_stem('我greatest我latinize我'))

    def test_simple(self):
        self.stem('caresses')
        self.stem('ponies')
        self.stem('ties')
        self.stem('caress')
        self.stem('cats')
        self.stem('feed')
        self.stem('agreed')
        self.stem('plastered')
        self.stem('bled')
        self.stem('motoring')
        self.stem('sing')
        self.stem('conflated')
        self.stem('troubled')
        self.stem('sized')
        self.stem('hopping')
        self.stem('tanned')
        self.stem('falling')
        self.stem('hissing')
        self.stem('fizzed')
        self.stem('failing')
        self.stem('filing')
        self.stem('happy')
        self.stem('sky')
        self.stem('quickly')
        self.stem('running')
        self.stem('dying')
        self.stem('tying')
        self.stem('flying')

    def test_comprehensive(self):
        # Open ../lists/en_unigram_freq.csv.bz2 and test all words
        with bz2.open('../lists/en_unigram_freq.csv.bz2', 'rt') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                self.stem(row[0])


if __name__ == '__main__':
    unittest.main()