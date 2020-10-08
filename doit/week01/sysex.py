# -*- coding: utf-8 -*-
# (실습 3-1)
# 01. py 파일을 생성한다
# 02. 아나콘다 프롬포트를 열기
# 03. 명령어(cd)로 해당 폴더로 이동 후, 파이썬 실행
# python 파이썬파일명.py


import sys
print(sys.argv)

mode = sys.argv[1]
if mode == 'r':
    print("파일 읽기")
elif mode == 'w':
    print("파일 쓰기")