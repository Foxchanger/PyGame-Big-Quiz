import pgzrun
import pygame

WIDTH = 1280
HEIGHT = 720

score = 0
time_left = 10

q1 = [""]

def draw ():
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
        question =question.pop(0)
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
