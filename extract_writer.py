import os
import glob
import shutil
from collections import Counter
from PIL import Image

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


# d = {}
# with open('forms_for_parsing.txt') as f:
#     for line in f:
#         key = line.split(' ')[0]
#         writer = line.split(' ')[1]
#         d[key] = writer


# # print([key for key in d.keys() if d[key]=="671"])
# # print(len(d))

# # #make a counter to count num of writers
# # select_writer_list = []

# # num_writers = Counter(d.values())
# # for k,v in num_writers.most_common():
# #     if v >1:
# #         select_writer_list.append(k)

# # print(select_writer_list)
# # print(len(select_writer_list)) #301 writers have more than 1 form. Lets just work of them

# #Select 50 most common writers for this analysis
# select_50_writer = []

# num_writers = Counter(d.values())
# for k,v in num_writers.most_common(50):
#     select_50_writer.append(k)

# # print(select_50_writer)
# # print(len(select_50_writer))

# ## Now I need list of forms related to these writers
# select_forms = []
# for k,v in d.items():
#     if v in select_50_writer:
#         select_forms.append(k)

# # print(select_forms)  #Only has forms associated with top 50 writers
# print(len(select_forms))

# # ##Copy all associated files to a new directory


# cwd = os.getcwd()
# new_path = os.path.join('data','sentences','*.png')
# new_path = "/Users/tejasreddy9/Documents/Handwriting Recognition/"+new_path
# # print(new_path)
# for filename in sorted(glob.glob(new_path)):
# 	# print(filename)
# 	image_name = filename.split('/')[-1]
# 	file, ext = os.path.splitext(image_name)
# 	parts = file.split('-')
# 	form = parts[0]+'-'+parts[1]
# 	if form in select_forms:
# 		dst = os.path.join('data','data_subset',image_name)
# 		dst = "/Users/tejasreddy9/Documents/Handwriting Recognition/"+dst
# 		shutil.copy2(filename,dst)



# after copying
width_list = []
height_list = []
new_path = os.path.join('data','data_subset','*.png')
new_path = "/Users/tejasreddy9/Documents/Handwriting Recognition/"+new_path
for filename in sorted(glob.glob(new_path)):
    im = Image.open(filename)
    width = im.size[0]
    height = im.size[1]
    width_list.append(width)
    height_list.append(height)

plt.plot(width_list)
plt.ylabel('width')
plt.show()

plt.plot(height_list)
plt.ylabel('height')
plt.show()

print("Avg width: ", sum(width_list)/len(width_list))
print("Avg height: ", sum(height_list)/len(height_list))
