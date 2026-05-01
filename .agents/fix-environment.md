---
description: Workflow para instalar pacotes faltantes ou resolver erros de compilação/importação ("Cannot find module").
---

# Workflow: Resolução de Ambiente e Dependências (/fix-env)

**Descrição:** Workflow para instalar pacotes faltantes ou resolver erros de compilação/importação ("Cannot find module").
**Invocação:** O utilizador aciona via `/fix-env [nome_do_pacote] [target: frontend|backend]`.

## Passos de Execução (Linear):

1. **Instalação Confinada (Skills):**
   - *Ação:* Você está ESTRITAMENTE PROIBIDO de dizer ao utilizador "rode npm install no seu terminal".
   - *Ação:* Invoque a skill `docker-executor` passando o target (frontend ou backend) e o comando de instalação apropriado (ex: `npm install [pacote]` ou `poetry add [pacote]`).

2. **Invalidação de Cache de Volume:**
   - *Ação:* Após a instalação ser bem-sucedida, você deve invocar novamente o `docker-executor` rodando o comando: `docker restart [nome_do_container_alvo]`.
   - *Justificativa:* Isso garante que os volumes do Docker sincronizem a nova pasta `node_modules` ou o novo ambiente virtual Python com o servidor local (Rule 04).

3. **Relatório:**
   - *Ação:* Informe ao utilizador que a dependência foi instalada dentro do container isolado e o serviço foi reiniciado.