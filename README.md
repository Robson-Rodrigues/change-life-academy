# Change Life Academy - Sistema de Gestão de Academia

Sistema web completo para gestão de academia desenvolvido com Python Flask, HTML, CSS e Bootstrap.

## 🏋️ Características

- **Sistema de Login Seguro**: Autenticação com usuários pré-cadastrados
- **Dashboard Moderno**: Interface intuitiva com estatísticas em tempo real
- **Design Responsivo**: Funciona perfeitamente em desktop e mobile
- **Tema de Academia**: Visual moderno e profissional
- **Bootstrap 5**: Framework CSS para interface responsiva

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone ou baixe o projeto**
2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação:**
   ```bash
   python app.py
   ```

4. **Acesse no navegador:**
   ```
   http://localhost:5000
   ```

## 👥 Usuários de Teste

O sistema vem com usuários pré-cadastrados para teste:

| Usuário | Senha | Nome | Função |
|---------|-------|------|--------|
| admin | admin123 | Administrador | Admin |
| instrutor1 | instrutor123 | Carlos Silva | Instrutor |
| instrutor2 | ana123 | Ana Santos | Instrutor |
| aluno1 | joao123 | João Oliveira | Aluno |
| aluno2 | maria123 | Maria Costa | Aluno |
| aluno3 | pedro123 | Pedro Lima | Aluno |
| recepcao | recepcao123 | Sofia Ferreira | Recepção |

## 📁 Estrutura do Projeto

```
change-life-academy/
├── app.py                 # Aplicação Flask principal
├── users.json            # Base de dados de usuários
├── requirements.txt      # Dependências Python
├── README.md            # Este arquivo
├── templates/           # Templates HTML
│   ├── base.html        # Template base
│   ├── login.html       # Página de login
│   └── dashboard.html   # Dashboard principal
└── static/             # Arquivos estáticos
    └── css/
        └── style.css    # Estilos personalizados
```

## 🎨 Funcionalidades

### Página de Login
- Interface moderna com tema de academia
- Validação de usuário e senha
- Mensagens de erro/sucesso
- Design responsivo

### Dashboard
- **Visão Geral**: Estatísticas da academia
- **Navegação Lateral**: Menu com diferentes seções
- **Cards de Estatísticas**: Membros ativos, aulas, instrutores
- **Atividade Recente**: Timeline de eventos
- **Próximas Aulas**: Agenda do dia

### Sistema de Autenticação
- Sessões seguras
- Redirecionamento automático
- Logout seguro
- Proteção de rotas

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Ícones**: Bootstrap Icons
- **Dados**: JSON (usuários)
- **Sessões**: Flask Sessions

## 🎯 Próximas Funcionalidades

- [ ] Cadastro de novos usuários
- [ ] Gestão de membros
- [ ] Sistema de aulas
- [ ] Relatórios avançados
- [ ] Integração com banco de dados
- [ ] Sistema de pagamentos

## 📱 Responsividade

O sistema é totalmente responsivo e funciona em:
- 💻 Desktop
- 📱 Tablet
- 📱 Smartphone

## 🔒 Segurança

- Sessões seguras com chave secreta
- Validação de entrada
- Proteção contra acesso não autorizado
- Logout automático

## 📞 Suporte

Para dúvidas ou sugestões, entre em contato através do sistema de issues do projeto.

---

**Change Life Academy** - Transforme sua vida através do fitness! 💪
