import json
# When they select this option, they will be presented with a list of courses that they can take. This list will 
# include "How to use In College learning", "Train the trainer", and "Gamification of learning".  
# Additionally, "Understanding the Architectural Design Process" and "Project Management Simplified" 
# will be displayed. 

def learning_ui(user):
    # read the contents of the courses_taken.json file
    with open('courses_taken.json') as json_file:
        courses_taken = json.loads(json_file.read())

    # loop through the contents of the courese taken file and print out the courses that the user has taken
    user_courses = []
    for courses in courses_taken:
        if courses['user'] == user.username:
            user_courses = courses['courses']
            print(user_courses)

    # user input loop for learning courses
    while True:
        # print the learning courses options
        print("\n ********* InCollege Learning Courses ********* \n")

        menu_opt = {
            "1": "How to use InCollege learning",
            "2": "Train the trainer",
            "3": "Gamification of learning",
            "4": "Understanding the Architectural Design Process",
            "5": "Project Management Simplified",
            "q": "Quit"
        }

        for key, value in menu_opt.items():
            # if the user has taken the course, print Completed next to a course they have taken
            if value in user_courses:
                print(key, ")", value, "-- Completed")
            else:
                print(key, ")", value)

        # user input for learning courses
        user_input = input("\nPlease select a course you would like to take: ")

        # if the users selects a course, and they have not taken it, print "You have now completed this training"
        # if the user selects q, quit the program
        if user_input == "1":
            if "How to use InCollege learning" not in user_courses:
                # add the course to the user's courses taken
                add_course(user, user_courses, "How to use InCollege learning")
            else:
                retake_course()
        elif user_input == "2":
            if "Train the trainer" not in user_courses:
                # add the course to the user's courses taken
                add_course(user, user_courses, "Train the trainer")
            else:
                retake_course()
        elif user_input == "3":
            if "Gamification of learning" not in user_courses:
                # add the course to the user's courses taken
                add_course(user, user_courses, "Gamification of learning")
            else:
                retake_course()
        elif user_input == "4":
            if "Understanding the Architectural Design Process" not in user_courses:
                # add the course to the user's courses taken
                add_course(user, user_courses, "Understanding the Architectural Design Process")
            else:
                retake_course()
        elif user_input == "5":
            if "Project Management Simplified" not in user_courses:
                # add the course to the user's courses taken
                add_course(user, user_courses, "Project Management Simplified")
            else:
                retake_course()
        elif user_input == "q":
            break
        else:
            print("Unknown Selection, Try Again!")

# function to add a user course taken to the courses_taken.json file
def add_course(user, user_courses, course):
    print(user.username)
    print(course)

    # print the user has not taken the courses
    print("\nYou have now completed this training")
    user_courses.append(course)

    # read the contents of the courses_taken.json file
    with open('courses_taken.json') as json_file:
        courses_taken = json.loads(json_file.read())

    # if the user does not exit in the courese_taken list, add the user to the file
    in_file = False # keep track if the user is in the file
    for i, courses in enumerate(courses_taken):
        if courses['user'] == user.username:
            in_file = True

            # append the course to the user's courses taken
            courses_taken[i]['courses'].append(course)

            # write the new courses_taken list to the courses_taken.json file
            with open('courses_taken.json', 'w') as outfile:
                json.dump(courses_taken, outfile)
            
            return

    # if the user is not in the file, add the user to the file
    if in_file == False:
        print("User not in file")
        courses_taken.append({
            "user": user.username,
            "courses": [course]
        })

        # write the new courses_taken list to the courses_taken.json file
        with open('courses_taken.json', 'w') as outfile:
            json.dump(courses_taken, outfile)

# If a student selects to take a course again that they have already taken, the application will ask them 
# "You have already taken this course, do you want to take it again?" If the student says yes, then the 
# notice "You have now completed this training" will be displayed. Otherwise "Course Cancelled" will be 
# displayed and the student will be taken back to the list of courses. 
def retake_course():
    print("You have already taken this course, do you want to take it again (Y/N)?")
    user_input = input("")

    if user_input == "Y" or user_input == "y":
        print("\nYou have now completed this training")
    else:
        print("\nCourse Cancelled")
    