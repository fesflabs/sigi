---
trigger: always_on
---

---
trigger: always_on
---
# Governança de Segredos e Variáveis de Ambiente do SIGI

Ao analisar solicitações de configuração de banco de dados, chaves de API, ou ao gerar/modificar arquivos de configuração, **sempre priorize** as seguintes leis de segurança:

1. **Isolamento de Credenciais:** Nunca faça hardcode de senhas, URIs de banco de dados ou tokens de acesso diretamente no código-fonte ou no `docker-compose.yml`.
2. **Uso do Padrão ENV:** Ao identificar a necessidade de uma variável sensível, determine que ela deve ser consumida do ambiente e provida via arquivo `.env`.
3. **Template Obrigatório:** Ao adicionar qualquer nova variável exigida pelo sistema, você deve registrar a chave no arquivo `.env.example` com um valor fictício (dummy) para manter o registro seguro.
4. **Proteção de Commit:** Nunca sobrescreva as regras do arquivo `.gitignore` que protegem arquivos de ambiente.