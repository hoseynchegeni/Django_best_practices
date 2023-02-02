{% extends "mail_templated/base.tpl"%}
{%block subject%}

Account Activation

{%endblock%}

{%block html%}

<a href = "http://127.0.0.1:8000/accounts/api/v1/activation/confirm/{{token}}">Account Activation</a>

{%endblock%}