from pathlib import Path
import sys

root_path = sys.path[0]
# print(root_path)

tree = ''


def generate_tree(pathname, fill=''):
    global tree
    subFile = [subfile for subfile in pathname.iterdir()
               if subfile.is_file()]
    subDir = [subdir for subdir in pathname.iterdir()
              if subdir.is_dir()]

    for dirct in subDir[:-1]:
        tree += fill + '├─' + dirct.stem + '\n'
        generate_tree(dirct, fill+'│  ')

    if len(subDir) > 0:
        tree += fill + ('├─' if len(subFile) >
                        0 else '└─') + subDir[-1].stem + '\n'
        generate_tree(subDir[-1], fill+('│  ' if len(subFile) else '   '))

    for file in subFile[:-1]:
        tree += fill + '├─' + file.name + '\n'
    if len(subFile) > 0:
        tree += fill + '└─' + subFile[-1].name + '\n'


def outToFile():
    with open(sys.path[0] + '/DirectoryTree.txt', 'w') as file:
        try:
            file.write(tree)
            print('输出成功！')
        except IOError as err:
            print('输出出错！！')
            print(err)


if __name__ == '__main__':
    generate_tree(Path(root_path))
    print(tree)
    outToFile()
