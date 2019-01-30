def search_letter(phrase:str,letter=set('aeiou')) ->dict:
    '''调查一个字符串中存在多少个元音'''
    data = {}
    for i in phrase:
        if i in letter:
            if i not in data:
                data[i] = 1
            else:
                data[i]+=1
    return data

if __name__=='__main__':
    k = search_letter('life is good   datating')
    print(k)


asddas  asdasd 123456
asdas asdasd aa123456
asdasdasdqw  as123456d
asdasdqwd  asda123456