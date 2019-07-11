import collections
import sys
import csv
from collections import defaultdict
from collections import Counter

csv.field_size_limit(sys.maxsize) #To expand the limit. The limit is 131072 lines. Our data is over 233000. 

###### take transitions data 
columns = defaultdict(list) #each vlaue in each column is appended to a list
with open('user_transitions.csv',"r") as file: #open data file
    reader = csv.reader(file, delimiter='|', quotechar='"') #read rows into a dictionary format
    next(reader) # skip header
    for row in reader: #read a row as {column1 : value1, column2: value2, ...}
        #print(row)
        for i, v in enumerate(row): #go over each column name and value
           columns[i].append(v) #append the value into the appropriate listbased on column name k

tran_id = columns[0]
#print(tran_id[0])
tran_uuid = columns[1]
tran_from_url = columns[2]
tran_to_url = columns[3]
tran_cookie_id = columns[4]
tran_from_material_model_id = columns[5]
tran_to_material_model_id = columns[6]
tran_recommended_urls = columns[7]
tran_selected_position = columns[8]
tran_num_of_recommendations = columns[9]
tran_updated_at = columns[10]

columns2 = defaultdict(list) #each vlaue in each column is appended to a list
with open('urls.csv',"r") as file: #open data file
    reader2 = csv.reader(file, delimiter='|', quotechar='"') #read rows into a dictionary format
    next(reader2) # skip header
    for row in reader2: #read a row as {column1 : value1, column2: value2, ...}
        #print(row)
        for i, v in enumerate(row): #go over each column name and value
           columns2[i].append(v) # append the value into the appropriate listbased on column name k

urls_id = columns2[0]
urls_url = columns2[1]
urls_provider_id = columns2[2]
urls_material_id = columns2[3]

#print(len(tran_to_url)) 
chosenproviders = {}
chosenproviders[0]=[] #tansition id 
chosenproviders[1]=[] #url 
chosenproviders[2]=[] #position 
chosenproviders[3]=[] #provider
for tran in tran_id:
   ind_tran = tran_id.index(tran)
   print('index of transition:', ind_tran)
   from_url = tran_from_url[ind_tran]
   to_url = tran_to_url[ind_tran]
   i = 0
   #chosen material's url 
   print('to url', to_url)
   for url in urls_id:
      ind_urls = urls_id.index(url)
      #print('index of url in the urls file:', ind_urls)
      if urls_url[ind_urls] == to_url:
         print('found:', urls_url[ind_urls])
         chosenproviders[0].append(tran_id[ind_tran])
         chosenproviders[1].append(to_url)
         chosenproviders[2].append(tran_selected_position[ind_tran])
         chosenproviders[3].append(urls_provider_id[ind_urls])
         break
         # else: 
         #    print('nothing')
   #print(chosenproviders)
   break

#print(chosenproviders)


f = open('chosenmaterials.csv', 'w')
fwriter = csv.writer(f, delimiter = ',')
fwriter.writerow(['tran_id','url','position','provider']) #header
length = len(chosenproviders[0])
for i in range(length):
   fwriter.writerow([chosenproviders[0][i], chosenproviders[1][i],chosenproviders[2][i],chosenproviders[3][i]])












# uwcookie = [] #users who accepted cookies i.e. cookie_id value is not empty 
# for i in tran_cookie_id:
#    if i != '':
#       print('The user allowed to cookies use.')
#       uwcookie.append(i)

#    else: 
#       print('Unknown user.')

# print(len(uwcookie)) #number of transitions done by a user who accepted cookiesd. 
# print(len(set(uwcookie))) #number of unique users who accepted cookies in the transition file. 

#statistics on how many recommendations provided 
# cnt= 0 
# avnumrec = 0
# a = 0
# for i in tran_num_of_recommendations:
#    if i != '' and i != 'num_of_recommendations':
#       print('Num of recom.', int(i))
#       cnt = cnt +1
#       a = a + int(i)
#       print('total number of reccommendations', a)
#       print('how many times a recommendation offered', cnt)
#       print('average number of recommendation', a/cnt)
#    # else: 
#    #    print('empty value or heading', i)

# avnumrec = a/cnt
# print(avnumrec)

#statistic on which material at what position selected 
# cnt= 0 
# avnumrec = 0
# a = 0
# firstpage = 0
# scrolleddown = 0
# for i in tran_selected_position:
#    if i != '' and i != 'selected_position':
#       print('Num of the position.', int(i))
#       if int(i) < 7: 
#          firstpage = firstpage + 1 
#       else: 
#          scrolleddown = scrolleddown + 1
#       cnt = cnt +1
#       a = a + int(i)
      # print('total number of reccommendations', a)
      # print('how many times a recommendation offered', cnt)
      #print('average position of a selected recommendation', a/cnt)
   # else: 
   #    print('empty value or heading', i)

# avnumrec = a/cnt
# print(avnumrec)
# print(firstpage, scrolleddown)





























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





#to delete later 
# print(len(tran_to_url)) 
# chosenproviders = []
# for tran in tran_id:
#    ind_tran = tran_id.index(tran)
#    print('index of transition:', ind_tran)
#    from_url = tran_from_url[ind_tran]
#    to_url = tran_to_url[ind_tran]
#    i = 0
#    #chosen material's url 
#    print('to url', to_url)
#   # while(i<len(tran_to_url)):
#       for url in urls_id:
#          ind_urls = urls_id.index(url)
#          #print('index of url in the urls file:', ind_urls)
#          if urls_url[ind_urls] == to_url:
#             print('found:', urls_url[ind_urls])
#             chosenproviders.append(urls_provider_id[ind_urls])
#             #break
#          # else: 
#          #    print('nothing')
#       #i = i+1 
#       #i = 233221 #len(tran_to_url)
#    #print(chosenproviders)
#    break