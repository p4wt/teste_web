elements_queries = {
    "barra_pesquisa": "$('#lst-ib').text",
    "botao_pesquisar": "btnK"}


dic_urls = {
    "google": "https://www.google.com.br",
    "uol": "https://www.gaaaaaa",}

dic_navegador = {
    "Firefox": "Firefox"
}
def get_text(context, elemento):
    return context.driver_execute_script('return {}'.format(elemento))
