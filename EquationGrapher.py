# Python 3.5
# Equation Graph maker from function of one variable

import turtle            

def draw_coordinate_systen(screen_dimension,function, input_range):
    """
    Draws Coordinate System on screen 
    @param screen_dimension 
    """
    turtle.penup()
    turtle.goto(0,screen_dimension[1])
    turtle.pendown()
    turtle.goto(0,-screen_dimension[1])
    turtle.penup()
    turtle.goto(-screen_dimension[1],0)
    turtle.pendown()
    turtle.goto(screen_dimension[1],0)
    turtle.penup()
    turtle.goto(0,0)

    #titles (equation, input_range)
    turtle.color("red")  
    turtle.penup()
    turtle.goto(-screen_dimension[0]+100,screen_dimension[1]-30)
    turtle.pendown()
    turtle.write("Wykres f(x)="+function)
    turtle.penup()
    turtle.goto(-screen_dimension[0]+100,screen_dimension[1]-40)
    turtle.pendown()
    turtle.write("input_range: "+str(input_range))
    turtle.penup()

def draw_borders(screen_dimension, left, right, down, up):
    """
    Draws border titles
    @param screen_dimension
    @param left - left x
    @param right - right x
    @param up - up y
    @param down - down y
    """
    #boundary titles
    turtle.color("black")  
    turtle.penup()
    turtle.goto(-screen_dimension[0]+100,10)
    turtle.pendown()
    if(left<0):
        turtle.write(str(left))
    turtle.penup()
    turtle.goto(screen_dimension[0]-150,10)
    turtle.pendown()
    turtle.write(str(right))
    turtle.penup()
    turtle.goto(5,screen_dimension[1]-20)
    turtle.pendown()
    turtle.write(str(up))
    turtle.penup()
    turtle.goto(5,-screen_dimension[1]+15)
    turtle.pendown()
    if(down<0):
        turtle.write(str(down))

def draw_graph(function, input_range, screen_dimension):
    """
    Draw Graph
    @param function - input equation
    @param input_range - input_range 
    @param screen_dimension - screen dimensions from turtle (2*x, 2*y)
    """
    
    coordinates = []
    suma_input_rangeow = abs(input_range[0]) + abs(input_range[1]) 
    division = 1 if int(suma_input_rangeow / 100) == 0 else int(suma_input_rangeow / 100)     # divide input_rangeu to equal fragments  
	
    for x in range(input_range[0],input_range[1], division):
        try:
            y = eval(function)
        except:
            raise Exception("Wrong f(x)")
        coordinates.append((x, y))

    # Making Zoom
    # If helper to prevent from dividing by 0

    divide_helper_x_down = input_range[0]/(screen_dimension[0]) if input_range[0] != 0 else 1
    down_input_range_rys_x = input_range[0]/abs(divide_helper_x_down)

    divide_helper_x_up = input_range[1]/screen_dimension[0] if input_range[1] != 0 else 1
    up_input_range_rys_x = input_range[1]/abs(divide_helper_x_up)
   
    divide_helper_y_down = eval(function)/screen_dimension[1] if eval(function) != 0 else 1
    down_input_range_rys_y = y/abs(divide_helper_y_down)
    
    x = input_range[1]
    y = eval(function)
    divide_helper_y_up = y/screen_dimension[1] if y != 0 else 1
    up_input_range_rys_y = y/abs(divide_helper_y_up)


    start_flag = True

    # draw titles
    draw_borders(screen_dimension, input_range[0], input_range[1], coordinates[0][1], y)

    # Draw orginal graph
    #for wsp in coordinates:
        #turtle.setpos(wsp[0],wsp[1])
    
    # Draw zoomed graph
    for wsp_skalowana in coordinates:
        x, y
        if(wsp_skalowana[0]<0):
            x = wsp_skalowana[0]/abs(divide_helper_x_down)
        elif(wsp_skalowana[0]==0):
            x = 0;
        elif(wsp_skalowana[0]>0):
            x = wsp_skalowana[0]/abs(divide_helper_x_up)
        if(wsp_skalowana[1]<0):
            y = wsp_skalowana[1]/abs(divide_helper_y_down)
        elif(wsp_skalowana[1]==0):
            y = 0
        elif(wsp_skalowana[1]>0):
            y = wsp_skalowana[1]/abs(divide_helper_y_up)      
        
        if(start_flag):
            
            turtle.penup()
            turtle.goto(x,y) 
            turtle.pendown()
            turtle.color("red")  
            start_flag = False   
               
        turtle.setpos(x,y)

def user_interface():
    """
    User interface
    """
    # Loop until all arguments are valid
    function = None
    input_range_down = None
    input_range_up = None
    while True:
        try:
            if function == None:
                function = input("Enter function of one variable f(x)=")
                # check if function is valid
                x = 1
                y = eval(function)
        except:
            print("Function is not valid")
            function = None
            continue
        try:
            if input_range_down == None:
                input_range_down = int(input("Input the lower range: "))
        except:
            print("Lower range is not valid.")
            continue
        try:
            if input_range_up == None:
                input_range_up = int(input("Input the upper range: "))
        except:
            print("Upper range is not valid.")
            continue
        if(function != None and input_range_down != None and input_range_up != None):

            # switch input_range values is lower is greater from upper
            if(input_range_down > input_range_up):
                input_range_down, input_range_up = input_range_up, input_range_down

            break
     
    input_range = (input_range_down, input_range_up)
    
    turtle.tracer(0, 0)           # auto refresh off
    screen = turtle.Screen()      # make drawing screen
    screen_dimension = screen.screensize()

    draw_coordinate_systen(screen_dimension, function, input_range)       # draw coordinates system
    try:
        draw_graph(function, input_range, screen_dimension)   # draw graph
    except Exception as e:
        print(e)

    turtle.update()               # refresh screen
    screen.mainloop()             # main loop

#start 
user_interface()

