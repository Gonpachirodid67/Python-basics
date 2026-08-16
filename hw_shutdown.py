def shutdown():
    answer = input("Do you want to shut down? ").lower()

    if answer == "yes" or "yeah" or "sure" or "yep" or "ok" or "postive" or "agreed":
        print("Shutting down")
    elif answer == "no" or "nah" or "nope" or "negative" or "declined":
        print("Abort shut down")
    else:
        print("Sorry")

shutdown()