from cmu_graphics import *

#Digestive System Simulation 
#Authors: Davina Rajendran and Midhousha Anura
#Date: Jan 31, 2023 
#Course: ICS4U
#Description: The user will be able to walk through an interactive simulation of the diegsitve 
              #system while learning about various eznymes and organs involved! They will 
              #also be able to quiz themselves and play an enzyme game at the end!


##...................................................... DRAWINGS ......................................................


###Screen 1 - Digestive System Simulation

app.url = 'https://cdn.vectorstock.com/i/preview-1x/48/74/digestive-system-concept-in-cartoon-style-vector-40544874.jpg'
begin = Rect(120, 330, 170, 30, fill = 'lightCoral')

startScreen = Group(
    Rect(0, 0, 400, 400, fill = None, border = 'crimson', borderWidth = 10),
    Image(app.url, 80, 70),
    Label('Digestive System Simulation', 200, 50, size = 30, font = 'caveat', bold = True, fill = 'crimson'),
    Line(50, 70, 350, 70, fill = 'crimson', lineWidth = 2),
    begin,
    Label('Click HERE to Start!', 205, 345, bold = True, font = 'caveat', size = 20, fill = 'white')
)

###Screen 2 - Menu 

start = Oval(200, 157, 120, 45, fill = 'crimson')
quiz1 =  Oval(200, 237, 120, 45, fill = 'crimson')
quiz2 =  Oval(320, 350, 120, 45, fill = 'crimson')
quiz2Label = Label("Quiz", 320, 348, fill = 'white', font = 'caveat', size = 30)
quiz2.visible = False
quiz2Label.visible = False
game1 =  Oval(200, 317, 120, 45, fill = 'crimson')

instructions = Group(
    Rect(0, 0, 400, 400, fill = None, border = 'crimson', borderWidth = 10),
    Label('Welcome to the Digestive', 200, 60, font = 'caveat', size = 30, fill = 'crimson'),
    Label('System Simulation!', 200, 90, font = 'caveat', size = 30, fill = 'crimson'),
    start,
    Label('Start', 200, 155, fill = 'white', font = 'caveat', size = 25),
    quiz1,
    Label('Quiz', 200, 235, fill = 'white', font = 'caveat', size = 25),
    game1,
    Label('Game', 200, 315, fill = 'white', font = 'caveat', size = 25)
)
instructions.visible = False


###Screen 3 - Body Adjustments

#Next button
next = Group(
        Oval(330, 360, 110, 50, fill = 'lightBlue'),
        Label('Next -> ', 332, 360, font = 'caveat', size = 25)
    )

#Groups the components of the body together
body = Group(
    Circle(85, 130, 10),
    Rect(82, 130, 5, 50),
    Rect(84,150, 25, 5, rotateAngle = 330),
    Rect(60, 150, 25, 5, rotateAngle = 210),
    Rect(67, 185, 25, 5, rotateAngle = 120),
    Rect(76, 185, 25, 5, rotateAngle = 70)
    )
body.centerY = 200
body.centerX = 100

#Age
b1 =Rect(180, 130, 40, 25, fill = 'lightSalmon')
b2 = Rect(220, 130, 40, 25, fill = 'salmon')
b3 = Rect(260, 130, 40, 25, fill = 'darkSalmon')
b4 = Rect(300, 130, 40, 25, fill = 'lightCoral')
b5 = Rect(340, 130, 40, 25, fill = 'crimson')

#Height
b6 = Rect(180, 180, 40, 25, fill = 'lightSalmon')
b7 = Rect(220, 180, 40, 25, fill = 'salmon')
b8 = Rect(260, 180, 40, 25, fill = 'darkSalmon')
b9 = Rect(300, 180, 40, 25, fill = 'lightCoral')
b10 = Rect(340, 180, 40, 25, fill = 'crimson')

#Weight
b11 = Rect(180, 230, 40, 25, fill = 'lightSalmon')
b12 = Rect(220, 230, 40, 25, fill = 'salmon')
b13 = Rect(260, 230, 40, 25, fill = 'darkSalmon')
b14 = Rect(300, 230, 40, 25, fill = 'lightCoral')
b15 = Rect(340, 230, 40, 25, fill = 'crimson')

#Groups all the components of the customization screen together
customizations = Group(
    Label('Select a box in each category to indicate', 280, 78, size = 20, font = 'caveat'),
    Label('your age, height, & weight', 280, 98, size = 20, font = 'caveat'),

    #age
    Label('Age:', 275, 165, size = 20, font = 'caveat'),
    b1,
    Label('0-15',200,140,size = 10),
    b2,
    Label('16-30',240,140,size = 10),
    b3,
    Label('31-45',280,140,size = 10),
    b4,
    Label('45-60',320,140,size = 10),
    b5,
    Label('61+',360,140,size = 10),

    #weight
    Label('Weight:   lbs', 270, 217, size = 20, font = 'caveat'),
    b11,
    Label('0-2',200,240,size = 10),
    b12,
    Label('3-4',240,240,size = 10),
    b13,
    Label('5-6',280,240,size = 10),
    b14,
    Label('7-8',320,240,size = 10),
    b15,
    Label('8+',360,240,size = 10),

    #height
    Label('Height:    ft', 260, 267, size = 20, font = 'caveat'),
    b6,
    Label('0-50',200,190,size = 10),
    b7,
    Label('51-100',240,190,size = 10),
    b8,
    Label('101-150',280,190,size = 10),
    b9,
    Label('151-200',320,190,size = 10),
    b10,
    Label('200+',360,190,size = 10),

    body, 
    next,
)
customizations.centerX = 220
customizations.visible = False

###Screen 4 - The Mouth & Foods

#Mouth
mouth = Group(
    Arc(200, 60, 310, 310, 180, 180, rotateAngle = 270),
    Arc(200, 62, 300, 300, 180, 180, rotateAngle = 270, fill = 'maroon'),
    Rect(63, 62, 275, 45, fill = 'white'),
    Oval(200, 187, 150, 50, fill = 'lightCoral')
    )
mouth.centerY = 220

#Pizza
pizza = Group(
    Rect(170, 280, 50, 15, fill = 'saddlebrown'),
    RegularPolygon(195, 268, 30, 3, fill = 'orange'),
    Circle(185, 270, 5, fill = 'firebrick'),
    Circle(205, 275, 5, fill = 'firebrick'),
    Circle(195, 255, 5, fill = 'firebrick')
    )
pizza.centerX = 100
pizza.centerY = 350

#Salad
salad = Group(
    Arc(345, 260, 65, 45, 180, 180, rotateAngle = 270, fill = 'maroon'),
    RegularPolygon(345, 255, 10, 3, fill = 'olive'),
    RegularPolygon(360, 255, 10, 3, fill = 'green'),
    RegularPolygon(330, 255, 10, 3, fill = 'darkOlivegreen'),
    RegularPolygon(338, 248, 10, 3, fill = 'darkGreen'),
    RegularPolygon(353, 248, 10, 3, fill = 'oliveDrab'),
    Circle(348, 248, 2, fill = 'lightYellow'),
    Circle(345, 257, 2, fill = 'lightYellow'),
    Circle(330, 254, 2, fill = 'lightYellow'),
    Circle(333, 250, 2, fill = 'lightYellow'),
    Circle(358, 255, 2, fill = 'lightYellow'),
    Circle(363, 253, 2, fill = 'lightYellow')
    )
salad.centerX = 200
salad.centerY = 350

#Icecream
icecream = Group(
    RegularPolygon(50, 280, 20, 3, rotateAngle = 180, fill = 'sienna'),
    Arc(50, 270, 35, 35, 180, 180, rotateAngle = 90, fill = 'pink'),
    Arc(50, 260, 30, 30, 180, 180, rotateAngle = 90, fill = 'maroon'),
    Arc(50, 250, 25, 25, 180, 180, rotateAngle = 90, fill = 'lightSkyBlue'),
    Circle(50, 235, 4, fill = 'crimson'),
    Arc(55, 245, 5, 30, 0, 90, rotateAngle = 35, fill = 'brown')
    )
icecream.centerX = 300
icecream.centerY = 350

