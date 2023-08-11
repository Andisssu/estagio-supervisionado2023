# Repositório da disciplina Estagio Supervisionado

## Configuração do Ambiente Django
- Este repositório contém as instruções necessárias para configurar um ambiente Django. Siga as etapas abaixo para configurar corretamente o ambiente.

## Instalação
### Instalar Python
- Certifique-se de ter o Python instalado em seu sistema antes de prosseguir. Você pode baixar o Python em python.org.

### Instalar Django
Use o seguinte comando para instalar o Django usando o pip:
- pip install django

## Configuração do Ambiente Virtual
### Criar um ambiente virtual
- Execute o seguinte comando para criar um novo ambiente virtual:
- python -m venv myenv

### Ativar o ambiente virtual
- Para ativar o ambiente virtual, use o seguinte comando:
- myenv\Scripts\activate
  
### Criar e Executar um Projeto Django
- Criar um novo projeto Django
- Para iniciar um novo projeto Django, execute o seguinte comando:
- python -m django startproject project .

### Instalar Django no ambiente virtual
- Após criar o projeto, é recomendado instalar o Django novamente no ambiente virtual. Use o comando abaixo:
- pip install django


### Executar o Servidor de Desenvolvimento
- Para executar o servidor de desenvolvimento do Django, utilize o comando:
- python manage.py runserver


### Instalar o pacote Pillow (opcional)
- O pacote Pillow serve para processamento de imagens, você pode instalá-lo usando o seguinte comando:
- pip install pillow
- Lembre-se de executar esses comandos em um terminal ou prompt de comando no diretório adequado.

## Notas
- Lembre-se de que essas são apenas as etapas básicas para configurar um ambiente Django. Dependendo dos requisitos específicos do seu projeto, você pode precisar fazer outras configurações.

- Para mais informações sobre como usar o Django, consulte a documentação oficial.

- Agora você está pronto para começar a desenvolver seu projeto Django!
