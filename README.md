<h1 align="center"> 
Sistema de Gestão para o Núcleo de Apoio à Inclusão - SGNAI</h1>

# 📚 Sobre
O Sistema de Gestão para o Núcleo de Apoio à Inclusão (SGNAI) foi desenvolvido para otimizar o gerenciamento de atividades, monitorias, tutorias e acompanhamento de alunos PcD no âmbito do Núcleo de Apoio à Inclusão (NAI) da Universidade Federal do Acre (UFAC).

### 📑Resumo
#### 🌍 Histórico e Motivação:

Um sistema de registro para gerenciar as atividades de monitorias, tutorias e assistência aos alunos do NAI já pré-desenvolvido existia. No entanto, durante um estágio supervisionado, identificou-se a necessidade de aprimorar suas funcionalidades e documentação para viabilizar sua efetiva implantação na rotina do NAI.
<br>

#### 📈 Aprimoramentos Realizados:

O sistema passou por um processo abrangente de refinamento, abrangendo:

- Refatoração de código: O código foi reestruturado para aumentar sua legibilidade, modularidade e manutenabilidade.
- Testes de software: Testes rigorosos foram realizados para garantir a confiabilidade e robustez do sistema.
- Interfaces intuitivas: As interfaces foram redesenhadas para proporcionar uma experiência de usuário mais amigável e intuitiva.
- Recursos de acessibilidade: A acessibilidade foi priorizada, com a implementação de recursos que garantem a igualdade de acesso para todos os usuários.
<br>
<br>
A imagem abaixo ilustra a página de login atual após alterações na interface.

<div align='center'>
    <img src='https://github.com/anacarolinens/weather-vue/assets/85416744/c187fb36-eaa2-4800-b1c3-9cd1b2814df1' width='50%' style="border-radius: 25px;">
</div>
<p align='center' style='font-size:10px'>Página de login</p>

## 🖥️🛠️ Tecnologias e Ferramentas utilizadas

Essas foram algumas das ferramentas fundamentais que impulsionaram o desenvolvimento do projeto:

<br>

<div align="center">
    <img alt="python" width=100 height="70"  src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" />
    <img alt="django" width=100 height="70"   src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain-wordmark.svg" />
    <img alt="GitHub" width=100 height="70"  src="https://raw.githubusercontent.com/devicons/devicon/master/icons/github/github-original.svg"/>
    <img  alt="figma" width=100 height="70"  src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/figma/figma-original.svg" />
    <img alt="bootstrap" width=100 height="70"  src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bootstrap/bootstrap-original-wordmark.svg" />
    <img alt="vscode" width=100 height="70" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original-wordmark.svg" />     
    <img alt="mysql" width=100 height="70"   src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original-wordmark.svg" />
             
</div>
<br>


## 🚀  Funcionalidades, recursos e melhorias adicionadas
Essas são algumas das funcionalidades, recursos e melhorias que foram implementadas no sistema:

- Prototipação: Desenvolvimento de protótipos para visualização e validação das funcionalidades do sistema antes da implementação completa.

- Acessibilidade: Implementação do VLibras além de para oferecer suporte à acessibilidade, permitindo que usuários surdos ou com deficiência auditiva tenham acesso ao conteúdo em língua de sinais. Além disso foram utilizadas ferramentas como axe devtools e o weve evaluation tool que ajuda os autores a tornar seu conteúdo da Web mais acessível para pessoas com deficiência visual.

- Teste de Software e Validação: Realização de testes de software abrangentes para garantir o funcionamento correto do sistema, incluindo testes de unidade, integração e aceitação.

- Refatoração: Melhorias no código-fonte existente para aumentar a legibilidade, escalabilidade e manutenibilidade do sistema, garantindo uma base sólida para futuras atualizações e desenvolvimentos.

# ⚙ Configuração do Ambiente de Desenvolvimento
Siga as etapas abaixo para configurar corretamente o ambiente e conseguir rodar o sistema localmente em sua máquina.
### ✔️ Passo 1
####  Clonar o repositório
```bash
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```
### ✔️ Passo 2
#### Instalar Python
Certifique-se de ter o Python instalado em seu sistema antes de prosseguir. Você pode baixar o Python <a href='https://www.python.org/downloads/'>clique aqui</a>.

### ✔️ Passo 3
#### IDE - Ambiente de Desenvolvimento Integrado
Escolha uma IDE que melhor se adapte às suas preferências, como o Visual Studio Code, PyCharm, ou qualquer outra de sua escolha.