#Instructions
ints1 = Group( 
    Rect(50, 20, 300, 32, fill = 'powderBlue'),
    Rect(63, 40, 277, 32, fill = 'powderBlue'),
    Rect(63, 60, 277, 32, fill = 'powderBlue'),
    Rect(128, 80, 147, 32, fill = 'powderBlue'),

    Label('On your keyboard, press the letter each food', 200, 35, font = 'caveat', size = 19),
    Label('starts with to view the nutrition facts.', 200, 55, font = 'caveat', size = 19),
    Label('Then, drag the food you want the person', 200, 75, font = 'caveat', size = 19),
    Label('to eat to the mouth', 200, 95, font = 'caveat', size = 19)
)

#Nutritional Label - Icecream
iceint = Group(
    Rect(33, 33, 335, 335, fill = 'lightBlue'),
    Rect(40, 40, 320, 320, fill = 'lavender'),
    Label("Nutrition Facts (Icecream)", 200, 80, bold = True, size = 25, font = 'caveat'),
    Label("Calories           537", 200, 140, font = 'caveat', size = 20),
    Label("Total Fat           28.62g", 200, 160, font = 'caveat', size = 20),
    Label("Cholestrol          107mg", 200, 180, font = 'caveat', size = 20),
    Label("Sodium                 198mg", 200, 200, font = 'caveat', size = 20),
    Label("Total Carbohydrate        65.15g", 180, 220, font = 'caveat', size = 20),
    Label("Protein                 9.4g", 200, 240, font = 'caveat', size = 20),
    Rect(240, 300, 100, 40, fill = 'lightBlue'),
    Label('Press "r" to', 290, 285, font = 'caveat', size = 20),
    Label('Return', 290, 318, font = 'caveat', size = 25)
    )
iceint.visible = False

#Nutritional Label - Salad
salint = Group(
    Rect(33, 33, 335, 335, fill = 'lightBlue'),
    Rect(40, 40, 320, 320, fill = 'lavender'),
    Label("Nutrition Facts (Salad)", 200, 80, bold = True, size = 25, font = 'caveat'),
    Label("Calories                 140", 200, 140, font = 'caveat', size = 20),
    Label("Total Fat                 13g", 200, 160, font = 'caveat', size = 20),
    Label("Cholestrol                 9.3mg", 200, 180, font = 'caveat', size = 20),
    Label("Sodium                 176mg", 200, 200, font = 'caveat', size = 20),
    Label("Total Carbohydrate        6.4g", 180, 220, font = 'caveat', size = 20),
    Label("Protein                 3.8g", 200, 240, font = 'caveat', size = 20),
    Rect(240, 300, 100, 40, fill = 'lightBlue'),
    Label('Press "r" to', 290, 285, font = 'caveat', size = 20),
    Label('Return', 290, 318, font = 'caveat', size = 25)
    )
salint.visible = False

#Nutritional Label - Pizza
pizzaint = Group(
    Rect(33, 33, 335, 335, fill = 'lightBlue'),
    Rect(40, 40, 320, 320, fill = 'lavender'),
    Label("Nutrition Facts (Pizza)", 200, 80, bold = True, size = 25, font = 'caveat'),
    Label("Calories                 266", 200, 140, font = 'caveat', size = 20),
    Label("Total Fat                 10g", 200, 160, font = 'caveat', size = 20),
    Label("Cholestrol                 17mg", 200, 180, font = 'caveat', size = 20),
    Label("Sodium                 598mg", 200, 200, font = 'caveat', size = 20),
    Label("Total Carbohydrate        33g", 180, 220, font = 'caveat', size = 20),
    Label("Protein                 11g", 200, 240, font = 'caveat', size = 20),
    Rect(240, 300, 100, 40, fill = 'lightBlue'),
    Label('Press "r" to', 290, 285, font = 'caveat', size = 20),
    Label('Return', 290, 318, font = 'caveat', size = 25)
    )
pizzaint.visible = False

#Groups the components of the mouth screen together
mouthScreen = Group(
    mouth,
    pizza,
    salad, 
    icecream, 
    ints1
    )
mouthScreen.visible = False

###Screen 5 - The Esophagus

#Esophagus
esophagus = Group(
    Circle(200, 80, 100, fill = 'marron'),
    Arc(105, 95, 50, 40, 180, 180, fill = 'marron'),
    RegularPolygon(115, 75, 40, 3, fill = 'marron'),
    Circle(148, 145, 30, fill = 'marron'),
    Rect(160, 170, 80, 80, fill = 'marron'),
    Oval(130, 410, 550, 350, fill = 'marron'),
    Arc(175, 125, 100, 45, 270, 180, fill = 'pink'),
    Rect(180, 115, 25, 300, fill = 'pink'),
    Circle(217, 120, 10, fill = 'pink'),
    Label('Esophagus', 370, 40, font = 'caveat', size = 32),
    Line(320, 58, 430, 58, fill = 'crimson')
)
esophagus.centerX = 80
esophagus.visible = False

#Label - What happens in the esophagus
peristalsis = Group(
    Circle(153, 194, 7, fill = 'lightCoral'),
    Line(153, 194, 280, 194, lineWidth = 5, fill = 'lightCoral'),
    Rect(200, 165, 180, 110, fill = 'lightCoral'),
    Label("The food moves", 290, 185, size = 20, fill = 'white', font = 'caveat'),
    Label("through the esophagus", 290, 204, size = 20, fill = 'white', font = 'caveat'),    
    Label("in wave-like", 290, 221, size = 20, fill = 'white', font = 'caveat'),    
    Label("contractions called", 290, 238, size = 20, fill = 'white', font = 'caveat'),    
    Label("peristalsis", 290, 255, size = 20, fill = 'white', font = 'caveat')   
    )
peristalsis.visible = False

###SCREEN 6 - The Stomach 

#Labels the Stomach
ints2 = Group(
    Line(32, 68, 132, 68, fill = 'crimson'),
    Label('Stomach', 85, 50, font = 'caveat', size = 35),
    )
ints2.visible = False

#Groups all the stomach components together
acid = Oval(185, 267, 170, 230, fill = 'orange', opacity = 30, rotateAngle = 80)
stomach = Group(
    #stomach
    Oval(230, 170, 190, 250, fill = 'crimson'),
    Oval(215, 225, 200, 250, fill = 'crimson', rotateAngle = 30),
    Oval(190, 260, 210, 250, fill = 'crimson', rotateAngle = 65),

    #bottom
    Oval(80, 280, 60, 60, fill ='crimson', rotateAngle = 90),
    Oval(70, 300, 60, 80, fill = 'crimson'),
    Oval(67, 340, 60, 200, fill = 'crimson'),
    Oval(87, 260, 65, 125, fill = 'crimson', rotateAngle = 30),

    #top
    Oval(177, 80, 70, 150, fill = 'crimson', rotateAngle = -25),
    Oval(170, 50, 50, 230, fill = 'crimson', rotateAngle = -20),
    Oval(155, 30, 60, 110, fill = 'crimson'),

    #inside 
    Oval(230, 170, 170, 230, fill = 'lightSalmon'),
    Oval(215, 225, 170, 220, fill = 'lightSalmon', rotateAngle = 30),
    Oval(190, 260, 180, 220, fill = 'lightSalmon', rotateAngle = 65),
    Oval(145, 270, 140, 150, fill = 'lightSalmon', rotateAngle = 55),

    #filling top
    Oval(177, 80, 55, 150, fill = 'lightSalmon', rotateAngle = -25),
    Oval(170, 50, 30, 230, fill = 'lightSalmon', rotateAngle = -20),
    Oval(155, 30, 40, 110, fill = 'lightSalmon'),

    #filling bottom
    Oval(90, 275, 60, 70, fill ='lightSalmon', rotateAngle = 20),
    Oval(67, 340, 45, 150, fill = 'lightSalmon'),
    Oval(90, 275, 60, 70, rotateAngle = 30, fill = 'orange', opacity = 17),
    Oval(67, 340, 45, 150, fill = 'orange', opacity = 17),

    #food
    Circle(180, 300, 20, fill = 'wheat', border = 'sandybrown'),
    Circle(215, 310, 17, fill = 'wheat', border = 'sandybrown'),
    Circle(230, 290, 10, fill = 'wheat', border = 'sandybrown'),
    Circle(250, 290, 12, fill = 'wheat', border = 'sandybrown'),    
    Circle(250, 300, 10, fill = 'wheat', border = 'sandybrown'),  
    Circle(240, 310, 15, fill = 'wheat', border = 'sandybrown'),
    Circle(225, 270, 11, fill = 'wheat', border = 'sandybrown'),
    Circle(260, 270, 17, fill = 'wheat', border = 'sandybrown'),
    Circle(190, 280, 17, fill = 'wheat', border = 'sandybrown'),
    Circle(210, 290, 14, fill = 'wheat', border = 'sandybrown'),        
    Circle(200, 300, 10, fill = 'wheat', border = 'sandybrown'),
    Circle(200, 320, 14, fill = 'wheat', border = 'sandybrown'),
    Circle(240, 270, 14, fill = 'wheat', border = 'sandybrown'),
    Circle(205, 270, 14, fill = 'wheat', border = 'sandybrown'),
    acid
)    
stomach.centerX = 220
stomach.visible = False

