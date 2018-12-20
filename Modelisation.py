# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:14:15 2018

@author: Hellunicorn
"""

class Modele():
    def __init__(self):
        
        self.plateau = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
    
    def jouer(self, indice):
        """
        Fonction permettant de jouer sur une case

        :param indice: case à jouer
        :return: dernière case jouée
        """
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
        
    def test_dernier(self, retour, joueur):
        """
        Vérification si le dernier point était vide

        :param retour: dernière case
        :param joueur: joueur qui a joué
        :return:
        """
        if self.plateau[retour] == 1:
                if joueur == 1 and retour >= 7 and retour <= 12:
                    self.vider(joueur, retour)
                elif joueur == 2 and retour >= 0 and retour <= 5:
                    self.vider(joueur, retour)
        
    def vider(self, joueur, case):
        """
        Vider une case et sa case en face

        :param joueur: joueur qui a joué
        :param case: case à vider
        :return:
        """
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
    
    def fin(self):
        """
        Vérification si les conditions de fin sont atteintes

        :return boolean: False si fini, True sinon
        """
        if self.plateau[0:6] == [0,0,0,0,0,0]:
                nb = 0
                for i in range (6):
                    nb+= self.plateau[i + 7]
                    self.plateau[i + 7] = 0
                self.plateau[13] += nb
                return False
        elif self.plateau[7:13] == [0,0,0,0,0,0]:
            nb = 0
            for i in range (6):
                nb+= self.plateau[i]
                self.plateau[i] = 0
            self.plateau[6] += nb
            return False
        return True