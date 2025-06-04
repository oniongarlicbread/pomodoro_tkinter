# list of messages to display in the text gui
import random

# shown in sequence upon startup, then after each session
def tooltip(number):
    messages = [
        (
                "This is a pomodoro timer. To use it, click the tomato."
        +"\n" + "There are 3 pomodoro in total, with each one lasting 25 minutes."
        +"\n" + "Once started, they cannot be paused, so make sure to eliminate all current and future distractions before starting the timer."
        ),
        (
            "Time to take 5-10 minutes of rest. Rest your eyes on faraway blue/green objects."
            + "\n" + "It's called a short rest, but you must use it to review your current pomodoro and prepare for your next pomodoro."
            + "\n" + "You must either record and postpone all other activities, or abandon the current pomodoro."
    )]
    return messages[number-1] # Return the nth tooltip

    # list comprehension is so confusing  >:C

# only shown while timer is counting
def flavortext():
    messages = [
        ("it's time to lock in", 0.5),
        ("Jesse, we need to cook", 0.2),
        ("potatotomato "*12, 0.1),
        ("Let's get dat bread!", 0.05),
    ]
    return random.choices(
        population=[msg for msg, weight in messages],
        weights=[weight for msg, weight in messages],
        k=1
    )[0]