#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:21:35 2020

@author: formation
"""
# -*- coding: utf-8 -*-
# import mysql.connector as mc

# -------------------------------------------------------------------------
# Creation des différentes classes
# -------------------------------------------------------------------------
class Client:
    def __init__(self, id_client, numCompte, nom, prenom, adresse, score=0):
        self.id_client = id_client
        self.numCompte = numCompte
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.score = score
        self.test = 0

class Compte:
    def __init__(self, id_compte, id_client, solde):
        self.id_compte = id_compte
        self.id_client = id_client
        self.solde= solde

class Operations:
    def __init__(self, id_operation, id_compte, nb_operations, nb_decouverts_dans_l_annee):
        self.id_operation = id_operation
        self.id_compte = id_compte
        self.nb_operations = nb_operations
        self.nb_decouverts_dans_l_annee = nb_decouverts_dans_l_annee

class Credits:
    def __init__(self, id_credit, nom, prenom, num_comptes, credit_accorde):
        self.id_credit = id_credit
        self.nom = nom
        self.prenom = prenom
        self.num_comptes = num_comptes
        self.credit_accorde = credit_accorde
# -------------------------------------------------------------------------

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Instancier une connexion
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# mydb  = mc.connect(
#     host="localhost",
#     user="jloyau",
#     password="toto"
# )

# # --------------
# # TEST ET CURSOR
# # --------------
# #print (mydb)
# sql_req = mydb.cursor()
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Recuperation des donnees de SQL
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sql_req.execute("use banque")

# sql_req.execute("SELECT * FROM banque.clients")
# clients_table = sql_req.fetchall()

# sql_req.execute("SELECT * FROM banque.comptes")
# comptes_table = sql_req.fetchall()

# sql_req.execute("SELECT * FROM banque.operations")
# operations_table = sql_req.fetchall()

# mydb.commit()
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ------------------------------------------------
# INPUTS ALEATOIRES POUR TESTER EN AVANCE DE PHASE
# ------------------------------------------------
client1 = '"11", "0001", "toto", "titi", "1 rue de paris"'
client2 = '"22", "0002", "totu", "titu", "2 rue de paris"'
clients_table = [client1,client2]
# print(clients_table)
compte1 = '"AAA1", "11", "1000"'
compte2 = '"AAA2", "22", "2000"'
comptes_table = [compte1,compte2]
# print(comptes_table)
op1 = '"OP1", "AAA1", "9", "1'
op2 = '"OP2", "AAA2", "30", "3'
operations_table = [op1,op2]
# print(operations_table)
# ------------------------------------------------

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Recuperation des donnees de la BD SQL "Banque" qui a été créée au préalable
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# TAB_CLIENTS : liste contenant autant de elements Class qu'il y a de clients
TAB_CLIENTS = []
for ligne in clients_table:
    ligneSplit = ligne.split(", ")
    elt = Client(ligneSplit[0], ligneSplit[1], ligneSplit[2], ligneSplit[3], ligneSplit[4])
    TAB_CLIENTS.append(elt)

# TAB_COMPTES : liste contenant autant de elements Class qu'il y a de clients
TAB_COMPTES = []
for ligne in comptes_table:
    ligneSplit = ligne.split(", ")
    elt = Compte(ligneSplit[0], ligneSplit[1], ligneSplit[2])
    TAB_COMPTES.append(elt)

# TAB_COMPTES : liste contenant autant de elements Class qu'il y a de clients
TAB_OPERATIONS = []
for ligne in operations_table:
    ligneSplit = ligne.split(", ")
    elt = Operations(ligneSplit[0], ligneSplit[1], ligneSplit[2], ligneSplit[3])
    TAB_OPERATIONS.append(elt)
    
print(TAB_CLIENTS[0].id_client)
print(TAB_COMPTES[0].id_compte)
print(TAB_OPERATIONS[0].id_operation)

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# Commandes pour info
# ---------------------------------------------------------------------------
# #excecuter la requette
# sql_req.execute("SELECT * FROM banque.clientBanque")

# #capturer le résultat et le stoquer dans 'clients_table'
# clients_table = sql_req.fetchall()

# sql_req.execute('insert into banque.clientBanque(identifiant,nom,prenom,adresse,num_compte) values ("101","xoxo","vovo","1 rue de vovo","112");')
#mydb.commit()
# #boucle pour afficher le contenu de la table capturee ci-dessus
# for ligne in clients_table:
#     print(ligne)





















        
        
        
