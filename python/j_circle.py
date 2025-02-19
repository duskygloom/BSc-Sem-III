''' QUESTION
Given the following class representing a Circle, add a method calculate ‘circumference’ that
returns the circumference of the circle.
c l a s s C i r c l e :
d e f i n i t ( s e l f , r a d i u s ) :
s e l f . r a d i u s = r a d i u s
d e f c a l c u l a t e a r e a ( s e l f ) :
r e t u r n 3 . 1 4 ∗ s e l f . r a d i u s ∗ s e l f . r a d i u s
# Add t h e c a l c u l a t e c i r c u m f e r e n c e method h e r e
c i r c l e = C i r c l e ( 5 )
p r i n t ( ‘ Area : ’ , c i r c l e . c a l c u l a t e a r e a ( ) )
p r i n t ( ‘ C i r c u m f e r e n c e : ’ , c i r c l e . c a l c u l a t e c i r c u m f e r e n c e ( ) )
'''

class Circle:
    def __init__(self, radius: int):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    
    def calculate_circumference(self):
        return 2 * 3.14 * self.radius
    
circle = Circle(5)
print("Area:", circle.calculate_area())
print("Circumference:", circle.calculate_circumference())

''' OUTPUT
$ python3 j_circle.py 
Area: 78.5
Circumference: 31.400000000000002
'''
