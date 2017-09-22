from pages.auxiliar import elements_queries, dic_urls, dic_navegador
from selenium import webdriver
from behave import step
from pages.google import Google, Gmail
import time


@step('entro no google')
def abre_navegador(context):
    # assert False
    context.google = Google(context.driver)
    context.google.navigate()


@step('pesquiso "{receitas}"')
def pesquisa_as_parada(context, receitas):
    context.google.search(receitas)


@step('abro o Firefox')
def abrir(context):
    context.gmail = Gmail(context.driver)
    context.gmail.acesso_pagina()


@step('coloco meu login')
def login(context):
    context.gmail.execute_login(context.google_user, context.google_passwd)


@step('aguardo um minuto')
def afuardo(context):
    time.sleep(10)
