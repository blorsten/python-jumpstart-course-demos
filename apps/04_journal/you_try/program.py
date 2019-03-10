import journal


def main():
    journal.load()
    print_header()
    loop()
    journal.save()


def print_header():
    print('-----------------------------')
    print('Journal app')
    print('-----------------------------')


def list_journal():
    print('You have {} entries:'.format(len(journal.journal)))
    rev = reversed(journal.journal)
    for idx, entry in enumerate(rev):
        print('{}: {}'.format(idx + 1, entry))


def save_entry(entry):
    journal.add_entry(entry)
    print('your entry was added, count: {}'.format(len(journal.journal)))


def loop():
    cmd = None
    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_journal()

        elif cmd == 'a':
            print('What do you want to add?')
            value = input()
            save_entry(value)

        elif cmd != 'x':
            print('Command not understood')


if __name__ == "__main__":
    main()
