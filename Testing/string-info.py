message = input("Enter a IP : ")

print("First number: ", message[0])
print("Last number: ", message[-1])
print("Middle number: ", message[int(len(message) / 2)])
print("Even characters: " ,message[0::2])
print("Odd characters: " ,message[0::1])
print("Backwords IP: ",message[::-1])