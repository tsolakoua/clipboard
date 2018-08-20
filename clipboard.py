import subprocess
import datetime
import sys

def get_clipboard():
    result = ""
    while True:
        access = subprocess.Popen(['pbpaste'], stdout = subprocess.PIPE)
        copied_data = access.stdout.read().decode("utf-8")
        if result != copied_data:
            result = copied_data
            write_to_file(result)

def write_to_file(result):
    f = open("clipboard_file","a")
    f.write(result + " at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    f.write('\n')

def main():
    get_clipboard()

if __name__ == "__main__":
    sys.exit(main())
