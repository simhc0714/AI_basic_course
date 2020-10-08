# _*_ coding: utf-8 _*_

# 전진, 후진
# mod_a.py
# 모듈

# 일정 거리만큼 전진
def forward(loc, d):
    tmp = loc + d
    print("현재 위치는: ", tmp)
    return tmp

# 일정 거리만큼 후진
def backward(loc, d):
    tmp = loc - d
    print("현재 위치는: ", tmp)
    return tmp

## 3만큼 전진

if __name__ == "__main__":
    p_loc = forward(0,3)
    # print("현재 위치는: ", p_loc)


