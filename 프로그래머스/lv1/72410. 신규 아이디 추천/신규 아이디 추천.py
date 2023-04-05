import re

def solution(new_id):
    
    # 문자열로 치환
    s0 = str(new_id)
    
    # 대문자 -> 소문자
    s1 = new_id.lower()
    
    # 특수문자 제거
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789_-.'
    s2 = ''.join(x for x in s1 if x in chars)
    
    # . 중복 제거
    s3 = re.sub('\.+', '.', s2)

    # . 앞 뒤 제거
    if s3[0] == '.':
        s4_1 = s3[1:]
    else:
        s4_1 = s3
        
    if s4_1 != '':
        if  s4_1[-1] == '.':
                s4_2 = s4_1[:-1]
        else:
            s4_2 = s4_1        
    else:
        s4_2 = s4_1
        
    # 빈 문자열이라면
    if s4_2 == '':
        s5 = 'a'
    else:
        s5 = s4_2
        
    # 16자 이상
    if len(s5) > 15:
        s6_1 = s5[0:15]
    else:
        s6_1 = s5
    
    if s6_1[-1] == '.':
        s6_2 = s6_1[:-1]
    else:
        s6_2 = s6_1
        
    if len(s6_2) == 1:
        s7 = s6_2[0] + s6_2[0] + s6_2[0]
    elif len(s6_2) == 2:    
        s7 = s6_2 + s6_2[-1]
    else:
        s7 = s6_2
    
    answer = s7
    
    return answer