import os
import subprocess

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def executar(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"{RED}Erro ao executar comando.{RESET}")

def limpar():
    os.system("clear")

def cabecalho():
    limpar()
    print(f"""{GREEN}
=================================================
                GIT PROJECT MANAGER
                 Developed by Pablo
=================================================
{RESET}
1 - Git Status
2 - Add + Commit
3 - Push
4 - Pull
5 - Add + Commit + Push
6 - Ver Branch
7 - Ver Últimos Commits
8 - Criar Branch
9 - Trocar Branch
10 - Deletar Branch
11 - Ver Remotos
12 - Git Log Completo
13 - Git Diff
14 - Stash Save
15 - Stash List
16 - Stash Pop
17 - Clonar Repositório
18 - Inicializar Git
19 - Ver Tags
20 - Criar Tag
21 - Buscar Atualizações
22 - Limpar Arquivos Não Rastreados
23 - Corrigir erro de push
24 - Forçar push
0 - Sair
""")

while True:
    cabecalho()

    opcao = input(f"{CYAN}Opção: {RESET}")

    if opcao == "1":
        executar("git status")

    elif opcao == "2":
        msg = input("Mensagem commit: ")
        executar("git add .")
        executar(f'git commit -m "{msg}"')

    elif opcao == "3":
        executar("git push")

    elif opcao == "4":
        executar("git pull")

    elif opcao == "5":
        msg = input("Mensagem commit: ")
        executar("git add .")
        executar(f'git commit -m "{msg}"')
        executar("git push")

    elif opcao == "6":
        executar("git branch")

    elif opcao == "7":
        executar("git log --oneline -10")

    elif opcao == "8":
        nome = input("Nome da branch: ")
        executar(f"git checkout -b {nome}")

    elif opcao == "9":
        nome = input("Branch destino: ")
        executar(f"git checkout {nome}")

    elif opcao == "10":
        nome = input("Branch para deletar: ")
        executar(f"git branch -d {nome}")

    elif opcao == "11":
        executar("git remote -v")

    elif opcao == "12":
        executar("git log --graph --oneline --all")

    elif opcao == "13":
        executar("git diff")

    elif opcao == "14":
        nome = input("Nome do stash: ")
        executar(f'git stash save "{nome}"')

    elif opcao == "15":
        executar("git stash list")

    elif opcao == "16":
        executar("git stash pop")

    elif opcao == "17":
        repo = input("URL do repositório: ")
        executar(f"git clone {repo}")

    elif opcao == "18":
        executar("git init")

    elif opcao == "19":
        executar("git tag")

    elif opcao == "20":
        tag = input("Nome da tag: ")
        executar(f"git tag {tag}")

    elif opcao == "21":
        executar("git fetch")

    elif opcao == "22":
        executar("git clean -fd")

    elif opcao == "23":
        print(f"{YELLOW}1. Buscando atualizações...{RESET}")
        executar("git fetch origin")

        print(f"{YELLOW}2. Aplicando rebase...{RESET}")
        executar("git pull origin main --rebase")

        print(f"{YELLOW}3. Enviando alterações...{RESET}")
        executar("git push origin main")

    elif opcao == "24":
        confirmacao = input(f"{RED}Tem certeza que deseja forçar o push? (s/n): {RESET}")
        
        if confirmacao.lower() == "s":
            executar("git push --force")

    elif opcao == "0":
        print(f"{YELLOW}Saindo...{RESET}")
        break

    else:
        print(f"{RED}Opção inválida.{RESET}")

    input(f"\n{GREEN}Pressione ENTER para continuar...{RESET}")
