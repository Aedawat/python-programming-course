import random

def test_random():
    #สร้างตัวแปร random_number สุ่มตัวเลขระหว่าง 1-10
    random_number = random.randint(1, 10)
    print("== Guess Number Between (1-10) ==")
    guess_number = input("What is yor guess number: ")#input รับค่าแค่ Str ต้องแปลงให้รับเป็นตัวเลขในบรรทัดต่อไป
    guess_number = int(guess_number)#เพิ่ม int เพื่อให้รับค่าตัวเลข
    
    if random_number == guess_number:
        print("Congratulation!")

    elif random_number < guess_number:
        print("Too high")

    elif random_number > guess_number:
        print("Too low")
    
test_random()