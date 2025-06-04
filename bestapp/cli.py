import argparse
from .todo import TodoList


def main():
    parser = argparse.ArgumentParser(description='Simple TODO application')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', help='Description of the task')

    subparsers.add_parser('list', help='List tasks')

    done_parser = subparsers.add_parser('done', help='Mark task as done')
    done_parser.add_argument('index', type=int, help='Index of the task (starting from 1)')

    remove_parser = subparsers.add_parser('remove', help='Remove a task')
    remove_parser.add_argument('index', type=int, help='Index of the task (starting from 1)')

    args = parser.parse_args()

    todo = TodoList()
    todo.load()

    if args.command == 'add':
        todo.add(args.description)
    elif args.command == 'list':
        for i, task in enumerate(todo.list_tasks(), 1):
            status = '✔' if task.done else ' '
            print(f'{i}. [{status}] {task.description}')
    elif args.command == 'done':
        todo.complete(args.index - 1)
    elif args.command == 'remove':
        todo.remove(args.index - 1)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
