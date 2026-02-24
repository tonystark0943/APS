def draw_ruler(length, max_tick):
    if length == 0:
        return  
    
    draw_ruler(length - 1, max_tick)
    
    print('-' * length)
    
    draw_ruler(length - 1, max_tick)

draw_ruler(4, 4)