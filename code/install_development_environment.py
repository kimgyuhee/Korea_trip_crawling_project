import sys         # 파이썬 인터프리터와 관련된 정보 기능을 제공하는 모듈
import subprocess  # 쉘 명령을 실행할수있게 해주는 라이브러리

print('\n')
print('='*60)
print('\t\t  필요한 모듈 설치')
print('='*60)

def install(name):

    subprocess.call(['pip', 'install', name])
    print('{} 모듈을 설치하였습니다.\n '.format(name))

module_list = ['pip', 'beautifulsoup4', 'bs4', 'selenium', 'webdriver', 'sympy', 'konlpy', 'tqdm', 'numpy', 'wordcloud', 'matplotlib', 'pandas']

for i in module_list :
    install(i)

# print('모듈 설치중')
# install('pip')
# install('beautifulsoup4')
# install('bs4')
# install('selenium')
# install('webdriver')
# install('sympy')
# print('모듈 끝')

#     subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'tqdm'])
#     print('tqdm 모듈을 설치하였습니다.\ntqdm 버전: ' + tq.__version__)
