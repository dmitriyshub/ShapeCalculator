import csv
file = 'db.csv'
def Iitialize(file):
	"""

	:param file: dataset file
	:return:
	"""
	local_db = []
	with open('db.csv', encoding='utf-8') as File:
		Reader = csv.reader(File, delimiter=',')

		for row in Reader:
			local_db.append(row)
	titles = tuple(local_db.pop(0))
	return local_db ,titles
dataset,titels = Iitialize(file)
#print(dataset)

# local_db=[]
# with open('db.csv', encoding='utf-8') as File:
#     Reader = csv.reader(File, delimiter=',')
#
#     for row in Reader:
#         local_db.append(row)

# Calculate the mean of a list of numbers
def mean(numbers):
	return sum(numbers)/float(len(numbers))

# Split the dataset by class values, returns a dictionary
def separate_by_class(dataset):
	separated = dict()
	for i in range(len(dataset)):
		vector = dataset[i]
		class_value = vector[-1]
		if (class_value not in separated):
			separated[class_value] = list()
		separated[class_value].append(vector)
	return separated

print(separate_by_class(dataset))
#@print(separate_by_class(local_db))

