# Desafio Técnico Desenvolvedor Back-End Estagiário

## Django Login & Register

Este projeto é uma aplicação Django que implementa um sistema de autenticação com telas de Login, Registro e um Menu simples.

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **Django**
- **SQLite** (padrão, mas pode ser substituído por MySQL, PostgreSQL, etc.)

## 📌 Requisitos

Antes de iniciar, certifique-se de ter o seguinte instalado:

- Python 3.x
- Pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)

## 📥 Instalação e Configuração

### 1️⃣ Clonar o repositório

```sh
git clone https://github.com/seu-usuario/django-login-register.git
cd django-login-register
```

### 2️⃣ Criar e ativar um ambiente virtual (opcional, mas recomendado)

```sh
python -m venv venv  # Criar ambiente virtual
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3️⃣ Instalar dependências

```sh
pip install -r requirements.txt
```

### 4️⃣ Configurar o banco de dados

```sh
pytitncluhon manage.py migrate
```

```sh
python manage.py migrate
```

### 5️⃣ Criar um superusuário (opcional, para acessar o Django Admin)

```sh
python manage.py createsuperuser
```

Siga as instruções e defina um nome de usuário, e-mail e senha.

### 6️⃣ Executar o servidor

```sh
python manage.py runserver
```

Acesse no navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000). Este endereço foi configurado para redirecionar automaticamente para a tela de login.

## 🖥️ Como Testar a Aplicação

- **Acesso ao Sistema**: Acesse `http://127.0.0.1:8000` redirecione para a tela de login.
- **Tela de Login**: Acesse `http://127.0.0.1:8000/accounts/login/` e tente fazer login.
- **Tela de Registro**: Acesse `http://127.0.0.1:8000/accounts/register/` para criar uma conta.
- **Redirecionamento**: Após o login bem-sucedido, o usuário será direcionado para a tela `Menu`.

## 📧 Extra: Envio de E-mail

Caso queira habilitar o envio de e-mails de boas-vindas, configure as credenciais SMTP no arquivo `settings.py`.

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.seuprovedor.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu-email@example.com'
EMAIL_HOST_PASSWORD = 'sua-senha'
```

Se as credenciais de e-mail **não** estiverem configuradas, os e-mails serão impressos no log da aplicação ao invés de serem enviados. Para isso, utilize a seguinte configuração:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Isso fará com que todos os e-mails sejam exibidos no terminal ao invés de serem enviados.


Se as credenciais de e-mail não estiverem configuradas, os e-mails serão impressos no log da aplicação ao invés de serem enviados.


## 📝 Configuração de Log da Aplicação

Para facilitar a depuração e análise de erros, o log da aplicação foi habilitado. Adicione a seguinte configuração ao seu `settings.py`:

```python
# Logger Configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'django_debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

Os logs serão salvos no arquivo `django_debug.log`, permitindo uma melhor análise dos eventos da aplicação.

## 🛠️ Configuração do Runner no IntelliJ

Se você estiver utilizando o IntelliJ IDEA para rodar o projeto Django, siga os passos abaixo:

1. **Abrir as Configurações de Execução:**
   - No IntelliJ IDEA, vá até `Run` > `Edit Configurations`.

2. **Criar uma nova configuração:**
   - Clique no botão `+` e selecione `Python`.

3. **Configurar o Django Runserver:**
   - No campo `Script path`, adicione o caminho para `manage.py` do seu projeto.
   - No campo `Parameters`, adicione `runserver`.
   - No campo `Environment variables`, adicione:
     ```
     DJANGO_SETTINGS_MODULE=config.settings
     ```
   - Se estiver utilizando um ambiente virtual, configure o caminho do `Python interpreter` para apontar para o `venv` do projeto.

4. **Salvar e Executar:**
   - Clique em `Apply` e `OK`.
   - Agora, clique em `Run` para iniciar o servidor Django diretamente pelo IntelliJ IDEA.

## 📜 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar! 🚀

