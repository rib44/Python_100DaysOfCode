try:
    file = open("random.txt", "a")
except FileNotFoundError as msg:
    print(f"{msg}")
else:
    print("Everything is working correctly")
finally:
    print("Bye")
    file.close()
