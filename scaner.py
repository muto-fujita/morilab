import subprocess
import sys
import time

"scanimage -L" #show scaner
a = "scanimage --device {} --format=tiff > {}.tiff".format("1", "1")

def cmd(cmd):
    proc = subprocess.run(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
        )

    return proc.stdout.decode("utf8")


def test(interval, cycles):
    command = "scanimage -L" 

    for i in range(cycles):
        print("{}回目".format(i+1))
        # command = "scnaimage --sourse a {}.tiff " .format())
        r = cmd(["pwd"])
        print(r)
        time.sleep(interval*60)


if __name__ == '__main__':
    print("スキャン間隔を入力してください")
    interval = input('minutes : ')
    if not interval.isdecimal():
        print("不正な入力です")
        sys.exit()
    interval = int(interval)

    print("スキャン回数を入力してください")
    cycles = input('cycles : ')
    if not cycles.isdecimal():
        print("不正な入力です")
        sys.exit()
    cycles = int(cycles)

    print("{}分間隔で{}回スキャンを行います".format(interval, cycles))
    yn = input("y/n : ")
    if yn == "y":
        test(interval,cycles)
    elif yn == "n":
        print("終了します")
    else:
        print("不正な入力です")
        sys.exit()

    
