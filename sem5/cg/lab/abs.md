### CG LAB ABS

#### <u>EX 1A</u>

##### Inputs:

- 1st coords (x0,y0)

- 2nd coords (x1,y1)

##### Functions:

- ###### DrawLine(x0,y0,x1,y1)
  
  - x = x0; y = y0
  
  - dx = x1 - x0; dy = y1 - y0
  
  - p = 2 \* dy - dx
  
  - while(x <= x1 && y<= y1)
    
    - putpixel(x, y, 7)
    
    - x++
    
    - p += 2 \* dy
    
    - if(p >= 0)
      
      - y++
      
      - p -= 2\* d

- ###### main()
  
  - Init graphics
  
  - take input from user
  
  - call DrawLine with the inputs
  
  - exit 0

#### <u>EX 1B</u>

##### Inputs

- Radius (r)

##### Functions

- ###### drawCircle(r)
  
  - x = 0; y = r
  
  - xpiv = 320; ypiv = 240
  
  - p = 1 - r
  
  - while (x < y)
    
    - putpixel(xpiv + x, ypiv + y, 7)
    
    - putpixel(xpiv - x, ypiv + y, 7)
    
    - putpixel(xpiv + x, ypiv - y, 7)
    
    - putpixel(xpiv - x, ypiv - y, 7)
    
    - putpixel(xpiv + y, ypiv + x, 7)
    
    - putpixel(xpiv - y, ypiv + x, 7)
    
    - putpixel(xpiv + y, ypiv - x, 7)
    
    - putpixel(xpiv - y, ypiv - x, 7)
    
    - x++
    
    - p += 2x + 3
    
    - if(p >= 0)
      
      - y--
      
      - p -= 2y + 2

- ###### main()
  
  - Init graph
  
  - Get input for radius, r
  
  - call drawCircle(r)

#### <u>EX 02</u>

##### Inputs

- x and y radius, rx, ry

##### Functions

- ###### DrawEll(rx, ry)
  
  - x = 0; y = ry
  
  - xp = 320; yp = 240
  
  - dx = 2 * ry^2
  
  - dy = 2 * rx^2
  
  - p = ry^2 - rx^2 * y
  
  - while(dx < dy)
    
    - put pixel on 4 quads
      
      - xp+x, yp+y, 7
      
      - xp+x, yp-y, 7
      
      - xp-x, yp+y, 7
      
      - xp-x, yp-y, 7
    
    - x++
    
    - dx += 2 * ry^2
    
    - p += dx + ry^2
    
    - if(p>0)
      
      - y--
      
      - dy -= 2 * ry^2
      
      - p -= dy
  
  - p = (ry^2 * x^2) + (rx^2 * y^2) - (rx^2 * ry^2)
  
  - while(y>0)
    
    - put pixel on 4 quads
      
      - xp+x, yp+y, 7
      
      - xp+x, yp-y, 7
      
      - xp-x, yp+y, 7
      
      - xp-x, yp-y, 7
    
    - y--
    
    - dy -= 2 * rx^2
    
    - p -= dy + rx^2
    
    - if(p<0)
      
      - x++
      
      - dx += 2 * ry^2
      
      - p += dx

- ###### main()
  
  - Init graph
  
  - get input for rx, ry
  
  - call drawEll(rx, ry)

#### <u>EX 03</u>

##### Input

- ###### prompt
  
  - Line
  
  - Circle
  
  - Ellipse

- ###### Line
  
  - co-ords (x0, y0, x1, y1)
  
  - line style
  
  - thickness [1 - 3]
  
  - color

- ###### Circle
  
  - radius (r)
  
  - co-ords (xp, yp)
  
  - color
  
  - fill style

- ###### Ellipse
  
  - radius (xr, yr)
  
  - co-ords (xp,yp)
  
  - color
  
  - fill style

##### Functions

- ###### drawline()
  
  - take input for co-ords, line style, thickness, color
  
  - setcolor(color)
  
  - setlinestyle(style, 1, thick)
  
  - line(x,0, y0, x1, y1)

- ###### drawcir()
  
  - take input for radius, co-ords, color, fill-style
  
  - setcolor(color)
  
  - setfillstyle(style, color)
  
  - circle(xp, yp, r)
  
  - floodfill(xp, yp, color)

- ###### drawell()
  
  - take input for radius, co-ords, color, fill-style
  
  - setcolor(color)
  
  - setfillstyle(style, color)
  
  - ellipse(rx, ry, 0, 360, xp, yp)
  
  - fillellipse(rx, ry, xp, yp)

- ###### main()
  
  - init graph
  
  - prompt user to choose between line/circle/ellipse
  
  - call above functions accourdingly

#### <u>EX 04</u>

##### Inputs

- ###### Dimensions
  
  - left corner (x0, y0)
  
  - right corner (x2, y2)

- ###### Prompt
  
  - Translation
  
  - Rotation
  
  - Scaling
  
  - Reflection
  
  - Shearing

- ###### Translation
  
  - shift vector (dx, dy)

- ###### Rotation
  
  - fixed point and angle (dx, dy, deg)

- ###### Scaling
  
  - shift vector (dx, dy)

- ###### Reflection
  
  - Prompt
    
    - x axis
    
    - y axiis
    
    - both axis
  
  - fixed point
