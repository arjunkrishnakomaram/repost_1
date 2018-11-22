##"jarceo.extern.ucsd.edu"

# for line in opening_file:
#    if "jarceo.extern.ucsd.edu" in line
#        pr   int(line)
# import re
# #
# user = input("enter date")
# file_name = r"C:\Users\Admin\Desktop\New folder\access_log_Jul95_new.txt"
# fop = open(file_name, 'r', errors = 'ignore')
# opening_file = fop.read()
# # lineno = 0
# fop.close()
# extra = []
# for data in opening_file :
#     if user == '14/Jul/1995':
#         pattern = r"\w+.*?\.\w+.*?\.\w+.*?\.\w+.*"
#     if pattern in data:
#         search_pattern = re.search(pattern, opening_file)
#         print('url found', search_pattern)
#         extra.append(data)
#         print(extra)
#         # print("line number is : ", lineno)
#         # lineno += 1
#     else:
#         print("url Not found")
#         break












#
# file_name = r"C:\Users\Admin\Desktop\New folder\access_log_Jul95_new.txt"
#
# output = []
# pattern = ["jarceo.extern.ucsd.edu"]
#
# with open(file_name, 'r', errors='ignore') as f:
#     s = f.readlines()
# for line_no, line in enumerate(s,1):
#       for data in pattern:
#         if data in line:
#             output.append(line)
#             print('url is present in this line : ', line_no)
#             break
#
# print("No.of times URL accessed is : ", output)
# for ele in output:
#     print(ele)
# print('the length of the output is :  ', len(output))




# Try to find the lines of logs generated on a particular day
#
# import re
#
# file_name1 = r"C:\Users\Admin\Desktop\New folder\access_log_Jul95_new.txt"
#
# # pattern = "14/Jul/1995"
# pattern = '\d.+'
# empty = []
# fop = open(file_name1,'r',errors='ignore')
# reading_file = fop.readlines()
# fop.close()
# for data in reading_file:
#     for date in pattern:
#         if date in data:
#             empty.append(data)
#             break
# print(empty)









import re
file_name1 = r"C:\Users\Admin\Desktop\New folder\access_log_Jul95_new.txt"
find_date = ["14/Jul/1995"]
pattern = ['\w+\.\w+\.\w+\.\w']
empty = []
with open(file_name1, 'r', errors='ignore') as fp:
    read_data = fp.readlines()
    for line_no, data in enumerate(read_data,1):
        for date in find_date:
            for lines in pattern:
                if date in data :
                    s = re.findall(pattern[0], data)
                    empty.append(data)
                    print('Data found', line_no)
                # break
print('The lines of logs generated on a particular day - "14/Jul/1995 is : ', empty)
for ele in empty :
    print(ele)
print('The length of the list is :', len(empty))









# import re
# file_name1 = r"C:\Users\Admin\Desktop\New folder\access_log_Jul95_new.txt"
# find_date = ["14/Jul/1995"]
# pattern = ['\w+\.\w+\.\w+\.\w']
# empty = []
# with open(file_name1, 'r', errors='ignore') as fp:
#     read_data = fp.readlines()
#     for line_no, data in enumerate(read_data,1):
#         for date in find_date:
#             for lines in pattern:
#                 if date in data :
#                     s = re.findall(pattern[0], data)
#                     empty.append(data)
#                     print('Data found', line_no)
#                 # break
# print('The lines of logs generated on a particular day - "14/Jul/1995 is : ', empty)
# for ele in empty :
#     print(ele)
# print('The length of the list is :', len(empty))











