import re

s = '''riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com
riya ariya@gmail.com
julia bjulia@julia.me
julia csjulia@gmail.com
julia djulia@gmail.com
samantha esamantha@gmail.com
tanya ftanya@gmail.com
riya riya@live.com
julia julia@live.com
julia sjulia@live.com
julia julia@live.com
samantha samantha@live.com
tanya tanya@live.com
riya ariya@live.com
julia bjulia@live.com
julia csjulia@live.com
julia djulia@live.com
samantha esamantha@live.com
tanya ftanya@live.com
riya gmail@riya.com
priya priya@gmail.com
preeti preeti@gmail.com
alice alice@alicegmail.com
alice alice@gmail.com
alice gmail.alice@gmail.com'''
name_list = []
for i in s.split('\n'):
    first_name_email_id = i.split()
    first_name = first_name_email_id[0]
    email_id = first_name_email_id[1]

    first_name_re = re.match(r'^[a-z]{1,20}$', first_name)
    email_id_re = re.match(r'^([a-z]|\.|@){1,50}@gmail.com$', email_id)

    if first_name_email_id and email_id_re:
        name_list.append(first_name)

print('\n'.join(sorted(name_list)))