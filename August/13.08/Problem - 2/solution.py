def youngPhysicist():
    forces = int(input())
    totalX,totalY,totalZ =0,0,0
    for f in range(forces):
         x, y, z = map(int, input().split())
         totalX = totalX + x
         totalY = totalY + y
         totalZ = totalZ + z

    if totalX == totalY == totalZ ==0:
        print("YES")
    else:
        print("NO")
    

youngPhysicist()