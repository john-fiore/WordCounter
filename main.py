from colorama import Fore as col
import os, sys
import subprocess as sp

academic_mode = True

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def get_count(sentence: str) -> int:
    return len(sentence.split())

def main():
    clear()
    print(f"Welcome to the {col.BLUE}Word Counter{col.RESET}.")
    print("=================================================")
    print("Please select a mode:")
    print()
    print("1) Regular Mode")
    print("   └ Counts the words, then prints it.")
    print("2) Academic Mode")
    print("   └ Asks user for a word count requirement, counts")
    print("     the words, determines whether it reaches the")
    print("     goal, and prints it.")
    print("=================================================")
    m_choice = input("> ")
    
    if m_choice == "1":
        clear()
        sentence = input("Enter your sentence: ")
        count = get_count(sentence)
        clear()
        print(f"Your sentence has {col.GREEN}{count}{col.RESET} words.")
        print()
        input(f"Press {col.YELLOW}[ENTER]{col.RESET} to continue.")
        main()
    elif m_choice == "2":
        clear()
        word_goal = int(input("Enter the required word count: "))
        sentence = input("Enter your sentence: ")
        count = get_count(sentence)
        clear()
        if count < word_goal:
            words_left = word_goal - count
            print(f"Your sentence has {col.RED}{count}{col.RESET} words.")
            print(f"You still need {col.YELLOW}{words_left}{col.RESET} more words.")
        else:
            print(f"Your sentence has {col.GREEN}{count}{col.RESET} words.")
        print()
        input(f"Press {col.YELLOW}[ENTER]{col.RESET} to continue.")
        main()
    else:
        clear()
        print(f"{col.RED}ERROR:{col.RESET} Invalid choice.")
        input()
        main()

if __name__ == "__main__":
    sp.run("title Word Counter", shell=True)
    main()