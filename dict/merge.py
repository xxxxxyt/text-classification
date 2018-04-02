in_path = 'stop-list.txt'
out_path = 'stop-list1.txt'

ifs = open(in_path, 'r')
word_list = ifs.read().split('\n')
word_dict = {}
for word in word_list:
    if word in word_dict:
        continue
    else:
        word_dict.update({word : 0})
word_list = [key for key in word_dict]
print(word_list)

ofs = open(out_path, 'w')
ofs.write('\n'.join(word_list))