name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)
emails = dict()

for line in handle:
    words = line.split()
    if not line.startswith('From') or len(words) < 3:
        continue
    email = words[1]
    emails[email] = emails.get(email, 0) + 1
    
max = 0
max_email = None
for email, count in emails.items():
    if count > max:
        max = count
        max_email = email

print(max_email, max)
    