#Groups all the information about the enzymes in the stomach
returnBox = Rect(280, 350, 90, 40, fill = 'lightBlue')
enzStomach = Group(
    returnBox,
    Label('Return', 325, 367, font = 'caveat', size = 25),
    Label('Enzymes of the Stomach', 200, 40, fill = 'crimson', font = 'caveat', size = 32),
    Line(50, 60, 350, 60, fill = 'crimson'),
    Rect(30, 95, 80, 40, fill = 'crimson'),

    #Pepsin
    Label("Pepsin", 70, 113, fill = 'white', font = 'caveat', size = 23),
    Label("is secreted by the stomach to break", 250, 93, font = 'caveat', size = 20),
    Label("down proteins into peptides or smaller", 250, 113, font = 'caveat', size = 20),
    Label("groups of amino acids", 250, 133, font = 'caveat', size = 20),

    #Amylase
    Rect(30, 195, 80, 40, fill = 'crimson'),
    Label("Amylase", 70, 215, fill = 'white', font = 'caveat', size = 23),
    Label("is an enzyme produced in the pancreas", 250, 195, font = 'caveat', size = 20),
    Label("that breaks down carbohydrates into", 250, 215, font = 'caveat', size = 20),
    Label(" sugars.", 250, 235, font = 'caveat', size = 20),

    #Lipase
    Rect(30, 295, 80, 40, fill = 'crimson'),
    Label("Lipase", 70, 315, fill = 'white', font = 'caveat', size = 23),
    Label("is an enzyme that is used to break", 250, 295, font = 'caveat', size = 20),
    Label("down fats in food so they can be", 250, 315, font = 'caveat', size = 20),
    Label("can be absorbed in the intestines.", 250, 335, font = 'caveat', size = 20)
    )

enzStomach.visible = False

#Label - What happens in the stomach
stomachLabel1 = Group(
    Rect(25, 142, 230, 120, fill = 'powderBlue'),
    Label("Glands in the stomach lining make", 142, 162, size = 18, font = 'caveat'),
    Label("stomach acid and enzymes that", 142, 182, size = 18, font = 'caveat'),    
    Label("break down food chemically.", 142, 202, size = 18, font = 'caveat'),    
    Label("The stomach muscles mix the", 142, 222, size = 18, font = 'caveat'),    
    Label("food with these digestive juices.", 142, 242, size = 18, font = 'caveat'),
    Circle(160, 300, 7, fill = 'powderBlue'),
    Line(100, 250, 160, 300, lineWidth = 5, fill = 'powderBlue')
    )
stomachLabel1.centerY = 180 
stomachLabel1.visible = False   

#Label - Informs the user to click "here" to learn about the enzymes
hereEnzStomach = Oval(75, 85, 35, 25, fill = 'salmon')
stomachLabel2 = Group(
    hereEnzStomach,
    Label('Click          to learn', 85, 85, font = 'caveat', size = 18),
    Label('here', 75, 85, font = 'caveat', size = 18, fill = 'white'),
    Label('about the enzymes', 85, 105, font = 'caveat', size = 18),
    Label('in the stomach!', 85, 125, font = 'caveat', size = 18)
    )
stomachLabel2.centerY = 50 
stomachLabel2.centerX = 85
stomachLabel2.visible = False   

####SCREEN 7 - Small Intestine, Large Intestine & Rectum

#Small intestine
smallint = Group(
    Oval(100, 116, 24, 53, rotateAngle = 110, fill = 'maroon'),
    Oval(170, 130, 24, 50, rotateAngle = 110, fill = 'maroon'),
    Oval(190, 132, 24, 50, rotateAngle = 85, fill = 'maroon'),
    Oval(140, 122, 24, 50, rotateAngle = 100, fill = 'maroon'),
    Oval(215, 130, 24, 50, rotateAngle = 100, fill = 'maroon'),
    Oval(225, 135, 24, 50, rotateAngle = 110, fill = 'maroon'),
    Oval(250, 155, 24, 50, rotateAngle = 150, fill = 'maroon'),
    Oval(260, 185, 24, 50, rotateAngle = 180, fill = 'maroon'),
    Oval(250, 208, 24, 50, rotateAngle = 45, fill = 'maroon'),
    Oval(207, 215, 24, 50, rotateAngle = 90, fill = 'maroon'),
    Oval(185, 225, 24, 50, rotateAngle = 220, fill = 'maroon'),
    Oval(190, 250, 24, 50, rotateAngle = 110, fill = 'maroon'),
    Oval(220, 245, 24, 50, rotateAngle = 60, fill = 'maroon'),
    Oval(235, 215, 24, 50, rotateAngle = 170, fill = 'maroon'),
    Oval(225, 195, 24, 50, rotateAngle = 150, fill = 'maroon'),
    Oval(200, 180, 24, 50, rotateAngle = 90, fill = 'maroon'),
    Oval(175, 174, 24, 50, rotateAngle = 110, fill = 'maroon'),
    Oval(150, 173, 24, 50, rotateAngle = 75, fill = 'maroon'),
    Oval(130, 182, 24, 50, rotateAngle = 50, fill = 'maroon'),
    Oval(120, 210, 24, 50, rotateAngle = -10, fill = 'maroon'),
    Oval(125, 230, 24, 50, rotateAngle = -15, fill = 'maroon'),
    Oval(135, 255, 24, 50, rotateAngle = -25, fill = 'maroon'),
    Oval(170, 295, 24, 50, rotateAngle = -70, fill = 'maroon'),
    Oval(200, 298, 24, 50, rotateAngle = 90, fill = 'maroon'),
    Oval(235, 290, 20, 50, rotateAngle = 60, fill = 'maroon'),
    Oval(262, 267, 20, 50, rotateAngle = 40, fill = 'maroon'),
    Oval(275, 242, 20, 50, rotateAngle = 20, fill = 'maroon'),
    Oval(280, 215, 20, 50, rotateAngle = 10, fill = 'maroon'),
    Oval(285, 195, 20, 50, rotateAngle = 5, fill = 'maroon'),
    Oval(285, 165, 20, 50, rotateAngle = -10, fill = 'maroon'),
    Oval(275, 140, 20, 50, rotateAngle = -30, fill = 'maroon'),
    Oval(250, 132, 20, 50, rotateAngle = 70, fill = 'maroon'),
    Oval(230, 155, 20, 50, rotateAngle = 40, fill = 'maroon'),
    Oval(208, 180, 20, 50, rotateAngle = 40, fill = 'maroon'),
    Oval(202, 200, 20, 50, rotateAngle = -20, fill = 'maroon'),
    Oval(210, 225, 20, 50, rotateAngle = -20, fill = 'maroon'),
    Oval(235, 260, 20, 50, rotateAngle = -60, fill = 'maroon'),
    Oval(260, 270, 20, 50, rotateAngle = -80, fill = 'maroon'),
    Oval(265, 275, 20, 50, rotateAngle = -80, fill = 'maroon'),
    Oval(270, 293, 20, 50, rotateAngle = 60, fill = 'maroon'),
    Oval(255, 300, 20, 50, rotateAngle = 65, fill = 'maroon'),
    Oval(223, 310, 20, 50, rotateAngle = 80, fill = 'maroon'),
    Oval(195, 315, 20, 50, rotateAngle = 85, fill = 'maroon'),
    Oval(175, 320, 20, 50, rotateAngle = 75, fill = 'maroon'),
    Oval(150, 315, 20, 50, rotateAngle = -60, fill = 'maroon'),
    Oval(145, 290, 20, 50, rotateAngle = 40, fill = 'maroon'),
    Oval(170, 275, 20, 50, rotateAngle = 90, fill = 'maroon'),
    Oval(200, 277, 20, 50, rotateAngle = 100, fill = 'maroon'),
    Oval(210, 265, 20, 50, rotateAngle = -45, fill = 'maroon'),
    Oval(170, 230, 20, 50, rotateAngle = -30, fill = 'maroon'),
    Oval(170, 195, 20, 50, rotateAngle = 30, fill = 'maroon'),
    Oval(190, 170, 20, 50, rotateAngle = 40, fill = 'maroon'),
    Oval(180, 150, 20, 50, rotateAngle = 90, fill = 'maroon'),
    Oval(150, 147, 20, 50, rotateAngle = 100, fill = 'maroon'),
    Oval(120, 150, 20, 50, rotateAngle = 70, fill = 'maroon'),
    Oval(110, 172, 20, 50, rotateAngle = -20, fill = 'maroon'),
    Oval(130, 200, 20, 50, rotateAngle = -30, fill = 'maroon'),
    Oval(145, 220, 20, 50, rotateAngle = -20, fill = 'maroon'),
    Oval(150, 245, 20, 50, rotateAngle = -10, fill = 'maroon'),
    Oval(135, 308, 22, 50, rotateAngle = -45, fill = 'maroon'),
    )
