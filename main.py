def spacing_frames():
    works = int(input("How frames would you like to hang on your wall?"))
    width_of_works = int(
        input("In inches, what is the width of all the frames combined?"))
    width_of_wall = int(
        input(
            "In inches, what is the width of the wall which will house your frames?"
        ))
    calculations = (width_of_works - width_of_wall) / (works + 1) * -1
    rounded_calc = round(calculations, 2)

    print(
        "Okay, you want to hang {} different works, whose combined width is {} inches, on a wall of whose width spans {} inches. ".
        format(works, width_of_works, width_of_wall) +
        "Since there will be {} spaces along your wall, if you measure {:0.2} inches between each wall and frame, your frames will span the width of the wall evenly.".
        format(works + 1, rounded_calc))


spacing_frames()


