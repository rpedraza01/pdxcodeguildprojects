#contact_list_demo_with_classes.py

class ContactList:
	def __init__(self, csv = None):
		self.contacts = []
		self.header = ['name', 'age', 'job', 'phone', 'email', 'shoesize']
		if csv:
			self.load(csv)
		#path = "abcdef" # path is a local variable, only works within this scope, not accessible in the rest of the program

	def load(self, path): # self converts the function into a method
		"""
		update self.contacts with parsed csv contacts
		"""
		with open(path) as f:
			lines = f.read().split('\n')

		contacts = []
		header = lines[0].split(',')
		if header != self.header:
			if len(self.contacts) > 0:
				return "CSV not compatible."

		for i in range(1, len(lines)):
			row = lines[i].split(',')
			contact = dict(zip(header, row))
			contacts.append(contact)

		self.contacts += contacts
		self.header = header

	def save(self, path):
    """
    writes contact list to a path.csv file
    """
    lines = [','.join(self.header)]
    for contact in self.contacts:
        row = ','.join(contact.values())
        lines.append(row)

    csv = '\n'.join(lines)

    with open(path, 'w') as f:
        f.write(csv)	

	def find_contact(self, name):
    """
    returns contact index if name exists in contact list
    """
    for i, self.contact in enumerate(contacts):
        if self.contact['name'] == name:
            return i
    return -1


def create(self, contact):
    """
    adds contact to contacts list and returns contact
    :contact: dict
    """
    self.append(contact)
    return contact


def read(self, name):
    """
    returns contact from contacts list given a name
    """
    idx = self.find_contact(self.contacts, name)
    if idx > -1:
        return self.contacts[idx]
    else:
        return f'{name} not in contact list'


def update(self, name, updated_info):
    """
    updates existing contact given a name and dictionary of updated fields
    returns updated contact
    :name: str
    :updated_info: dict
    """
    idx = self.find_contact(self.contacts, name)
    if idx > -1:
        self.contacts[idx].update(updated_info)
        return self.contacts[idx]
    else:
        return f'{name} not in contact list'    


def delete(self, name):
    """
    removes contact from contacts list
    """
    idx = self.find_contact(self.contacts, name)
    if idx > -1:
        return self.contacts.pop(idx)
    else:
        return f'{name} not in contact list'

# don't need to include REPL, but can

if __name__ == '__main__' # all print tests fall under this line
	path = 'contacts_list.csv'
	contacts_list = ContactList("contact_list.csv")
	print(contacts_list.contacts)

	print(contacts_list.create({'name': 'rick', 'age:' 35, 'job:' 'programmer'}))
	print(contacts_list.contacts)

	print(contacts_list.read('rick'))
	print()
	contacts_list.save(path)