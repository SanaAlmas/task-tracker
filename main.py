import argparse
from app.structure import Structure

def main():
    s = Structure()
    parser = argparse.ArgumentParser(
                    prog='TaskTracker',
                    description='Manages Tasks',
                    epilog='Thanks for using the application')
    parser.add_argument('-a','--add', nargs='*', type= str)
    parser.add_argument('-u', '--update', nargs=2, metavar=('TASK', 'STATUS'),
                        help="Update an existing task status to INPROGRESS|DONE")
    parser.add_argument('-d', '--delete', nargs=1, metavar=('TASK'),
                        help="Delete an existing task")
    parser.add_argument(
        '-s', '--show',
        nargs='?',
        const="all",
        choices=["all", "todo", "inprogress", "done"],
        help="Display tasks. Optional: all|todo|inprogress|done"
    )
    args = parser.parse_args()

    if args.add:
        s.add(data = args.add[0])
        print('Task added')

    if args.update:
        s.update(data=args.update[0], new_status=args.update[1])
        print('Status updated')

    if args.delete:
        s.delete(data=args.delete[0])
        print('Task Deleted')

    if args.show:
        s.show(status = args.show)

if __name__ == "__main__":
    main()

