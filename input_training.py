import os.path

def input_training(train_list):
    # check if the file exists
    if not os.path.isfile("newtraining.txt"):
        return train_list
    else:
        with open("newtraining.txt", "r") as f:
            context = f.readlines()
            if len(context) == 0:
                return train_list
            else:
                index = 0
                del[train_list["q"]]
                while index < len(context):
                    train_program_ = context[index].strip()
                    train_list[index+5] = train_program_
                    index += 1
                train_list["q"] = "Quit"
                return train_list
