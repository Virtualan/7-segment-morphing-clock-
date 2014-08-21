# 7 segment clock display by Alan Smith
import sys
import pygame
from pygame.locals import *
import time
import math
from random import *

class SevenSegDisplay(object):
    
    def main(self, sc):
        # Define as an array of lists the segments on or off from 0 to 9 #
        seg = [[True, True, True, True, True, True, False],
               [False,True, True, False,False,False,False],
               [True, True, False,True, True, False,True],
               [True, True, True, True, False,False,True],
               [False,True, True, False,False,True, True],
               [True, False,True, True, False,True, True],
               [False,False,True, True, True, True, True],
               [True, True, True, False,False,False,False],
               [True, True, True, True, True, True, True],
               [True, True, True, False,False,True, True]]
               
        ss = 120  # segment size - many other parameters are proportional to this value
        
        #command line argument for size of clock
        
        if len(sys.argv) == 2:   
            ss = int(sys.argv[1])
            if ss > 120: ss = 120
            if ss < 10: ss = 10  
        
        # remaining globals
        
        ep = [150,50]                 # segment endpoint
        clock = pygame.time.Clock()   # timer for screen updates
        screen_size = (1024,300)      # screen size
        screen_color = (0, 0 ,0)      # Black
        pc = (255,255,000)            # yellow
        dc = (255,255,255)            # white 
        sw = ss/10                    # segment width
        sc = pygame.display.set_mode(screen_size,RESIZABLE)
        pygame.display.set_caption('Alans 7 Segment Display Morphing Clock')
        sc.fill(screen_color)
        loop = True
        digitspace = ss/4 + ss
        extradigitspace = digitspace + ss/3
        hourDigit1 = [30,30]
        hourDigit2 = [hourDigit1[0] + digitspace,hourDigit1[1]]
        minDigit1  = [hourDigit2[0] + extradigitspace,hourDigit1[1]]
        minDigit2  = [minDigit1[0] + digitspace,hourDigit1[1]]
        secDigit1  = [minDigit2[0] + extradigitspace,hourDigit1[1]]
        secDigit2  = [secDigit1[0] + digitspace,hourDigit1[1]]
        
        def drawdigit(n,sp):
            #Array of segment points relative to the start point
            zz = [(sp[0],sp[1]),(sp[0]+ss,sp[1]),(sp[0]+ss,sp[1]+ss),(sp[0]+ss,sp[1]+ss+ss),(sp[0],sp[1]+ss+ss),(sp[0],sp[1]+ss)]
            if n > 9: return # only 0 - 9 please
            if seg[n][0]:pygame.draw.line(sc, pc, zz[0],zz[1],sw)   # Seg 0
            if seg[n][1]:pygame.draw.line(sc, pc, zz[1],zz[2],sw)   # Seg 1
            if seg[n][2]:pygame.draw.line(sc, pc, zz[2],zz[3],sw)   # Seg 2
            if seg[n][3]:pygame.draw.line(sc, pc, zz[3],zz[4],sw)   # Seg 3
            if seg[n][4]:pygame.draw.line(sc, pc, zz[4],zz[5],sw)   # Seg 4
            if seg[n][5]:pygame.draw.line(sc, pc, zz[5],zz[0],sw)   # Seg 5
            if seg[n][6]:pygame.draw.line(sc, pc, zz[5],zz[2],sw)   # Seg 6
        
        def drawsegment(n,sp):
            #Array of segment points relative to the start point
            zz = [(sp[0],sp[1]),(sp[0]+ss,sp[1]),(sp[0]+ss,sp[1]+ss),(sp[0]+ss,sp[1]+ss+ss),(sp[0],sp[1]+ss+ss),(sp[0],sp[1]+ss)]
            if n > 6: return # only 0 - 6 please
            if n == 0:pygame.draw.line(sc, pc, zz[0],zz[1],sw)   # Seg 0
            if n == 1:pygame.draw.line(sc, pc, zz[1],zz[2],sw)   # Seg 1
            if n == 2:pygame.draw.line(sc, pc, zz[2],zz[3],sw)   # Seg 2
            if n == 3:pygame.draw.line(sc, pc, zz[3],zz[4],sw)   # Seg 3
            if n == 4:pygame.draw.line(sc, pc, zz[4],zz[5],sw)   # Seg 4
            if n == 5:pygame.draw.line(sc, pc, zz[5],zz[0],sw)   # Seg 5
            if n == 6:pygame.draw.line(sc, pc, zz[5],zz[2],sw)   # Seg 6
        
        def rotate_segment (segment ,q, sp, segs):   # segment, quadrant of rotation, start point, segments to redraw
            #clockwize
            if q == 1: sa,ea = 0,90+15
            if q == 2: sa,ea = 90,180+15
            if q == 3: sa,ea = 180,270+15
            if q == 4: sa,ea = 270,360+15
            #anti-clockwize
            if q == -1: sa,ea = 90,-15
            if q == -2: sa,ea = 180,90-15
            if q == -3: sa,ea = 270,180-15
            if q == -4: sa,ea = 360,270-15  
            
            #Array of segment points relative to the start point
            zz = [(sp[0],sp[1]),(sp[0]+ss,sp[1]),(sp[0]+ss,sp[1]+ss),(sp[0]+ss,sp[1]+ss+ss),(sp[0],sp[1]+ss+ss),(sp[0],sp[1]+ss)]  
            zs = zz[segment]
            
            #clockwize or anti-clockwize speed of rotation
            if sa > ea: s = -15
            if sa < ea: s = 15
            
            #make the segment move
            for x in range (sa,ea,s):                    # start angle, end angle , speed
                lt = time.localtime(time.time())         # keep seconds active while morphing
                sec = '%0*d' % (2,lt[5])
                ep[0]=zs[0]+(ss*math.cos(math.radians(x)) )
                ep[1]=zs[1]+(ss*math.sin(math.radians(x)) )
                pygame.draw.line(sc, pc, zs,ep,sw) 
                #rotate the segments in the lists
                for l in segs:
                    drawsegment(l,sp)
                #keep all other digits visible during morph
                if sp <> hourDigit1:drawdigit(int(hourm[0]),(hourDigit1))  
                if sp <> hourDigit2:drawdigit(int(hourm[1]),(hourDigit2))
                if sp <> minDigit1:drawdigit(int(minm[0]),(minDigit1))
                if sp <> minDigit2:drawdigit(int(minm[1]),(minDigit2))
                if sp <> secDigit1:drawdigit(int(secm[0]),(secDigit1))
                if sp <> secDigit2:drawdigit(int(secm[1]),(secDigit2))
                #draw the colons
                pygame.draw.rect(sc, pc, (hourDigit2[0]+extradigitspace-4*sw,hourDigit2[1]+4*sw,ss/10,ss/10))  
                pygame.draw.rect(sc, pc, (hourDigit2[0]+extradigitspace-4*sw,hourDigit2[1]+ss+4*sw,ss/10,ss/10))  
                pygame.draw.rect(sc, pc, (minDigit2[0]+extradigitspace-4*sw,hourDigit2[1]+4*sw,ss/10,ss/10))  
                pygame.draw.rect(sc, pc, (minDigit2[0]+extradigitspace-4*sw,hourDigit2[1]+ss+4*sw,ss/10,ss/10)) 
                #update the display
                pygame.display.flip()
                pygame.display.update()
                sc.blit(sc, (0, 0))
                sc.fill(screen_color)
              
        def morph_digit(sp,fd,td):   # start point, morph first digit (to) second digit    
            if fd == 0 and td == 1:
                rotate_segment(0,-1,sp,[0,1,2,3,4])
                rotate_segment(4,4,sp,[0,1,2,3])
                rotate_segment(1,-2,sp,[1,2,3])
                rotate_segment(3,3,sp,[1,2])
            if fd == 1 and td == 2: 
                rotate_segment(1,2,sp,[1,2])
                rotate_segment(2,2,sp,[0,1])
                rotate_segment(5,1,sp,[0,1,6])
                rotate_segment(4,4,sp,[0,1,6,4])
            if fd == 2 and td == 3:
                rotate_segment(3,3,sp,[0,1,4,6])
                rotate_segment(4,4,sp,[0,1,6,2])
            if fd == 3 and td == 4:
                rotate_segment(0,1,sp,[1,2,3,6])
                rotate_segment(3,3,sp,[1,2,5,6])
            if fd == 4 and td == 5:
                rotate_segment(1,2,sp,[2,5,6])
                rotate_segment(3,-3,sp,[0,2,5,6])
            if fd == 5 and td == 6:
                rotate_segment(4,-4,sp,[0,2,3,5,6])
            if fd == 6 and td == 7:
                rotate_segment(3,3,sp,[0,2,4,5,6])
                rotate_segment(5,-1,sp,[0,2,5,6])
                #rotate_segment(2,3,sp,[0,2,5])
                rotate_segment(0,-1,sp,[0,1,2])
            if fd == 7 and td == 8:  
                rotate_segment(2,-3,sp,[0,1,2])
                rotate_segment(3,-3,sp,[0,1,2,6])
                rotate_segment(4,-4,sp,[0,1,2,3,6])
                rotate_segment(0,1,sp,[0,1,2,3,4,6])
            if fd == 8 and td == 9: 
                rotate_segment(5,-1,sp,[0,1,2,3,5,6])
            if fd == 9 and td == 0:
                rotate_segment(5,1,sp,[0,1,2,3,5])
            if fd == 5 and td == 0:
                rotate_segment(2,3,sp,[0,2,3,5])
                rotate_segment(4,-4,sp,[0,1,2,3,5])
           
        # MAIN LOOP #
        while loop == True:
            
            #get system time
            lt = time.localtime(time.time())
            
            #format to two digits (leading zeros)
            hour = '%0*d' % (2, lt[3])
            min = '%0*d' % (2,lt[4])
            sec = '%0*d' % (2,lt[5])
            
            #wait a few ticks for h,m,s comparisons
            dt = clock.tick(5)
            
            #store new time
            lt = time.localtime(time.time())
            hourm = '%0*d' % (2, lt[3])
            minm = '%0*d' % (2,lt[4])
            secm = '%0*d' % (2,lt[5])
            
            #draw the colons
            pygame.draw.rect(sc, dc, (hourDigit2[0]+extradigitspace-4*sw,hourDigit2[1]+4*sw,ss/6,ss/6))  
            pygame.draw.rect(sc, dc, (hourDigit2[0]+extradigitspace-4*sw,hourDigit2[1]+ss+4*sw,ss/6,ss/6))  
            pygame.draw.rect(sc, dc, (minDigit2[0]+extradigitspace-4*sw,hourDigit2[1]+4*sw,ss/6,ss/6))  
            pygame.draw.rect(sc, dc, (minDigit2[0]+extradigitspace-4*sw,hourDigit2[1]+ss+4*sw,ss/6,ss/6)) 
            
            #check for digit changes and morph the digits
            if hour[0]<>hourm[0]:morph_digit(hourDigit1,int(hour[0]),int(hourm[0]))
            else:drawdigit(int(hour[0]),(hourDigit1))
            if hour[1]<>hourm[1]:morph_digit(hourDigit2,int(hour[1]),int(hourm[1]))
            else:drawdigit(int(hour[1]),(hourDigit2))
            if min[0]<>minm[0]:morph_digit(minDigit1,int(min[0]),int(minm[0]))
            else:drawdigit(int(min[0]),(minDigit1))
            if min[1]<>minm[1]:morph_digit(minDigit2,int(min[1]),int(minm[1]))
            else:drawdigit(int(min[1]),(minDigit2))
            if sec[0] <> secm[0]:morph_digit(secDigit1,int(sec[0]),int(secm[0]))
            else:drawdigit(int(sec[0]),(secDigit1))
            if sec[1] <> secm[1]:morph_digit(secDigit2,int(sec[1]),int(secm[1]))
            else:drawdigit(int(sec[1]),(secDigit2))
            
            # press any key to quit
            for event in pygame.event.get():
                if event.type ==  QUIT:         
                    return
                elif event.type == KEYDOWN:
                    return
                
if __name__ == '__main__':
    pygame.init()
    sc = pygame.display.set_mode((1024,768),RESIZABLE)
    SevenSegDisplay().main(sc)
    pygame.quit()
    
 
