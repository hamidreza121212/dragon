
def while_true(status: bool):

    while status:
        action = int(input('inter : '))

        if action == 5:
            break

    question = (input('want play : '))

    if question == 'y':
        while_true(True)
    else:
        print('good bay')


