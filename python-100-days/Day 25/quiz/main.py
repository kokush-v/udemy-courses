import turtle
import pandas

data = pandas.read_csv('50_states.csv')
data_len = len(data.index)

screen = turtle.Screen()
screen.title('Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
correct_answers = []
correct_answers_count = len(correct_answers)
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()



while correct_answers_count < data_len:
    user_input = screen.textinput(title=f'{correct_answers_count}/{data_len} States Correct',
                                  prompt="What's another state's name?")
    if user_input == 'exit':
        states_list = data["state"].to_list()
        for state in states_list:
            if state in correct_answers:
                states_list.remove(state)
        pandas.DataFrame(states_list).to_csv('missing_states.csv')
        break

    if user_input != "":
        try:
            guessed_state = data[data['state'] == user_input.title()]
            if guessed_state.empty:
                 raise Exception()
            else:
                guessed_state_name = guessed_state["state"].values[0]
                pen.setpos(x=int(guessed_state.x.iloc[0]), y=int(guessed_state.y.iloc[0]))
                pen.write(guessed_state_name, align='center', font=("Courier", 8, "bold"))
                correct_answers.append(guessed_state_name)
        except:
            print('This state doesnt exist')


screen.mainloop()