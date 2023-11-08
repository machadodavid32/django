from django.shortcuts import render, HttpResponse

# Função render nos permite renderizar uma página html

# Create your views here.

def pagina_inicial(request):
    return HttpResponse('Pronto para investir')


# Sempre que quisermos criar uma nova página, é necessário entrar neste arquivo views e fazer uma 
# nova função

def pagina_contato(request):
    return HttpResponse('Página de contato')

def minha_historia(request):
    pessoa = {
        'nome': 'Jeff',
        'idade': 28,
        'hobby': 'games'
    }
    return render(request,'investimentos/minha_historia.html', pessoa)
# Esta função acima está encaminhando informações direto pra página. Numa aplicação real,...
# os dado da pessoa podem vir de um banco de dados, sendo atualizado dinamicamente para a pagina. 

def novo_investimento(resquest):
    return render(resquest, 'investimentos/novo_investimento.html')

def investimento_registrado(request):
    investimento = {
        'tipo_investimento':request.POST.get('TipoInvestimento')
    }
    return render(request, 'investimentos/investimento_registrado.html', investimento)
