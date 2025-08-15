def football():
    situation = input("")
    if '0000000' in situation or '1111111' in situation:
        print("YES")
    else:
        print("NO")
    
football()