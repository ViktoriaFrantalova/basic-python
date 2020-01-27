## koment ucitela: nic kedze nic nemam

def main() -> None:
    with open('phrases.txt', mode='r', encoding='utf8') as f:
        text = f.read()
    text


if __name__ == '__main__':
    main()
