started = False
while True:
    command = input(">").upper()
    if command == "HELP":
        print("start - to start the car.")
        print("stop - to stop the car.")
        print("quit - to exit.")
    elif command == "START":
        if started:
            print("Car already started.")
        else:
            started = True
            print("Car started. Ready to go.")
    elif command == "STOP":
        if not started:
            print("Car already stopped.")
        else:
            print("Car stopped.")
    elif command == "QUIT":
        break
    else:
        print("Sorry.I don't understand that.")
