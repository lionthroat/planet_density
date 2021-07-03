import kivy
kivy.require('2.0.0');

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty)

import sys

d_list = [0.7, 1.27, 1.33, 1.64, 3.93, 5.24, 5.43, 5.51]
comp_list = ['Gas Giant', 'Ice Giant', 'Gas Planet', 'Gas Planet', 'Rocky Planet', 'Rocky Planet', 'Metal-Rich Rocky Planet', 'Metal-Rich Rocky Planet']
name_list = ['Saturn', 'Uranus', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Mercury', 'Earth']
info_list = [
        'Saturn has the lowest density of all the planets in our Solar System. It is actually less dense than water!',
        'While Uranus has a tiny rocky core, it is largely composed of a mantle of water, ammonia, and methane ice.',
        'Jupiter has a magnetic field 14x stronger than Earth, which acts as a shield to deflect impact.',
        'Neptune is the coldest and most distant planet, with gravity similar to Earth.',
        'Mars is made up a "soft rocky paste" mostly of silicon, oxygen, iron, and magnesium.',
        'The composition of Venus is likely very similar to Earth',
        'Mercury is made up of about 70% metals and 30% silicate. It has the oldest, most pitted surface of any planet in our Solar System.',
        'Earth is the densest planet in our Solar System! The pressure of our own gravitation compresses Earth by a few percentage points.'
    ]

class PlanetGame(BoxLayout):
    def find_match(self):

        # Test Input for Exact Match
        exact_match = False
        planet_key = 0
        for d in d_list:
            if float(self.density.text) == d:
                exact_match = True
                planet_key = d_list.index(d)

        # Case 0: User Quit
        if self.density.text == 'q':
            sys.exit()

        # Case 1: Exact Match
        elif exact_match == True:
            self.input.text = '[b]You Input:[/b] ' + self.density.text + 'g/cm^3'
            self.composition.text = '[b]Composition:[/b] ' + comp_list[planet_key]
            self.match.text = '[b]Exact match![/b] ' + name_list[planet_key] + ' has a density of [b]0.7 g/cm^3[/b]'
            self.info.text = info_list[planet_key]

        # Case 2: Find Closest Match
        else:
            closest_value = d_list[min(range(len(d_list)), key = lambda i: abs(d_list[i]-float(self.density.text)))]
            closest = d_list.index(closest_value)
            self.input.text = '[b]You Input:[/b] ' + self.density.text + 'g/cm^3'
            self.composition.text = '[b]Likely Composition:[/b] ' + comp_list[closest]
            self.match.text = '[b]Your density most closely matches ' + name_list[closest] + '[/b], which has a density of ' + str(d_list[closest]) + ' g/cm^3'
            self.info.text = ''

        self.density.text = '' # clear input field

class PlanetDensityApp(App):
    def build(self):
        game = PlanetGame();
        return game

if __name__ == '__main__':
    PlanetDensityApp().run()
