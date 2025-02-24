from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags

import re
import logging

from accounts.exceptions import UserAlreadyExistsError

# Configuração do logger
logger = logging.getLogger(__name__)


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            messages.error(request, "Todos os campos são obrigatórios.")
        else:
            try:
                user = User.objects.get(email=email)
                auth_user = authenticate(username=user.username, password=password)
                if auth_user is not None:
                    login(request, auth_user)
                    return redirect("menu")
                else:
                    messages.error(request, "Senha inválida.")
            except User.DoesNotExist:
                messages.error(request, "E-mail inexistente.")

    return render(request, "accounts/login.html")


def register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if not name.isalpha():
            messages.error(request, "O nome deve conter apenas letras, espaços também não são aceitos.")
        elif not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            messages.error(request, "E-mail inválido.")
        elif not re.search(r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
            messages.error(request, "A senha deve conter ao menos 8 caracteres, 1 caractere especial, 1 número e 1 letra maiúscula.")
        elif password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
        else:
            try:
                # Verificar se o e-mail ou nome de usuário já existe
                if User.objects.filter(username=name).exists():
                    raise UserAlreadyExistsError("Este Nome já está cadastrado.")
                if User.objects.filter(email=email).exists():
                    raise UserAlreadyExistsError("Este e-mail já está em uso.")

                # Criar o usuário
                user = User.objects.create_user(username=email, email=email, password=password, first_name=name)

                messages.success(request, "Registro realizado com sucesso!")

                # Registrar o usuário criado no log
                logger.debug(f"Usuário criado: {user.first_name} ({user.email}), username: {user.username}")

                # Enviar e-mail de confirmação
                subject = "Confirmação de Cadastro"
                message_html = render_to_string('accounts/email_confirmation.html', {'name': name, 'email': email})
                message_text = strip_tags(message_html)  # Para a versão em texto
                send_mail(subject, message_text, 'seuemail@gmail.com', [email], html_message=message_html)

                return redirect("login")

            except UserAlreadyExistsError as e:
                messages.error(request, str(e))

    return render(request, "accounts/register.html")


def menu_view(request):
    return render(request, "accounts/menu.html")
