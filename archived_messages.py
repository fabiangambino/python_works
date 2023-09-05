messages = ["Hello!", "Welcome", "Goodbye"]
sent_messages = []

def send_messages(messages, sent_messages):
	while len(messages) != 0:
		current_message = messages.pop()
		print(current_message)
		sent_messages.append(current_message)

print(messages)

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)



