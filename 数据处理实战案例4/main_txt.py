#用于生成user.txt文件和item.txt文件

import pandas as pd
from tqdm import tqdm


def shengcheng_user():
    df = pd.read_csv('user_link_map.csv')
    user_x = list(df.user_new_x.values)
    user_y = list(df.user_new_y.values)


    count = 0
    iid_list = []
    sum_iid = []

    while count + 1 < len(user_y):
        iid_list.append(user_y[count])
        while user_x[count] == user_x[count + 1]:
            iid_list.append(user_y[count + 1])
            count += 1
            if count + 1 == len(user_y):
                break

        sum_iid.append(iid_list)
        iid_list = []
        count += 1

    for i in tqdm(sum_iid):
        with open('user.txt', 'a', encoding='utf-8')as f:
            a = ' '.join('%s' % id for id in i)
            f.write(a + '\n')

def shengcheng_item():
    df = pd.read_csv('item_link.csv')
    user_x = list(df.uid.values)
    user_y = list(df.iid.values)

    count = 0
    iid_list = []
    sum_iid = []

    while count + 1 < len(user_y):
        iid_list.append(user_y[count])
        while user_x[count] == user_x[count + 1]:
            iid_list.append(user_y[count + 1])
            count += 1
            if count + 1 == len(user_y):
                break

        sum_iid.append(iid_list)
        iid_list = []
        count += 1

    for i in tqdm(sum_iid):
        with open('item.txt', 'a', encoding='utf-8')as f:
            a = ' '.join('%s' % id for id in i)
            f.write(a + '\n')


if __name__ == '__main__':
    # shengcheng_user()
    shengcheng_item()