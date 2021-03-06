import sys         # 파이썬 인터프리터와 관련된 정보 기능을 제공하는 모듈
import subprocess  # 쉘 명령을 실행할수있게 해주는 라이브러리

print('\n')
print('='*60)
print('\t\t  필요한 모듈 설치')
print('='*60)

# def install(name):

#     subprocess.call(['pip', 'install', name])
#     print('{} 모듈을 설치하였습니다.\n '.format(name))

# module_list = ['pip', 'beautifulsoup4', 'bs4', 'selenium', 'webdriver', 'sympy', 'konlpy', 'tqdm', 'numpy', 'wordcloud', 'matplotlib', 'pandas']

# for i in module_list :
#     install(i)

# try :
#     import wheel
#     print('wheel 버전 : ' + wheel.__version__)
# except :
#     subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'wheel'])
#     print('wheel 모듈을 설치하였습니다.\nwheel 버전 : ' + wheel.__version__)

try :
    import pip
    print('pip 버전 : ' + pip.__version__)
except :
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    print('pip 모듈을 설치하였습니다.\npip : ' + pip.__version__)

try :
    import pandas as pd
    print('pandas 버전 : '+ pd.__version__)
except :
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pandas'])
    print('pandas 모듈을 설치하였습니다.\n')

try :
    import matplotlib as mt
    print('matplotlib 버전: ' + mt.__version__)
except :
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'matplotlib'])
    print('matplotlib 모듈을 설치하였습니다.\nmatplotlib 버전: ' + mt.__version__)

try :
    # 형태소 분석기
    import konlpy as kn
    print('konlpy 버전: ' + kn.__version__)
except :
    # 형태소 분석기
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'konlpy'])
    print('konlpy 모듈을 설치하였습니다.\nkonlpy 버전: ' + kn.__version__)


try :
    import numpy as np
    print('numpy 버전: ' + np.__version__)
except :
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'numpy'])
    print('numpy 모듈을 설치하였습니다.\nnumpy 버전: ' + np.__version__)

try :
    # 작업 진행도
    import tqdm
    print('tqdm 버전: ' + tqdm.__version__)
except :
    # 작업 진행도
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'tqdm'])
    print('tqdm 모듈을 설치하였습니다.\ntqdm 버전: ' + tqdm.__version__)


try :
    from bs4 import BeautifulSoup
except :
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'bs4'])
    print('bs4 모듈을 설치하였습니다.\n')


try :
    import selenium
    print('selenium 버전: ' + selenium.__version__)
except :
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'selenium'])
    print('selenium 모듈을 설치하였습니다.\n')

try :
    import openpyxl
    print('openpyxl 버전: ' + openpyxl.__version__)
except :
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'openpyxl'])
    print('openpyxl 모듈을 설치하였습니다.\n\nopenpyxl 버전: ' + openpyxl.__version__)

try :
    # 시각화
    import wordcloud
    print('wordcloud 버전: ' + wordcloud.__version__)
except :
     # 시각화 
    try :
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'Wordcloud'])
    except :
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'wordcloud-1.7.0-cp310-cp310-win_amd64.whl'])
    print('wordcloud 모듈을 설치하였습니다.\nwordcloud 버전: ' + wordcloud.__version__)

print('\n')
print('모듈 버전 검사를 마쳤습니다.')
