import pandas as pd 
import collections

#import pprint
#path = ''
#file_name = ''

#df500k = pd.read_csv(file_name, sep = '\t',header = None)


# =================== transform poi into trees dictionary ==============
# before use this function, should first usr split_rows() to make sure there is only one tree in each row

def split2trees(tags):
    poi_dic= {}
    #count = 1
    #for i in range(len(tags)):
    row_contents = tags.values            
    for row_content in row_contents:            
        #for items in content:   # if there are many categories in one row
        places = row_content.split(';')
        try:
            poi_dic.setdefault(places[0], {})
            poi_dic[places[0]].setdefault(places[1], {})
            poi_dic[places[0]][places[1]].setdefault(places[2], None)  # The None here is for further labeling
        except Exception as e:
            print e
                #count += 1
    return poi_dic

# ========= return a frequency dictionary ========== 

def freq(tags):    # input = a list of tags
    count = collections.Counter(tags)
    frequency_dic = {}
    for key,value in count.items():
        frequency_dic[key] = (value, 100.0*value/len(tags))
        #print key, value
    return frequency_dic     # return a dictionary = {tagname: (time_appeared, frequency%)}

# ======  create frequency count dataframe =========

def dic2df(dic, file_name = None):         # transform the dictionary from freq() into a dataframe
    freq_df = pd.DataFrame(columns = ['tags','time_appears','frequency']) 
    time = []
    freq = []
    unique_tag = []
    for key, value in dic.items():
        time.append(value[0])
        freq.append(value[1])
        unique_tag.append(key)
        #print key, 'Times appears: %d, frequency: %.2f'%(value[0],value[1]) + '%'
    freq_df.time_appears = time
    freq_df.tags = unique_tag
    freq_df.frequency = freq
    freq_df.sort('time_appears', ascending =False,inplace = True)
    freq_df.reset_index(inplace = True, drop = True)

    freq_df.to_csv(file_name)
    print 'file saved!'
    #return freq_df


# ========== print out to see top frequently appeared tags ============

def most_common(tags, num):     # tags: tags column; num: top * common
    count = collections.Counter(tags)
    frequency = count.most_common(num)
    for item in frequency:
 	    print item[0], item[1]   

# ========== get certain level tags =================

def get_level_tags(tags, level):  # tags: tags column; level input: 0,1,2 
    tag2 = []
    for i in tags.values:
        row_contents = i.split('|')
        for tags in row_contents:
            tag = tags.split(';')
            #print tag[0],tag[1],tag[2]
            tag2.append(tag[level])
    return tag2  # return certain level tags (eg. top level, mid level.)
  
# ========== make sure each rows only have one tree ================= 

def split_rows(tags):  # input a tag column
    output_row = []
    for i in tags.values:
        if '|' in i:
            content= i.split('|')
            for j in content:
                output_row.append(content)
        else:
            output_row.append(i)
    return output_row

# =========== Start scripting here =========================
#data =pd.read_csv('whole_data_freq.csv',sep='\t',header = None)
hangzhou = pd.read_csv('/Users/wifi/Desktop/poi86/zg_poi_amap_hangzhou.csv',sep='\t',header = None)

# tags = hangzhou[6]

# tag3 = get_level_tags(tags, 2)
# tag2 = get_level_tags(tags, 1)
# tag_pair = zip(tag2, tag3)

# frequency_dic  = freq(tag2)
# freq_df = dic2df(frequency_dic, file_name = 'hangzhou_freq.csv')


print len(hangzhou)













