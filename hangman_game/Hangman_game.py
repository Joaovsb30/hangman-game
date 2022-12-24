import random

# Lista de palavras que o jogo pode usar
words = ["casa", "arvore", "computador", "elefante"]

# Escolhe uma palavra aleatória da lista
word = random.choice(words)

# Inicializa a lista de letras corretas com hífens
correct_letters = ["*" for _ in word]

# Inicializa o número de tentativas restantes
attempts_remaining = 6

while True:
    # Mostra o estado atual do jogo
    print("Palavra: ", " ".join(correct_letters))
    print("Tentativas restantes: ", attempts_remaining)

    # Lê a entrada do jogador
    guess = input("Adivinhe uma letra: ")

    # Verifica se a letra está na palavra
    if guess in word:
        # Atualiza a lista de letras corretas
        for i in range(len(word)):
            if word[i] == guess:
                correct_letters[i] = guess

        # Verifica se o jogador acertou a palavra
        if "*" not in correct_letters:
            print("Parabéns, você acertou a palavra!")
            break
    else:
        # Decrementa o número de tentativas restantes
        attempts_remaining -= 1

        # Verifica se o jogador perdeu
        if attempts_remaining == 0:
            print("Você perdeu!")
            break
