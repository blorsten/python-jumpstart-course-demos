import os
import program

journal = []


def load():
    pass


def save():
    filename = get_full_path_name()
    print('.... saving to {}'.format(filename))

    with open(filename, 'w+') as fout:
        for e in journal:
            fout.write(e + '\n')


def get_full_path_name():
    filename = os.path.abspath(os.path.join('./apps/04_journal/you_try/journals', 'default.jrl'))
    return filename


def add_entry(entry):
    journal.append(entry)


if __name__ == "__main__":
    program.main()
