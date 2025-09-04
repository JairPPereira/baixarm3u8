import os
import psutil  # precisa instalar com: pip install psutil

def unlock_git_repo(repo_path="."):
    lock_file = os.path.join(repo_path, ".git", "index.lock")

    # Verifica se existe algum processo Git ativo
    git_running = any("git" in (p.name() or "").lower() for p in psutil.process_iter(attrs=["name"]))

    if git_running:
        print("⚠️ Existe um processo Git rodando. Espere terminar antes de remover o lock.")
        return

    # Verifica e remove o lock file
    if os.path.exists(lock_file):
        os.remove(lock_file)
        print("✅ Lock file removido com sucesso!")
    else:
        print("ℹ️ Nenhum lock file encontrado.")

if __name__ == "__main__":
    unlock_git_repo(".")
