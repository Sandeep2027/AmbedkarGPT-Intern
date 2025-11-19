from colorama import Fore, Style

def print_header():
    print(Fore.CYAN + "\n=== AmbedkarGPT — Offline RAG System ===" + Style.RESET_ALL)
    print(Fore.YELLOW + "Type your question, or:\n/exit to quit | /clear to clear screen | /reload to rebuild vectorstore\n" + Style.RESET_ALL)


def pretty_answer(answer):
    print(Fore.GREEN + "\nAnswer:" + Style.RESET_ALL)
    print(Fore.WHITE + answer + Style.RESET_ALL)
