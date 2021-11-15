from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)


contacts = {}
for row in contacts_list:
  pattern = re.compile("([\w]+)[\W]+([\w]+)[\W]+([\w]*)")
  name = row[0] + " " + row[1] + " " + row[2]
  result = re.match(pattern, name)
  lastname = result.group(1)
  firstname = result.group(2)
  surname = result.group(3)

  organization = row[3]
  position = row[4]

  pattern = re.compile("[\D]*[7|8]{1}[\D]*([\d]{3})[\D]*([\d]{3})[\D]*([\d]{2})[\D]*([\d]{2})[\D]*([\d]*)[\D]*")
  result = re.match(pattern, row[5])
  phone = ''
  if result is not None:
    phone = "+7(" + result.group(1) + ")" + result.group(2) + "-" + result.group(3) + "-" + result.group(4)
    dob = result.group(5)
    if len(dob) > 0:
      phone += " доб." + dob

  email = row[6]

  name = lastname + " " + firstname

  if name not in contacts:
    contacts[name] = {
      'firstname': firstname,
      'lastname': lastname,
      'surname': surname,
      'position': '',
      'organization': '',
      'phone': '',
      'email': '',
    }
  if position:
    contacts[name]['position'] = position
  if organization:
    contacts[name]['organization'] = organization
  if phone:
    contacts[name]['phone'] = phone
  if email:
    contacts[name]['email'] = email


contacts_list = []
for name in contacts:
  contact = contacts[name]
  contacts_list.append([
    contact['lastname'],
    contact['firstname'],
    contact['surname'],
    contact['organization'],
    contact['position'],
    contact['phone'],
    contact['email'],
  ])
print(contacts_list)

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)
