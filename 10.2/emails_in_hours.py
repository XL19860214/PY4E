name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

emailsInHours = dict()

for line in handle:
    words = line.split()
    if not line.startswith('From') or len(words) < 3:
        continue
    time = words[5]
    hour = time.split(':')[0]
    emailsInHours[hour] = emailsInHours.get(hour, 0) + 1

for hour in sorted(emailsInHours.keys()):
    print(hour, emailsInHours[hour])
