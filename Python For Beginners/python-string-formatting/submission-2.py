def say_goodbye(name: str, hour: int) -> str:
    #msg = f"Goodbye, {name}. See you again at {hour} o'clock."
    #msg = "Goodbye, {}. See you again at {} o'clock.".format(name, hour)
    msg = "Goodbye, {1}. See you again at {0} o'clock.".format(hour, name)
    return msg


# do not modify below this line
print(say_goodbye("Bob", 12))
print(say_goodbye("Jane", 4))
print(say_goodbye("NeetCode", 9))
