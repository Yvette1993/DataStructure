import random

def bubble_sort(dataset):
    for i in range(len(dataset)-1): #第i趟
        exchange = False
        for j in range(len(dataset)-i-1):
            if dataset[j] > dataset[j+1]: # 升序
            #if dataset[j] < dataset[j + 1]:  # 降序
                dataset[j], dataset[j+1] = dataset[j+1], dataset[j]
                exchange = True
        if not exchange:
            return

def select_sort_simple(li):
    # 简单的方法，缺点：使用两个列表，占用了两倍的空间。时间复杂度：O(n**2)
    li_new = []
    for i in range(len(li)):
        min_val = min(li)  #时间复杂度O（n）
        li_new.append(min_val)
        li.remove(min_val)  #时间复杂度O（n）
    return li_new

def select_sort(li):
    # 时间复杂度：O(n**2)
    for i in range(len(li)-1): #第i趟
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i],li[min_loc] = li[min_loc], li[i]

def insert_sort(li):
    for i in range(1, len(li)): #i表摸到的牌的下标
        tmp = li[i]
        j = i-1 #j表手里的牌的下标
        while j >= 0 and li[j] > tmp: #找插入的位置
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        print(li)

def partition(li, left, right):
    tmp = li[left]
    while left< right:
        while left < right and li[right]>=tmp:#从右面找比tmp小的数
            right -= 1 #往左走一步
        li[left] = li[right] #把右边的值写到左边空位上
        while left < right and li[left]<=tmp:
            left += 1
        li[right] = li[left] #把左边的值写到右边空位上
    li[left] = tmp    #把tmp归位
    return left
def _quick_sort(data, left, right):        #递归函数
    if left < right:     #至少两个元素
        mid = partition(data, left, right)
        _quick_sort(data, left, mid-1)
        _quick_sort(data, mid+1, right)
def quick_sort(li):               #穿马甲，包装为一个功能
    _quick_sort(li, 0, len(li)-1)


def sift(li, low, high):
    """
    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置，为了下标不越界
    :return:
    """
    i = low
    j = 2*i +1 #j开始是左孩子
    tmp = li[low] #把堆顶存起来
    while j <= high: #只要j位置有数
        if j+1 <= high and li[j+1] > li[j]: #如果右孩子存在且较大
            j = j+1 #指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j      #往下看一层
            j = 2*i +1
        else:  #tmp更大，把tmp放到i的位置上
            li[i] = tmp
            break
    else:
        li[i] = tmp #把tmp放在叶子节点上

def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):
        #i表建堆时调整的部分的根的下标
        sift(li, i, n-1)
    #建堆完成
    print(li)





#li = [random.randint(0,100) for i in range(100)]
li = [3,2,4,1,5,7,9,6,8]
print(li)
#bubble_sort(li)
#insert_sort(li)
quick_sort(li)
print(li)