### ✔️ Passo 4
#### Instalar Django
- Execute o seguinte comando no para instalar o Django usando o pip:
```bash
pip install django
```

## ⚙ Configuração do Ambiente  Django
### Criar um ambiente virtual
- Execute o seguinte comando para criar um novo ambiente virtual:
```bash
python -m venv myenv
```

### Ativar o ambiente virtual
- Para ativar o ambiente virtual, use o seguinte comando:
```bash
myenv\Scripts\activate
```

### Instalar Django no ambiente virtual
- Após criar o projeto, é recomendado instalar o Django novamente no ambiente virtual. Use o comando abaixo:
```bash
pip install django
```

### Instalar as dependências:
- Com o ambiente virtual ativado, execute o seguinte comando para instalar todas as dependências do sistema:
```bash
pip install -r requirements.txt
```

## 🔌⚡ Conexão e Migração do Banco de Dados

#### Pré-requisitos:

- Ter um editor e gerenciador SQL de banco de  de sua preferência instalado e 
- Ter o script SQL estagio.sql localizado na raiz do projeto.
Ter um projeto Django configurado e funcionando.

#### ⭐⭐⭐ Etapas:

1. Abrindo o Script SQL:

    - Abra o cliente de banco de dados de sua preferência.
    - Conecte-se ao banco de dados do seu projeto Django.
    - No menu do cliente, localize a opção para abrir um script SQL.
    - Navegue até a pasta raiz do seu projeto e selecione o arquivo estagio.sql.
    - Abra o script e revise seu conteúdo para garantir que você esteja executando as instruções corretas.
2. Executando o Script SQL:

    - Clique no botão para executar o script SQL.
    - Aguarde a execução do script. O tempo de execução pode variar dependingo da quantidade de dados e da complexidade das instruções.
    - Verifique se o script foi executado com sucesso na tela de resultados do cliente de banco de dados.

3. Migrando no Django:

    - Retorne ao seu IDE (PyCharm, VS Code, etc.) onde seu projeto Django está aberto.
    - No terminal do IDE, navegue até a pasta do seu projeto Django.
    - Execute o seguinte comando para criar as migrações:
    ```bash
    python manage.py makemigrations
    ```
    - Verifique se a migração foi criada na pasta migrations do seu projeto.
    - Execute o seguinte comando para aplicar a migração ao banco de dados:
    ```bash
    python manage.py migrate
    ``` 
### 💻 Executar o Servidor de Desenvolvimento
- Para executar o servidor de desenvolvimento do Django, utilize o comando:
```bash
python manage.py runserver
```


## 👩‍💻💼 Time de Desenvolvimento

Time por trás do desenvolvimento:

<div align="center">
    <a href="https://github.com/anacarolinens">
        <div align="center" style="display: inline-block; margin: 10px;">
            <div>
                <img src="https://avatars.githubusercontent.com/u/85416744?v=4" width="100" height="100" style="border-radius: 50%;">
            </div>
            <p>Ana Caroline</p>
        </div>
    </a>
    <a href="https://github.com/Andisssu">
        <div align="center" style="display: inline-block; margin: 10px;">
            <div>
                <img src="https://avatars.githubusercontent.com/u/127001432?v=4" width="100" height="100" style="border-radius: 50%;">
            </div>
            <p>Anderson Dantas</p>
        </div>
    </a>
    <a href="https://github.com/ShayllaMaia">
        <div align="center" style="display: inline-block; margin: 10px;">
            <div>
                <img src="https://avatars.githubusercontent.com/u/112740621?v=4" width="100" height="100" style="border-radius: 50%;">
            </div>
            <p>Shailla Maia</p>
        </div>
    </a>
</div>



## 🗃 Recursos Adicionais
- Documentação do Django: https://docs.djangoproject.com/en/5.0/
- Tutoriais do Django: https://www.djangoproject.com/start/
- Fórum da comunidade Django: https://forum.djangoproject.com/
- Documentação do MySQL: https://dev.mysql.com/doc/

## 📌 Dicas e Observações
- Lembre-se de que essas são apenas as etapas básicas para configurar um ambiente Django e verificar o andamento desse projeto.
- É importante revisar o script SQL antes de executá-lo para garantir que você esteja importando os dados corretos para as tabelas corretas.
- Se você encontrar erros durante a execução do script SQL, revise o script e consulte a documentação do PostgreSQL para obter ajuda.
- Certifique-se de executar as migrações no Django após importar os dados para o banco de dados.