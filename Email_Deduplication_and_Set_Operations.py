#LIST OF EMAIL ADDRESSES (SOME DUPLICATES)
email_addresses=[
    "user1@example.com","user2@example.com","user3@example.com"
    "user1@example.com","user4@example.com","user2@example.com"
]

#use a set to rempve duplicates
unique_emails=set(email_addresses)

#convert the set back to a sorted list if needed
unique_emails_list=sorted(unique_emails)

print(unique_emails_list)

#output the unique email addresses 
print("unique email addresses:")
for email in unique_emails_list:
    print(email)
    
#noW add more three emails(some reperated from set1) in another set 
#and print only emails which are present



#set difference
additional_emails={"sang12@gmail.com"}