# with open('data_anggaran.csv', 'r') as anggaran:
#     anggaran = anggaran.readlines()

# for data in anggaran:
#     if "realisasi" in data:
#         print(anggaran.rstrip())
## gagal diatas nyoba nyoba, 
##kalob code

with open("emails.txt")  as emails:
    emails = emails.readlines()

for email in emails:
    if "gmail" in email:
        print(email.rstrip())
        ....