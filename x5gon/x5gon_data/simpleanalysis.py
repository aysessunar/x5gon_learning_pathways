import collections
import csv
from collections import defaultdict
from collections import Counter

###### take cookies data 

columns = defaultdict(list) #each vlaue in each column is appended to a list
with open('user_activities.csv',"r") as file: #open data file
    reader = csv.reader(file, delimiter='|', quotechar='"') #read rows into a dictionary format
    for row in reader: #read a row as {column1 : value1, column2: value2, ...}
        #print(row)
        for i, v in enumerate(row): #go over each column name and value
           columns[i].append(v) # append the value into the appropriate listbased on column name k
		
users_ua = columns[3]
#users_ua_set = set(users_ua)

urls_viewed = columns[4]
#urls_viewed_set = set(urls_viewed)

f = open('urls_viewed.csv', 'w')
fwriter = csv.writer(f, delimiter = ',')
#fwriter.writerow(['url_id']) #header
#length = len(urls_viewed)
length = 11
for i in range(length):
   fwriter.writerow([users_ua[i], urls_viewed[i]])

#counter = collections.Counter(users_ua)

# m = 0
# for i in counter.values():
#     if i > 1:
#         print("active user")
#     else: 
#         print("it is", i)
#         m=m+1

# print(m)
#print(counter)
#print(counter.values())
#print(counter.most_common(10))

#print(users_ua)

# print(len(columns[3]))
# print(len(users_ua_set))
# print(len(urls_viewed))
# print(len(urls_viewed_set))