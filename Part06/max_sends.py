from collections import defaultdict


def best_sender(msgs, senders):
    snds = defaultdict(int)
    for msg, sender in zip(msgs, senders):
        snds[sender] += len(msg.split(' '))
    return sorted(sorted(snds.items(), reverse=True), key=lambda item: -item[1])[0][0]


# Tests
messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']
print(best_sender(messages, senders))

messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']
print(best_sender(messages, senders))

messages = ['Hello userTwooo', 'Hi userThree', 'Wonderful day Alice', 'Nice day userThree']
senders = ['Alice', 'userTwo', 'userThree', 'Alice']
print(best_sender(messages, senders))
