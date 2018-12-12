# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:14:15 2018

@author: Hellunicorn
"""

class Modele():
    def __init__(self):
        
        self.plateau = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
    
    def jouer(self, indice):
        nb = self.plateau [indice]
        self.plateau[indice] = 0
        retour = 0
        for i in range(nb):
            pos = i + indice + 1
            while pos > len(self.plateau) - 1:
                pos -= len(self.plateau)
            self.plateau[pos] += 1
            retour = pos
        return retour
        
    def vider(self, joueur, case):
        if joueur == 1:
            nb1 = self.plateau[case]
            nb2 = self.plateau[case - 7]
            self.plateau[case] = 0
            self.plateau[case - 7] = 0
            self.plateau[13] += nb1 + nb2
        if joueur == 2:
            nb1 = self.plateau[case]
            nb2 = self.plateau[case + 7]
            self.plateau[case] = 0
            self.plateau[case + 7] = 0
            self.plateau[6] += nb1 + nb2
            