To run, create a `names.csv` with each line in the form `name, email address,
family, previous match`. The family field is used to stop members from one
family getting each other, if everyone has the same word in family they can all
get each other.

A file titled `secret.ini` is also needed formatted as such:
```ini
[secret]
address =
passwd = 
header = 
smtp =
```
with the email address and password the emails will be sent from, the header of
the emails and the SMTP address for the email.
