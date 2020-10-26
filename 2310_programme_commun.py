#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:21:35 2020
########
@author: formation
"""
# -*- coding: utf-8 -*-
import mysql.connector as mc

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

    def calculScore(self, solde, nb_operations, nb_decouverts):
        if solde >=0:
            self.score = 0 + nb_operations/100.0 - nb_decouverts/12.0
        elif solde < 0:
            self.score = -0.5 + nb_operations/100.0 - nb_decouverts/12.0

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

    def __init__(self, id_credit,id_client, nom, prenom, num_comptes, credit_accorde):
        self.id_credit = id_credit
        self.id_client = id_client
        self.nom = nom
        self.prenom = prenom
        self.num_comptes = num_comptes
        self.credit_accorde = credit_accorde
        
    def calculInterets12Mois(self):
        self.interets = self.credit_accorde * 0.05
        return self.interets
    
    def valeurFutureCredit(self,n): #n = durée du crédit en mois formule valeur_future = valeur_initiale(1+taux_d_interet_annuel)**(nb_annuites)
        return self.credit_accorde * (1.05 ** (n/12))
# -------------------------------------------------------------------------

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Instancier une connexion
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mydb  = mc.connect(
        host="localhost",
        user="group1",
        password="formation"
 )

# # --------------
# # TEST ET CURSOR
# # --------------
print (mydb)
sql_req = mydb.cursor()
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Recuperation des donnees de SQL
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sql_req.execute("use banque2")

sql_req.execute("SELECT * FROM banque2.clients")
clients_table = sql_req.fetchall()

sql_req.execute("SELECT * FROM banque2.comptes")
comptes_table = sql_req.fetchall()

sql_req.execute("SELECT * FROM banque2.operations")
operations_table = sql_req.fetchall()

mydb.commit()
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ------------------------------------------------
# INPUTS ALEATOIRES POUR TESTER EN AVANCE DE PHASE
# ------------------------------------------------
"""
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
"""
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Recuperation des donnees de la BD SQL "Banque" qui a été créée au préalable
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# TAB_CLIENTS : liste contenant autant de elements Class qu'il y a de clients
TAB_CLIENTS = []
for ligne in clients_table:
    #print(ligne)
   # ligneSplit = ligne.split(", ")
    elt = Client(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4])
    TAB_CLIENTS.append(elt)

# TAB_COMPTES : liste contenant autant de elements Class qu'il y a de clients
TAB_COMPTES = []
for ligne in comptes_table:
    #ligneSplit = ligne.split(", ")
    elt = Compte(ligne[0], ligne[1], ligne[2])
    TAB_COMPTES.append(elt)

# TAB_COMPTES : liste contenant autant de elements Class qu'il y a de clients
TAB_OPERATIONS = []
for ligne in operations_table:
    #ligneSplit = ligne.split(", ")
    elt = Operations(ligne[0], ligne[1], ligne[2], ligne[3])
    TAB_OPERATIONS.append(elt)
    
print(TAB_CLIENTS[0].id_client)
print(TAB_COMPTES[0].id_compte)
print(TAB_OPERATIONS[0].id_operation)

#creation table credit
sql_req.execute("create table credits (id_credit int(20) not null auto_increment primary key, id_client int(20) not null, nom char(20) not null, prenom char(20) not null, numero_comptes char(100) not null, credit_accorde int(20))")

# Calcul du score dans Client
for elt in TAB_CLIENTS:
    ID = elt.id_client
    for elt2 in TAB_COMPTES:
        if elt2.id_client == ID:
            COMPTE = elt2.id_compte
            SOLDE = elt2.solde
            break
    for elt2 in TAB_OPERATIONS:
        if elt2.id_compte == COMPTE:
            NB_OPERATIONS = elt2.nb_operations
            NB_DECOUVERTS = elt2.nb_decouverts_dans_l_annee
            break
    #print (SOLDE, NB_OPERATIONS, NB_DECOUVERTS)
    elt.calculScore(SOLDE, NB_OPERATIONS, NB_DECOUVERTS)

#for elt in TAB_CLIENTS:
#   print (str(elt.score))

#création de la colonne score dans la table clients
sql_req.execute('alter table banque2.clients add score float;')

# Modification des valeurs score dans Clients
for elt in TAB_CLIENTS:
    sql_req.execute('update banque2.clients set score="' + str(elt.score) + '" where identifiant=' + str(elt.id_client) + ';')

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#condition accord crédit : score > 0,4
#Montant du crédit 10000*score : exemple si score = 0.5 => crédit = 5000 sur 12 mois avec un TJM de 5%
#Requete SQL pour aller chercher la table credit
#sql_req.execute("SELECT * FROM banque2.credits")
#credits_table = sql_req.fetchall()

#Requete SQL pour aller chercher la table clients avec la colonne score
#sql_req.execute("SELECT * FROM banque2.clients")
#clients_table = sql_req.fetchall()



#nouvelle classe client2 avec l'ajout de la colonne score


#creation de la table python à partir de la table SQL avec le score
#TAB_CREDITS = []
#for ligne in credits_table :
#    elt = Credit(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4], ligne[5])
#    TAB_CREDITS.append(elt)

# ajout des valeurs de credit dans la table python à partir des valeurs de scores.
for ligne in  TAB_CLIENTS :
    if ligne.score >0.4:
        valeur_credit= ligne.score*10000
        print(valeur_credit)
        req = "insert into banque2.credits (id_client, nom, prenom, numero_comptes, credit_accorde) values(%s,%s,%s,%s,%s)"
        sql_req.execute(req,(ligne.id_client,ligne.nom,ligne.prenom,ligne.numCompte,valeur_credit ))

# requete pour modifier les data SQL  à partir de la table python, ne fonctionne pas.
#req = "insert into banque2.credits (credit) values (%s)"
#for i in TAB_CREDITS:
#    sql_req.execute(req,i)

mydb.commit()


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


# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Lecture table credits
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sql_req.execute("SELECT * FROM banque2.credits")
credits_table = sql_req.fetchall()


# TAB_CREDITS : liste contenant autant de elements Class qu'il y a de credits
TAB_CREDITS = []
for ligne in credits_table:
    elt = Credits(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4],ligne[5])
    TAB_CREDITS.append(elt)

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Calcul bénéfice banque 12 mois
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
benefice = 0
for ligne in TAB_CREDITS:
    benefice += ligne.calculInterets12Mois() 
    
print("benefice de la banque au bout de 12 mois : ",benefice)

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Pour gagner 10 fois plus, calculer la durée de crédit optimale pour chaque crédit
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

gain_espere = 10 * benefice
valeur_future_credits = 0
valeur_initiale_credits = 0

#calcul de la valeur initiale des crédits
for ligne in TAB_CREDITS:
        valeur_initiale_credits += ligne.credit_accorde

#calcul de la valeur de n qui permet d'atteindre ou dépasser le gain espéré
n=12
while (valeur_future_credits - valeur_initiale_credits) < gain_espere: 
    n += 1
    valeur_future_credits = 0
    for ligne in TAB_CREDITS:
        valeur_future_credits += ligne.valeurFutureCredit(n)
      
print("Pour gagner 10 fois plus, proposer la durée de crédit de :", str(n),"mois")
