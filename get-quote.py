import random 
def main():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0])
  print("Ahora si")
  last = 13
  rnd = random.randint(0, last)
  last = len(quotes) -1
  print(quotes[rnd])
  print(quotes[13])

if __name__== "__main__":
  main()
