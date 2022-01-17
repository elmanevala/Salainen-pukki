# -*- coding: utf-8 -*-
import smtplib, ssl
import random

def viesti(pukki, pukin_sp, lahjan_saaja):
    context = ssl.create_default_context()

    viesti = f"{pukin_sp}\nJoulutervehdys, {pukki} \n Tervetuloa mukaan Taavilan tilan suurenmoiseen secret santa -spektaakkeliin. Sinä, mainio pukkinen, ostat lahjan henkilölle: {lahjan_saaja}"
    return viesti

def laheta_sahkoposti(pukki, pukin_sp, lahjan_saaja):
    context = ssl.create_default_context()
    arpoja_sposti = ""
    arpoja_salis = ""

    viesti = viesti(pukki, pukin_sp, lahjan_saaja)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        print(server.login(arpoja_sposti, arpoja_salis))
        print(server.sendmail(arpoja_sposti, pukin_sp, viesti))


pukit = ["Dan", "Dennart", "Eepu", "Sirpa", "Kada", "Epe"]
sahkopostit = [""] * 6 #pukkien sähköpostit pukki-listassa olevassa järjestyksessä
pukki_lkm = len(pukit)
ei_lahjaa = [True]*pukki_lkm

i = 0

while(i < pukki_lkm):  
    arpoja = random.randint(0,pukki_lkm)
    pukki = pukit[i]
    if ei_lahjaa[arpoja] and arpoja!=i:
        ei_lahjaa[arpoja] = False
        print(viesti(pukki, sahkopostit[i], pukit[arpoja]))
        ## laheta_sahkoposti(pukki, sahkopostit[i], pukit[arpoja])
        i = i+1
    print("") 