smallint.fill = 'pink'
smallint.visible = False 

#Large intestine
largeint = Group(
    Oval(75, 325, 95, 50, fill = 'lightCoral'),
    Oval(73, 300, 90, 50, fill = 'lightCoral'),
    Oval(70, 275, 85, 50, fill = 'lightCoral'),
    Oval(68, 250, 80, 50, fill = 'lightCoral'),
    Oval(65, 225, 75, 50, fill = 'lightCoral'),
    Oval(63, 200, 70, 50, fill = 'lightCoral'),
    Oval(60, 175, 65, 50, fill = 'lightCoral'),
    Oval(58, 150, 60, 50, fill = 'lightCoral'),
    Oval(55, 125, 55, 50, fill = 'lightCoral'),
    Oval(60, 115, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(65, 113, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(70, 110, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(75, 110, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(80, 108, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(85, 108, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(90, 108, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(95, 108, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(100, 108, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(105, 108, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(110, 110, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(115, 110, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(120, 110, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(125, 110, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(130, 110, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(135, 112, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(140, 112, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(145, 112, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(150, 114, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(155, 114, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(160, 114, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(165, 114, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(170, 116, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(175, 116, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(180, 116, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(185, 116, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(190, 116, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(195, 116, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(200, 118, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(205, 118, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(210, 118, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(215, 118, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(220, 118, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(225, 118, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(230, 114, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(235, 114, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(240, 114, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(245, 114, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(250, 114, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(255, 114, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(260, 112, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(265, 112, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(270, 112, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(275, 110, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(280, 110, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(285, 110, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(290, 108, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(300, 108, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(310, 106, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(315, 106, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(320, 104, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(325, 104, 55, 50, fill = 'lightCoral'),
    Oval(330, 110, 55, 50, fill = 'lightCoral'),
    Oval(330, 115, 55, 50, fill = 'lightCoral'),
    Oval(330, 120, 55, 50, fill = 'lightCoral'),
    Oval(330, 125, 60, 50, fill = 'lightCoral'),
    Oval(330, 130, 60, 50, fill = 'lightCoral'),
    Oval(330, 135, 60, 50, fill = 'lightCoral'),
    Oval(330, 140, 60, 50, fill = 'lightCoral'),
    Oval(330, 145, 65, 50, fill = 'lightCoral'),
    Oval(330, 150, 65, 50, fill = 'lightCoral'),
    Oval(330, 175, 65, 50, fill = 'lightCoral'),
    Oval(330, 200, 65, 50, fill = 'lightCoral'),
    Oval(330, 225, 65, 50, fill = 'lightCoral'),
    Oval(330, 250, 65, 50, fill = 'lightCoral'),
    Oval(330, 275, 65, 50, fill = 'lightCoral'),
    Oval(330, 300, 70, 50, fill = 'lightCoral'),
    Oval(330, 325, 70, 50, fill = 'lightCoral'),
    Oval(330, 350, 70, 50, fill = 'lightCoral'),
    Oval(320, 350, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(310, 355, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(300, 355, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(290, 360, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(280, 365, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(270, 365, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(260, 370, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(250, 370, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(240, 375, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(230, 375, 55, 50, fill = 'lightCoral', rotateAngle = 90),
    Oval(220, 375, 70, 50, fill = 'lightCoral'),
    Oval(210, 380, 40, 50, fill = 'lightCoral'),
    Oval(210, 385, 40, 50, fill = 'lightCoral'),
    Oval(210, 390, 40, 50, fill = 'lightCoral'),
    Oval(210, 395, 40, 50, fill = 'lightCoral'),
    Oval(210, 400, 40, 50, fill = 'lightCoral'),
    Oval(210, 405, 40, 50, fill = 'lightCoral'),
    Oval(210, 410, 35, 50, fill = 'lightCoral'),
    Oval(210, 415, 35, 50, fill = 'lightCoral'),
    Oval(210, 420, 35, 50, fill = 'lightCoral'),
    Oval(210, 425, 35, 50, fill = 'lightCoral'),
    Oval(210, 430, 30, 50, fill = 'lightCoral'),
    Oval(210, 435, 30, 50, fill = 'lightCoral'),
    Rect(88, 0, 23, 150, fill = 'pink'),
    )
largeint.centerY = 200
largeint.visible = False

#Label - Small & Large intestine
intLabels = Group (
    Circle(140, 310, 7, fill = 'powderBlue'),
    Line(140, 310, 115, 345, lineWidth = 4, fill = 'powderBlue'),
    Rect(25, 335, 150, 30, fill = 'powderBlue'),
    Label('Small Intestine', 100, 350, font = 'caveat', size = 20),


    Circle(151, 72, 7, fill = 'powderBlue'),
    Line(151, 72, 183, 37, lineWidth = 4, fill = 'powderBlue'),
    Rect(155, 20, 150, 30, fill = 'powderBlue'),
    Label('Large Intestine', 230, 34, font = 'caveat', size = 20)
)
intLabels.visible = False

#Label - Rectum
rectumLabel = Group (
    Circle(193, 150, 5, fill = 'powderBlue'),
    Line(193, 150, 155, 170, fill = 'powderBlue', lineWidth = 5),
    Rect(65, 148, 100, 35, fill = 'powderBlue'),
    Label("Rectum", 115, 165, font = 'caveat', size = 25),

    Rect(15, 195, 170, 95, fill = 'powderBlue'),
    Label("The rectum is an 8 inch", 100, 210, font = 'caveat', size = 18),
    Label("chamber that receives", 100, 230, font = 'caveat', size = 18),
    Label("stool from the colon &", 100, 250, font = 'caveat', size = 18),   
    Label("excretes it out of the body.", 100, 270, font = 'caveat', size = 18)
)
rectumLabel.visible = False

#Sets a counter to determine which screen to the user is currently on 
counter = Rect(10, 400, 10, 10, fill = 'white')
counter.visible = False

#Food clumps
foodClump = Group(
    Circle(197, 130, 5, fill = 'wheat', border = 'sandyBrown'),
    Circle(188, 126, 6, fill = 'wheat', border = 'sandyBrown'),
    Circle(189, 117, 5, fill = 'wheat', border = 'sandyBrown'),
    Circle(195, 121, 6, fill = 'wheat', border = 'sandyBrown'),
    Circle(195, 113, 6, fill = 'wheat', border = 'sandyBrown'),
    Circle(197, 160, 5, fill = 'wheat', border = 'sandyBrown'),
    Circle(188, 156, 6, fill = 'wheat', border = 'sandyBrown'),
    Circle(189, 137, 5, fill = 'wheat', border = 'sandyBrown'),
    Circle(195, 151, 6, fill = 'wheat', border = 'sandyBrown'),
    Circle(195, 143, 6, fill = 'wheat', border = 'sandyBrown'),
    Circle(197, 190, 5, fill = 'wheat', border = 'sandyBrown'),
    Circle(188, 186, 6, fill = 'wheat', border = 'sandyBrown'),
    Circle(189, 167, 5, fill = 'wheat', border = 'sandyBrown'),
    Circle(195, 181, 6, fill = 'wheat', border = 'sandyBrown'),
    Circle(195, 173, 6, fill = 'wheat', border = 'sandyBrown')
    )

foodClump.visible = False
foodClump.centerX = 130

chyme = Group(
    Circle(204, 274, 4, fill = 'wheat', border = 'sandybrown'),
    Circle(200, 278, 4, fill = 'wheat', border = 'sandybrown'),
    Circle(198, 272, 4, fill = 'wheat', border = 'sandybrown'),
    Circle(193, 280, 3, fill = 'wheat', border = 'sandybrown'),
    Circle(192, 274, 3, fill = 'wheat', border = 'sandybrown'),
    )
chyme.visible = False

smallFoodClumps = Group(
    Circle(256, 247, 5, fill = 'wheat', border = 'sandybrown'),
    Circle(250, 252, 7, fill = 'wheat', border = 'sandybrown'),
    Circle(248, 242, 5, fill = 'wheat', border = 'sandybrown'),
    Circle(243, 250, 4, fill = 'wheat', border = 'sandybrown'),
    Circle(278, 247, 7, fill = 'wheat', border = 'sandybrown'),
    Circle(285, 242, 6, fill = 'wheat', border = 'sandybrown'),
    Circle(288, 248, 5, fill = 'wheat', border = 'sandybrown'),
    Circle(257, 240, 5, fill = 'wheat', border = 'sandybrown'),
    Circle(211, 232, 4, fill = 'wheat', border = 'sandybrown'),
    Circle(208, 222, 7, fill = 'wheat', border = 'sandybrown'),
    Circle(208, 240, 6, fill = 'wheat', border = 'sandybrown'),
    Circle(197, 227, 5, fill = 'wheat', border = 'sandybrown'),
    Circle(205, 229, 5, fill = 'wheat', border = 'sandybrown'),
    Circle(251, 214, 8, fill = 'wheat', border = 'sandybrown'),
    Circle(256, 218, 6, fill = 'wheat', border = 'sandybrown'),
    Circle(260, 210, 5, fill = 'wheat', border = 'sandybrown')
    )
smallFoodClumps.visible = False

stool = Group(
    Circle(211, 232, 4, fill = 'sandyBrown', border = 'coral'),
    Circle(208, 222, 7, fill = 'sandyBrown', border = 'coral'),
    Circle(208, 240, 6, fill = 'sandyBrown', border = 'coral'),
    Circle(197, 227, 5, fill = 'sandyBrown', border = 'coral'),
    Circle(205, 229, 5, fill = 'sandyBrown', border = 'coral'),
    Circle(197, 234, 6, fill = 'sandyBrown', border = 'coral'),
    Circle(200, 238, 4, fill = 'sandyBrown', border = 'coral')
    )
stool.centerX = 60
stool.centerY = 280
stool.visible = False

#Label - What is the small intestine
next2 = Rect(300, 270, 70, 40, fill = 'lightSalmon')
smallintLabel = Group(
    Rect(40, 110, 320, 170, fill = 'powderBlue'),
    Label("The small intestine is a maze-like coil that", 200, 135, font = 'caveat', size = 19),
    Label("is 22 to 25 feet long. Digestive fluids &", 200, 155, font = 'caveat', size = 19),
    Label("enzymes produced by the small intestine's", 200, 175, font = 'caveat', size = 19),
    Label("walls collaborate with the liver & pancreatic", 200, 195, font = 'caveat', size = 19),
    Label("enzymes. Nearly all the nutrients from", 200, 215, font = 'caveat', size = 19),
    Label("your meals are absorbed into your", 200, 235, font = 'caveat', size = 19),
    Label("circulation through the small intestine", 200, 255, font = 'caveat', size = 19),
    next2,
    Label("Next", 335, 290, font = 'caveat', size = 25)
    )
smallintLabel.visible = False

#Label - What is the large intestine
returnBox2 = Rect(300, 235, 70, 40, fill = 'lightSalmon')
largeintLabel = Group(
    Rect(40, 110, 320, 135, fill = 'powderBlue'),
    Label("The large intestine is about 5 to 6 feet", 200, 135, font = 'caveat', size = 19),
    Label("long & it contains unique type of muscle", 200, 155, font = 'caveat', size = 19),
    Label("that contracts in waves. It is responsible", 200, 175, font = 'caveat', size = 19),
    Label("for producing & draining excess water", 200, 195, font = 'caveat', size = 19),
    Label("from feces so that it can exit the body normal.", 200, 215, font = 'caveat', size = 19),
    returnBox2,
    Label("Got it!", 335, 255, font = 'caveat', size = 23)
    )
largeintLabel.visible = False

####Screen 8 - Quiz 

#Assigns the correct answer to each question to the respective variable
ans1 = Rect(60, 240, 120, 40, fill = 'lightYellow', border = 'bisque')
ans2 = Rect(230, 160, 120, 40, fill = 'lightYellow', border = 'bisque')
ans3 = Rect(60, 240, 120, 40, fill = 'lightYellow', border = 'bisque')
ans4 = Rect(50, 160, 140, 40, fill = 'lightYellow', border = 'bisque')
ans5 = Rect(50, 240, 140, 40, fill = 'lightYellow', border = 'bisque')

#Groups all the components of the quiz together
score = Label(0, 223, 340, size = 30, font = 'caveat')
quizBackground = Group(
    #Background
    Rect(0, 0, 400, 400, fill = 'blanchedAlmond'),
    Rect(0, 0, 400, 400, borderWidth = 15, fill = None, border = 'bisque'),
    Line(90, 75, 310, 75, fill = 'crimson'),
    Rect(30, 100, 340, 30, fill = 'salmon'),
    Label("Score:    /5", 200, 340, font = 'caveat', size = 32),
    score,

    #Options
    Rect(60, 160, 120, 40, fill = 'lightYellow', border = 'bisque'),
    Rect(230, 160, 120, 40, fill = 'lightYellow', border = 'bisque'),
    Rect(60, 240, 120, 40, fill = 'lightYellow', border = 'bisque'),
    Rect(230, 240, 120, 40, fill = 'lightYellow', border = 'bisque')
    )
quizBackground.visible = False

#Groups the components of the game button toegther 
game = Oval(320, 350, 90, 45, fill = 'crimson')
game2 = Group (
    game,
    Label("Game", 320, 348, fill = 'white', font = 'caveat', size = 30)
)
game2.visible = False

##Quiz Questions

#Question 1
quizQ1 = Group(
    Label('Question #1', 200, 50, fill = 'crimson', font = 'caveat', size = 36),
    Label("What is the first part of the digestive tract?", 200, 115, fill = 'white', font = 'caveat', size = 20),
    Label("a. Stomach", 118, 180, font = 'caveat', size = 20),
    Label("b. Esophagus", 288, 180, font = 'caveat', size = 20),
    ans1,
    Label("c. Mouth", 118, 260, font = 'caveat', size = 20),
    Label("d. Rectum", 288, 260, font = 'caveat', size = 20),
)

quizQ1.visible = False

#Question 2
quizQ2 = Group (
    Label('Question #2', 200, 50, fill = 'crimson', font = 'caveat', size = 36),
    Label("What is the length of the small intestine?", 200, 115, fill = 'white', font = 'caveat', size = 20),
    Label("a. 10 ft", 118, 180, font = 'caveat', size = 20),
    ans2,
    Label("b. 22 - 25 ft", 288, 180, font = 'caveat', size = 20),
    Label("c. 25 - 30 ft", 118, 260, font = 'caveat', size = 20),
    Label("d. 30 - 35 ft", 288, 260, font = 'caveat', size = 20),
)

quizQ2.visible = False

#Question 3
quizQ3 = Group (
    Label('Question #3', 200, 50, fill = 'crimson', font = 'caveat', size = 36),
    Label("Which enzyme breaks proteins into peptides", 200, 115, fill = 'white', font = 'caveat', size = 20),

    Label("a. Amylase", 118, 180, font = 'caveat', size = 20),
    Label("b. Lipase", 288, 180, font = 'caveat', size = 20),
    ans3,
    Label("c. Pepsin", 118, 260, font = 'caveat', size = 20),
    Label("d. Carbohydrase", 288, 260, font = 'caveat', size = 20),
)
quizQ3.visible = False

#Question 4
quizQ4 = Group (
    Label('Question #4', 200, 50, fill = 'crimson', font = 'caveat', size = 36),
    Label("Where does most of the absorption take place?", 200, 115, fill = 'white', font = 'caveat', size = 20),
    ans4,
    Label("a. Small Intestine", 118, 180, font = 'caveat', size = 20),
    Label("b. Large Intestine", 288, 180, font = 'caveat', size = 20),
    Label("c. Stomach", 118, 260, font = 'caveat', size = 20),
    Label("d. Rectum", 288, 260, font = 'caveat', size = 20),
)
quizQ4.visible = False

#Question 5
quizQ5 = Group (
    Label('Question #5', 200, 50, fill = 'crimson', font = 'caveat', size = 36),
    Label("Where does the stool exit the digestive tract?", 200, 115, fill = 'white', font = 'caveat', size = 20),
    Label("a. Esophagus", 118, 180, font = 'caveat', size = 20),
    Label("b. Stomach", 288, 180, font = 'caveat', size = 20),
    ans5,
    Label("c. Rectum", 118, 260, font = 'caveat', size = 20),
    Label("d. Mouth", 288, 260, font = 'caveat', size = 20),
)

quizQ5.visible = False

###Screen 9 - Game

#Groups the components of the game instructions together
play = Oval(320, 340, 100, 50, fill = 'crimson')
gameInstructions = Group (
    Rect(0, 0, 400, 400, fill = 'papayaWhip'),
    play,
    Label("Play!", 320, 340, font = 'caveat', size = 28, fill = 'white'),
    Label("Keep the Enzyme within the Membrane!", 200, 50, font = 'caveat', size = 25),
    Line(20, 70, 380, 70, fill = 'crimson'),
    Label("Instructions:", 80, 100, font = 'caveat', size = 20),
    Label("This game can be played with one", 250, 100, font = 'caveat', size = 20, fill = 'crimson'),
    Label("or two players. The wad keys allow player 1 (the pink", 200, 120, font = 'caveat', size = 20, fill = 'crimson'),
    Label("block) to control their player. Player 2 (the crimson", 200, 140, font = 'caveat', size = 20, fill = 'crimson'),
    Label(" block) can direct their player using the up, right,", 200, 160, font = 'caveat', size = 20, fill = 'crimson'),
    Label("left arrow kets. The goal of this game is to keep the", 200, 180, font = 'caveat', size = 20, fill = 'crimson'),
    Label("ball (enzyme) within the membrane similar to how our", 200, 200, font = 'caveat', size = 20, fill = 'crimson'),
    Label("bodies do. If the enzyme falls to the gound on your", 200, 220, font = 'caveat', size = 20, fill = 'crimson'),
    Label("on your side, your opponent scores a point. The 1st", 200, 240, font = 'caveat', size = 20, fill = 'crimson'),
    Label("player to reach a score of 10 wins! Lets see", 200, 260, font = 'caveat', size = 20, fill = 'crimson'),
    Label("if you can handle the functions your", 200, 280, font = 'caveat', size = 20, fill = 'crimson'),
    Label("membrance preforms!", 200, 300, font = 'caveat', size = 20, fill = 'crimson'),
)
gameInstructions.visible = False

##Components of the game

#Membrane 1
membrane1 = Rect(50, 400, 75, 30 , fill = 'pink')
membrane1.dx = 0
membrane1.dy = 0
membrane1score = Label(0,100,50, size = 60, fill = 'black', font = 'caveat')

#Membrane 2
membrane2 = Rect(300, 400, 75, 30, fill = 'crimson')
membrane2.dx = 0
membrane2.dy = 0
membrane2score = Label(0, 300, 50, size = 60, fill = 'black', font = 'caveat')

#Ball
ball = Circle(200,200,10, fill = 'sandybrown')
ball.dx = 0
ball.dy = 0

#Membrane in the middle
membraneb = Line(200,400,200,300)

#Groups the components of the game together
gameBackground = Group(    
    Rect(0, 0, 400, 400, fill = 'papayaWhip'),
    membrane1score,
    membrane2score,
    ball,
    membraneb,
    membrane1, 
    membrane2
)
gameBackground.visible = False

#Groups the components of the winning screen together
gameCongrats = Group (
    Rect(0, 0, 400, 400, fill = 'crimson'),
    Rect(50, 125, 300, 55, fill = 'lightSalmon'),
    Label("Congratulations!", 200, 150, font = 'caveat', size = 40, fill = 'white'),
    Label('Wins!', 240, 210, font = 'caveat', size = 28, fill = 'white')
    )
gameCongrats.visible = False


##...................................................... ANIMATIONS ......................................................


##The onStep function is used to automatically move the food throughout 
##the digestive tract without any user interaction and to control 
##the movement of the enzyme during the game

def onStep():

    #Moves the food clumps down the esophagus
    if (foodClump.centerY < 400 and esophagus.visible == True and counter.visible == False):
        foodClump.centerY += 2
        if (foodClump.centerY >= 170):
            peristalsis.visible = True

    #Moves the food clumps in the stomach
    if (foodClump.centerY >= 400 and counter.visible == False):
        esophagus.visible = False
        peristalsis.visible = False
        stomach.visible = True
        ints2.visible = True
        foodClump.centerX = 195
        foodClump.centerY = -20
        foodClump.rotateAngle = -10
    if (foodClump.centerY < 260 and stomach.visible == True):
        foodClump.centerY += 1
    if (foodClump.centerY < 220 and stomach.visible == True):
        foodClump.centerX += 0.2
        foodClump.rotateAngle -= 0.1
    if (foodClump.hitsShape(acid) == True and stomach.visible == True and foodClump.centerY < 260):
        foodClump.rotateAngle -= 0.5

    #Informs the user about what happens in the stomach & the enzymes
    if (foodClump.centerY >= 260 and stomach.visible == True and counter.visible == False):
        stomachLabel1.visible = True
        stomachLabel2.visible = True
        ints2.visible = False
        foodClump.centerY = 260

    #Displays smaller food clumps and chyme after informing the user about the enzymes
    if (counter.visible == True and ints2.visible == True and chyme.centerX >= 110 and largeint.visible == False):
        foodClump.visible = False
        smallFoodClumps.visible = True
        chyme.visible = True
        chyme.centerX -= 1

    #Moves the chyme to the bottom of the stomach
    if(chyme.centerX <= 110 and largeint.visible == False):
        chyme.centerY += 1
        if (chyme.centerY >= 400):
            stomach.visible = False
            ints2.visible = False
            largeint.visible = True
            smallint.visible = True
            smallFoodClumps.visible = False
            intLabels.visible = True
            chyme.centerX = 99
            chyme.centerY = 11

    #Moves the chyme through the small intestine
    if (chyme.centerY <= 107 and smallint.visible == True):
        chyme.centerY += 1
        if (chyme.centerY >= 107 and chyme.centerX == 99 and smallint.visible == True):
            smallintLabel.visible = True

    #Moves the chyme through the large intestine 
    if (stool.visible == True and largeint.visible == True and stool.centerY >= 80 and stool.centerX == 60):
        stool.centerY -= 10
    if (stool.centerX <= 320 and stool.centerY <= 80 and stool.visible == True):
        stool.centerX += 5
    if (stool.centerX >= 320 and stool.centerY <= 310 and stool.visible == True):
        stool.centerY += 5
    if (stool.centerX <= 320 and stool.centerX >= 210 and stool.centerY >= 310 and stool.centerY <= 345 and stool.visible == True):
        stool.centerX -= 0.8
        stool.centerY += 0.25
    if (stool.centerY >= 344 and stool.centerY <= 400 and stool.visible == True):
        intLabels.visible = False
        largeint.centerY = -20
        smallint.centerY = 0 
        stool.centerY = 130

    #Moves the stool through the rectum
    if (stool.centerY >= 130 and stool.centerY <= 280 and largeint.centerY == -20):
        stool.centerY += 3
        rectumLabel.visible = True

    #Once the stool is released, the user is prompted to move to the quiz
    if (stool.centerY >= 280 and largeint.centerY == -20):
        quiz2.visible = True
        quiz2Label.visible = True

    #Creating the speed of the ball  
    ball.centerY += ball.dy
    ball.centerX += ball.dx

    #Getting the positions of the membranes (players)
    membrane1.centerX += membrane1.dx
    membrane1.centerY += membrane1.dy
    membrane2.centerX += membrane2.dx
    membrane2.centerY += membrane2.dy

    #Increasing the ball's speed in the y direction
    ball.dy += 0.5

    #Making sure Player 1 stays within the canvas    
    if(membrane1.bottom > 400 and gameBackground.visible == True):
        membrane1.dy = 0
        membrane1.bottom = 400

    #Making sure Player 2 stays within the canvas    
    if(membrane2.bottom > 400 and gameBackground.visible == True):
        membrane2.dy = 0
        membrane2.bottom = 400

    #Making sure the ball stays within the y components of the canvas and changes direction if it hits the ground    
    if (ball.bottom >= 400 and gameBackground.visible == True):
        ball.bottom = 400
        ball.dy = -ball.dy
        #Checking to see what side the ball hits the ground to add points to a specific player
        if(ball.centerX < 200):
            membrane2score.value += 1
        elif(ball.centerX > 200):
            membrane1score.value+=1

    #Making sure the ball stays within the y components of the canvas and changing speed if it hits the top
    if(ball.top <= 0 and gameBackground.visible == True):
        ball.top = 0
        ball.dy = ball.dy/2

    #Making sure the ball stays within the x components of the canvas and changes direction if it hits the two side walls 
    if(ball.left <= 0 and gameBackground.visible == True):
        ball.left = 0
        ball.dx = -ball.dx
    if(ball.right >= 400 and gameBackground.visible == True):
        ball.right = 400
        ball.dx = -ball.dx

    #Checks to see if a player hit the ball so that the ball can change direction
    if(ball.hitsShape(membrane1) and gameBackground.visible == True):
        ball.dx = -ball.dx
        ball.dy = -ball.dy
    if(ball.hitsShape(membrane2) and gameBackground.visible == True):
        ball.dx = -ball.dx
        ball.dy = -ball.dy

    #Checks to see which side the ball hit the middle membrane (net) if it did
    #If the ball hits net from the left side, it goes back to that side
    if(ball.hitsShape(membraneb) and gameBackground.visible == True):
        if(ball.centerX < 200):
            ball.dx = -5
            ball.dy = -5
        #If the ball hits net from the right side, it goes back to that side
        elif(ball.centerX > 200 and gameBackground.visible == True):
            ball.dx = 5
            ball.dy = -5
        #If the ball hits net in the middle, it goes back to a side picked at random
        else:
            #if a number <0.5 is chosen, the ball goes to the left side
            if(random() < 0.5 and gameBackground.visible == True):
                ball.dx = -5
                ball.dy = -5
            #if a number that isn't less than 0.5 is chosen, the ball goes to the right side
            else:
                ball.dx = 5
                ball.dy = -5

    #Checks to see if Player 1 gets a score of 10 so that the game finishes and Player 1 wins
    if (membrane1score.value == 10 and gameBackground.visible == True):
        gameCongrats.visible = True
        Label("Player 1", 160, 210, font = 'caveat', size = 28, fill = 'white')
        app.stop()
    #Checks to see if Player 2 gets a score of 10 so that the game finishes and Player 2 wins
    elif (membrane2score.value == 10 and gameBackground.visible == True):
        gameCongrats.visible = True
        Label("Player 2", 160, 210, font = 'caveat', size = 28, fill = 'white')  
        app.stop()

##The onKeyPress function is used to display the nutritional labels of various foods
##and to move the membranes in the game when the respective key is pressed

def onKeyPress(key):

    #Displays the nutritional labels of each food depending on the key the user presses
    if (key == 'p' and mouthScreen.visible == True):
        mouthScreen.visible = False
        pizzaint.visible = True
    elif (key == 's' and mouthScreen.visible == True):
        mouthScreen.visible = False
        salint.visible = True
    elif (key == 'i' and mouthScreen.visible == True):
        mouthScreen.visible = False
        iceint.visible = True

    #Allows the user to exit the nutritional labels when 'r' is pressed
    if (key == 'r' and (iceint.visible == True or pizzaint.visible == True or salint.visible == True)):
        iceint.visible = False
        pizzaint.visible = False
        salint.visible = False
        mouthScreen.visible = True

    #Controls the upward movements of the membranes in the game
    if(key == 'w' and gameBackground.visible == True):
        membrane1.dy = -2
    if(key == 'up'and gameBackground.visible == True):
        membrane2.dy = -2


##The onMousePress function is used to detect when and where the user
##clicks in order to preform various functions

def onMousePress(mouseX, mouseY):

    #If the user clicks on the begin button, the instructions will appear
    if (begin.contains(mouseX, mouseY) and begin.visible == True):
        startScreen.visible = False
        instructions.visible = True

    #If the user clicks on the start button, the customizations of the body will appear
    if (start.contains(mouseX, mouseY) and start.visible == True):
        instructions.visible = False
        customizations.visible = True

    #If the user clicks on the next button, the screen will move from the customizations to the mouth screen
    if (next.contains(mouseX, mouseY) and customizations.visible == True):
        customizations.visible = False
        mouthScreen.visible = True

    #If the user clicks on a specific block in the age category then that age is selected for the body
    if(b1.contains(mouseX,mouseY) == True and b1.visible == True and b2.fill != 'fireBrick' and b3.fill != 'fireBrick' and b4.fill != 'fireBrick' and b5.fill != 'fireBrick' and b15.fill != 'fireBrick'):
        b1.fill = 'fireBrick'
    elif(b2.contains(mouseX,mouseY) == True and b2.visible == True and b2.fill != 'fireBrick' and b3.fill != 'fireBrick' and b4.fill != 'fireBrick' and b5.fill != 'fireBrick' and b15.fill != 'fireBrick'):
        b2.fill = 'fireBrick'
    elif(b3.contains(mouseX,mouseY) == True and b3.visible == True and b2.fill != 'fireBrick' and b3.fill != 'fireBrick' and b4.fill != 'fireBrick' and b5.fill != 'fireBrick' and b15.fill != 'fireBrick'):
        b3.fill = 'fireBrick'
    elif(b4.contains(mouseX,mouseY) == True and b4.visible == True and b2.fill != 'fireBrick' and b3.fill != 'fireBrick' and b4.fill != 'fireBrick' and b5.fill != 'fireBrick' and b15.fill != 'fireBrick'):
        b4.fill = 'fireBrick'
    elif(b5.contains(mouseX,mouseY) == True and b5.visible == True and b2.fill != 'fireBrick' and b3.fill != 'fireBrick' and b4.fill != 'fireBrick' and b5.fill != 'fireBrick' and b15.fill != 'fireBrick'):
        b5.fill = 'fireBrick'

    #If the user clicks on a specific block in the height category then that height is selected for the body
    #Depending on the height clicked, the height of the body on screen changes
    if (b11.contains(mouseX, mouseY) == True and b11.visible == True and b11.fill != 'fireBrick' and b12.fill != 'fireBrick' and b13.fill != 'fireBrick' and b14.fill != 'fireBrick' and b15.fill != 'fireBrick'):
        body.height += 10
        b11.fill = 'fireBrick'
    elif (b12.contains(mouseX, mouseY) == True and b12.visible == True and b11.fill != 'fireBrick' and b12.fill != 'fireBrick' and b13.fill != 'fireBrick' and b14.fill != 'fireBrick' and b15.fill != 'fireBrick'):
        body.height += 20
        b12.fill = 'fireBrick'
    elif (b13.contains(mouseX, mouseY) == True and b13.visible == True and b11.fill != 'fireBrick' and b12.fill != 'fireBrick' and b13.fill != 'fireBrick' and b14.fill != 'fireBrick' and b15.fill != 'fireBrick'):
        body.height += 30
        b13.fill = 'fireBrick'
    elif (b14.contains(mouseX, mouseY) == True and b14.visible == True and b11.fill != 'fireBrick' and b12.fill != 'fireBrick' and b13.fill != 'fireBrick' and b14.fill != 'fireBrick' and b15.fill != 'fireBrick'):
        body.height += 40
        b14.fill = 'fireBrick'
    elif (b15.contains(mouseX, mouseY) == True and b15.visible == True and b11.fill != 'fireBrick' and b12.fill != 'fireBrick' and b13.fill != 'fireBrick' and b14.fill != 'fireBrick' and b15.fill != 'fireBrick'):
        body.height += 50
        b15.fill = 'fireBrick'

    #If the user clicks on a specific block in the weight category then that weight is selected for the body
    #Depending on the weight clicked, the weight of the body on screen changes
    if (b6.contains(mouseX, mouseY) == True and b6.visible == True and b6.fill != 'fireBrick' and b7.fill != 'fireBrick' and b8.fill != 'fireBrick' and b9.fill != 'fireBrick' and b10.fill != 'fireBrick'):
        body.width += 10
        b6.fill = 'fireBrick'
    elif (b7.contains(mouseX, mouseY) == True and b7.visible == True and b6.fill != 'fireBrick' and b7.fill != 'fireBrick' and b8.fill != 'fireBrick' and b9.fill != 'fireBrick' and b10.fill != 'fireBrick'):
        body.width += 20
        b7.fill = 'fireBrick'
    elif (b8.contains(mouseX, mouseY) == True and b8.visible == True and b6.fill != 'fireBrick' and b7.fill != 'fireBrick' and b8.fill != 'fireBrick' and b9.fill != 'fireBrick' and b10.fill != 'fireBrick'):
        body.width += 30
        b8.fill = 'fireBrick'
    elif (b9.contains(mouseX, mouseY) == True and b9.visible == True and b6.fill != 'fireBrick' and b7.fill != 'fireBrick' and b8.fill != 'fireBrick' and b9.fill != 'fireBrick' and b10.fill != 'fireBrick'):
        body.width += 40
        b9.fill = 'fireBrick'
    elif (b10.contains(mouseX, mouseY) == True and b10.visible == True and b6.fill != 'fireBrick' and b7.fill != 'fireBrick' and b8.fill != 'fireBrick' and b9.fill != 'fireBrick' and b10.fill != 'fireBrick'):
        body.width += 50
        b10.fill = 'fireBrick'

    #Displays the functions of the enzymes in the stomach if the respective button is pressed
    if (hereEnzStomach.contains(mouseX, mouseY) == True and stomach.visible == True and stomachLabel2.visible == True):
        stomach.visible = False
        ints2.visible = False
        foodClump.visible = False
        stomachLabel1.visible = False
        stomachLabel2.visible = False
        enzStomach.visible = True

    #Returns back to displaying the stomach when the user returns after viewing the ezymes of the stomach
    if (returnBox.contains(mouseX, mouseY) == True and enzStomach.visible == True):
        stomach.visible = True 
        ints2.visible = True
        foodClump.visible = True
        enzStomach.visible = False
        stomachLabel1.visible = False
        stomachLabel2.visible = False
        counter.visible = True

    #If the user clicks on the next button, the large intestine label will appear
    if (next2.contains(mouseX, mouseY) == True and smallintLabel.visible == True):
        smallintLabel.visible = False
        largeintLabel.visible = True

    #If the user clicks on the return button, the large intestine label will disappear
    #and the stool will be visible in the large intestine
    if (returnBox2.contains(mouseX, mouseY) == True and largeintLabel.visible == True):
        largeintLabel.visible = False
        chyme.visible = False
        stool.visible = True

    ##If the user clicks on either one of the quiz buttons, the quiz will appear
    ##If the user clicks on the correct answer, their score will increase by one and they will move onto the next question 
    ##If the user gets a question wrong, their score will remain the same and they will move onto the next question
    count = 0
    if ((quiz1.contains(mouseX, mouseY) and quiz1.visible == True) or (quiz2.contains(mouseX, mouseY) and quiz2.visible == True)):
        quizBackground.visible = True
        quizQ1.visible = True
    #Question 1
    elif (quizQ1.visible == True and ans1.contains(mouseX, mouseY) != True):
        quizQ1.visible = False
        quizQ2.visible = True
    elif (quizQ1.visible == True and ans1.contains(mouseX, mouseY) == True):
        score.value += 1
        quizQ1.visible = False
        quizQ2.visible = True
    #Question 2
    elif (quizQ2.visible == True and ans2.contains(mouseX, mouseY) != True):
        quizQ2.visible = False
        quizQ3.visible = True
    elif (quizQ2.visible == True and ans2.contains(mouseX, mouseY) == True):
        score.value += 1
        quizQ2.visible = False
        quizQ3.visible = True
     #Question 3       
    elif (quizQ3.visible == True and ans3.contains(mouseX, mouseY) != True):
        quizQ3.visible = False
        quizQ4.visible = True
    elif (quizQ3.visible == True and ans3.contains(mouseX, mouseY) == True):
        score.value += 1
        quizQ3.visible = False
        quizQ4.visible = True
     #Question 4   
    elif (quizQ4.visible == True and ans4.contains(mouseX, mouseY) != True):
        quizQ4.visible = False
        quizQ5.visible = True
    elif (quizQ4.visible == True and ans4.contains(mouseX, mouseY) == True):
        score.value += 1
        quizQ4.visible = False
        quizQ5.visible = True
     #Question 5 
    elif (quizQ5.visible == True and ans5.contains(mouseX, mouseY) != True):
        game2.visible = True
    elif (quizQ5.visible == True and ans5.contains(mouseX, mouseY) == True and game2.visible == False):
        score.value += 1
        game2.visible = True

    #If the user clicks on either of the game buttons, the game will appear
    if ((game1.visible == True and game1.contains(mouseX, mouseY) == True and instructions.visible == False) or (game2.visible == True and game2.contains(mouseX, mouseY) == True)):
        quizBackground.visible = False 
        quizQ5.visible = False
        gameInstructions.visible = True

    #If the user clicks on the play button, the game will start
    if (play.visible == True and play.contains(mouseX, mouseY)):
        gameInstructions.visible = False
        gameBackground.visible = True


##The onMouseDrag function is used to control the dragging of the food to the mouth
def onMouseDrag(mouseX, mouseY):

    #If the mouse's position is within the food, the food will move along as the mouse is dragged
    if (pizza.contains(mouseX, mouseY) == True and pizza.visible == True):
        pizza.centerX = mouseX
        pizza.centerY = mouseY
    elif (salad.contains(mouseX, mouseY) == True and salad.visible == True):
        salad.centerX = mouseX
        salad.centerY = mouseY
    elif (icecream.contains(mouseX, mouseY) == True and icecream.visible == True):
        icecream.centerX = mouseX
        icecream.centerY = mouseY


##The onMouseRelease function is used to detect when the foods are released into the mouth
def onMouseRelease(mouseX, mouseY):

    #If either one of the foods hits the mouth, the mouth screen will disapear 
    #and the next part of the digestive tract will appear
    if ((pizza.hitsShape(mouth) or salad.hitsShape(mouth) or icecream.hitsShape(mouth)) and mouth.visible == True):
        mouthScreen.visible = False
        esophagus.visible = True
        foodClump.visible = True

##The onKeyHold function is used to control the player's membrane in the game
def onKeyHold(keys):

    #If the specific keys are pressed while the game screen is active, Player 1 will move according to the user's directions
    if('d' in keys and membrane1.right<200 and gameBackground.visible == True):
        membrane1.dx = 3
    elif('a' in keys and membrane1.left>0) and gameBackground.visible == True:
        membrane1.dx = -3
    else:
        membrane1.dx = 0

    #If the specific keys are pressed while the game screen is active, Player 2 will move according to the user's directions
    if('right' in keys and membrane2.right<400 and gameBackground.visible == True):
        membrane2.dx = 3
    elif('left' in keys and membrane2.left>200 and gameBackground.visible == True):
        membrane2.dx = -3
    else:
        membrane2.dx = 0

##The onKeyRelease function is used to detect when the membranes (players) must fall back into their original position 
def onKeyRelease(key):

    #Once these keys are released the membrane falls back into its original position
    if((key == 'a' or key == 'd') and gameBackground.visible == True):
        membrane1.dx = 0
    elif((key == 'right' or key == 'left') and gameBackground.visible == True):
        membrane2.dx = 0
    elif(key == 'w'):
        membrane1.dy = 2
    elif(key == 'up'):
        membrane2.dy = 2



cmu_graphics.run()