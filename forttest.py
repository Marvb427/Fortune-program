import subprocess

def get_fortune():
  fortune = subprocess.run(["fortune"], stdout=subprocess.PIPE)
  return fortune.stdout.decode("utf-8")

def main():
  while True:
    input("Press enter to see a fortune...")
    print(get_fortune())

if __name__ == "__main__":
  main()
