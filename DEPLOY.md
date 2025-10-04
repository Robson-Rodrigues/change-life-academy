# 🚀 Guia de Deploy - Change Life Academy

## Opções de Hospedagem Gratuita

### 1. Railway (RECOMENDADO) ⭐

**Vantagens:**
- ✅ Deploy automático via GitHub
- ✅ Domínio personalizado gratuito
- ✅ SSL automático
- ✅ Banco de dados gratuito
- ✅ Sem limitações de tempo

**Como fazer o deploy:**

1. **Crie uma conta no Railway:**
   - Acesse: https://railway.app
   - Faça login com GitHub

2. **Conecte seu repositório:**
   - Clique em "New Project"
   - Selecione "Deploy from GitHub repo"
   - Escolha seu repositório

3. **Configure as variáveis (se necessário):**
   - Railway detectará automaticamente que é uma aplicação Python
   - O deploy será feito automaticamente

4. **Acesse sua aplicação:**
   - Railway fornecerá uma URL como: `https://seuapp.railway.app`

---

### 2. Render

**Vantagens:**
- ✅ Deploy automático
- ✅ SSL gratuito
- ✅ Domínio personalizado

**Como fazer o deploy:**

1. **Crie uma conta no Render:**
   - Acesse: https://render.com
   - Faça login com GitHub

2. **Crie um novo Web Service:**
   - Conecte seu repositório GitHub
   - Selecione "Web Service"
   - Configure:
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `python app.py`

3. **Deploy:**
   - Render fará o deploy automaticamente
   - Sua URL será: `https://seuapp.onrender.com`

---

### 3. Heroku

**Vantagens:**
- ✅ Muito popular
- ✅ Fácil de usar

**Limitações:**
- ⚠️ Aplicação "dorme" após 30 min de inatividade
- ⚠️ Limite de 550 horas/mês no plano gratuito

**Como fazer o deploy:**

1. **Instale o Heroku CLI:**
   ```bash
   # Windows
   winget install Heroku.HerokuCLI
   
   # Ou baixe em: https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Faça login no Heroku:**
   ```bash
   heroku login
   ```

3. **Crie uma aplicação:**
   ```bash
   heroku create sua-academia-app
   ```

4. **Faça o deploy:**
   ```bash
   git add .
   git commit -m "Deploy para Heroku"
   git push heroku main
   ```

5. **Abra sua aplicação:**
   ```bash
   heroku open
   ```

---

### 4. PythonAnywhere

**Vantagens:**
- ✅ Específico para Python
- ✅ Interface web para gerenciar arquivos

**Como fazer o deploy:**

1. **Crie uma conta:** https://www.pythonanywhere.com
2. **Faça upload dos arquivos** via interface web
3. **Configure o WSGI file** para apontar para sua aplicação
4. **Acesse sua aplicação** via URL fornecida

---

## 📋 Checklist Antes do Deploy

- [x] ✅ Arquivo `Procfile` criado
- [x] ✅ `requirements.txt` atualizado com gunicorn
- [x] ✅ `runtime.txt` especificando versão Python
- [x] ✅ `app.py` configurado para produção
- [x] ✅ Debug desabilitado
- [x] ✅ Porta dinâmica configurada

## 🔧 Configurações Importantes

### Variáveis de Ambiente (se necessário)
Se precisar configurar variáveis de ambiente:

```bash
# No Railway/Render
SECRET_KEY=sua_chave_secreta_aqui
```

### Banco de Dados
Para produção, considere usar um banco de dados real:
- **Railway:** PostgreSQL gratuito
- **Render:** PostgreSQL gratuito
- **Heroku:** PostgreSQL gratuito (com limitações)

## 🚨 Solução de Problemas

### Erro de Porta
Se aparecer erro de porta, verifique se o `app.py` está configurado corretamente:
```python
port = int(os.environ.get('PORT', 5000))
app.run(debug=False, host='0.0.0.0', port=port)
```

### Erro de Dependências
Verifique se todas as dependências estão no `requirements.txt`:
```
Flask==2.3.3
Werkzeug==2.3.7
gunicorn==21.2.0
```

### Erro de Secret Key
Se aparecer erro de secret key, adicione uma variável de ambiente:
```python
app.secret_key = os.environ.get('SECRET_KEY', 'change_life_academy_secret_key_2024')
```

## 🎯 Recomendação Final

**Use o Railway** - É a opção mais simples e confiável para aplicações Flask gratuitas!

1. Conecte seu GitHub
2. Selecione o repositório
3. Deploy automático
4. Pronto! 🎉

---

**Sua aplicação estará online em poucos minutos!** 🚀
