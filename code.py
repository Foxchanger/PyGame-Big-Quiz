import pgzrun
import pygame

WIDTH = 1280
HEIGHT = 720

score = 0
time_left = 10

q1 = ["Qual valor da soma 1+1?",
"5","1","2","4",3 ]

q2 = ["Qual é a letra que antecede a letra O no alfabeto brasileiro?",
"N.","M","S","T",1 ]

q3 = ["A qual banda de rock que o cantor britânico Fred Mercury pertenceu?",
"Led Zeppelin","AC/DC","Guns N' Roses","Queen",4 ]

q4 = ["Qual cidade brasileira é conhecida como a terra da garoa?",
"Rio de Janeiro","Curitiba","Amazonas","São Paulo",4 ]

q5 = ["Quantos segundos há em duas horas?",
"2800","7200","6900","3600",1 ]

question = [q1,q2,q3,q4,q5]
question = question.pop(0)

main_box = Rect(0, 0, 820, 240) 
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50,40)
answer_box1.move_ip(50,358)
answer_box2.move_ip(735,358)
answer_box3.move_ip(50,538)
answer_box4.move_ip(735,538)
answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]

def draw ():
    screen.fill("dim grey")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")

    screen.draw.textbox(str(time_left),timer_box, color=("black"))
    screen.draw.textbox(question[0], main_box, color=("black)"))

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index],box, color = ("black"))
        index = index +1 

def game_over():
    global question, score, time_left
    message = "Game Over. You got %s question correct" % str(score)
    question = [message, "-","-","-","-",5]
    time_left = 0

def correct_answer():
    global question, score , time_left    

    score = score + 1
    if question:
        question = question.pop(0)
        time_left = 10
    else:
        print("End of question")
        game_over()

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer" + str(index))
            if index == question[5]:
                print("You got it correct!")
                correct_answer()

def update_time_left():
    global time_left

    if time_left:
        time_left = time_left - 1
    else:
        game_over()
clock.schedule_interval(update_time_left,1.0) 
pgzrun.go()