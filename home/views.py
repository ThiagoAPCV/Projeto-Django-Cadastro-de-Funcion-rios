from django.http import HttpResponse

# View principal do app home
def index(request):
    """
    Função que responde quando o usuário acessa a página inicial.
    """
    return HttpResponse("Primeiro app Django funcionando corretamente!")
