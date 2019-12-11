
import subprocess
import sys
import time

"scanimage -L" #show available scaner
cmd = "scanimage\
    --resolution 360\
    --mode Color\
    --source TPU8x10\
    --format=tiff".split()

def scan(interval, cycles):
    for i in range(cycles):
        print("{}回目".format(i+1))
        with open("{}.tiff".format(i+1), "w") as f:
            subprocess.check_call(cmd, stdout=f)
        time.sleep(interval*60)
    print("end")

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
        scan(interval,cycles)
    elif yn == "n":
        print("終了します")
    else:
        print("不正な入力です")
        sys.exit()