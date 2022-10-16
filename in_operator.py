import random

# Project--101 
# randomize 
# while
# inputprint formating 
# comparison operators
# break and continue

#Using While first because we want it constanly running until its find True input
while True:
    welcome = "Halo selamat datang di Python Project-101, kita akan bermain batu gunting kertas"
    print(welcome)
    my_answer  = input("Choose wisely(ketik pilihan mu)")
    keluar = "Kalo mau keluar ketik (quit) ya"
    computer_answer = ["batu", "gunting", "kertas"]
    menang = ["kertas" and "batu", "batu" and "gunting", "kertas" and "batu"]
    my_answer = my_answer.lower()
    keluar = keluar.lower()

    if my_answer == "quit":
        break
    
   
    if my_answer not in computer_answer:
        print("Pilih salah satu ya ! Batu, Kertas, or Gunting")
        continue

    computer_answer = random.choice(["batu", "gunting", "kertas"])
    print(f"Komputer milih: {computer_answer}")

    # !=(is not)
    # if my_answer != "batu" and my_answer != "kertas" and my_answer != "gunting":
   
    if my_answer == computer_answer:
        print("Kamu seri, coba lagi")
        continue
# PR
    elif my_answer ==menang:
        print("Kamu Menang!!")
        break

    else:
        print("Kasian deh kalah, coba lagi!")
        continue

print(keluar)
    

        

    # elif my_answer == "kertas" and computer_answer == "batu":
    #     print("Anda Menang!!")
    #     break
    # elif my_answer == "batu" and computer_answer == "gunting":
    #     print("Anda Menang!!")
    #     break
    # elif my_answer == "gunting" and computer_answer == "kertas":
    #     print("Anda Menang!!")
    #     break
        
