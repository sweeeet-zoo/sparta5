# import sys
# print(sys.version)
import seaborn as sns

def get_tips():
    tips = sns.load_dataset('tips')
    return tips

def print_get():
    #print('테스트 확인') #수동 테스트 확인
    return '일어나세요 용사여!'

if __name__ == '__main__': #자동 테스트(?)
    print_get()
