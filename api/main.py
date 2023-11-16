"""
Utilizes Nobelz's api API to create a difficulty rating for a given UCI course based on RMP reviews.
"""
import requests
import api

SCHOOL = api.get_school_by_name("UC Irvine")

# For getting JSON responses for courses or instructors
def generate_response(input_type: str, input_id: str):
    url = f"https://api-next.peterportal.org/v1/rest/{input_type}/{input_id}"
    response = requests.get(url).json()
    return response


# Gives a list of names of instructors that have taught the course you want
def give_instructor_list(course_id):
    instructor_list = []
    instructor_history = generate_response("courses", course_id)["payload"]["instructorHistory"]
    for instructor_id in instructor_history:
        instructor_name = generate_response("instructors", instructor_id)["payload"]["name"]
        instructor_list.append(instructor_name)
    return instructor_list


def find_difficulty_average(course_entered: str):
    # User enters the course they want
    course_number = generate_response("courses", course_entered)["payload"]["courseNumber"]

    # Gets list of instructors that have taught that course
    course_instructors = give_instructor_list(course_entered)

    total_difficulty_sum = 0
    total_rating_count = 0

    # Print statement for debugging
    print(f"{len(course_instructors)} {course_entered} instructors found")

    # Iterates through instructors and looks them up on RMP
    for instructor in course_instructors:
        # Grabs instructor's last name
        instructor_name = instructor.split()[-1]
        professor = api.get_professor_by_school_and_name(SCHOOL, instructor_name)
        # If the instructor is on there
        if professor is not None:
            # Iterates through their ratings and if it's for the course the user wants, adds the difficulty to a sum
            difficulty_sum = 0
            rating_count = 0
            for rating in professor.get_ratings():
                if course_number in rating.class_name:
                    difficulty_sum += rating.difficulty
                    rating_count += 1

            # Print statements for debugging
            if rating_count:
                print(f"{instructor}'s difficulty rating for {course_entered} is {round(difficulty_sum/rating_count, 1)}")
            else:
                print(f"No information found for {instructor}")

            total_difficulty_sum += difficulty_sum
            total_rating_count += rating_count
            
    # Calculates the average difficulty rating of that course across instructors
    difficulty_average = None
    if total_rating_count != 0:
        difficulty_average = round(total_difficulty_sum/total_rating_count, 1)
    return difficulty_average

if __name__ == "__main__":
    user_course = "I&CSCI45C"
    # Print statements for debugging
    print("Loading...")
    difficulty_rating = find_difficulty_average(user_course)
    print(f"The difficulty rating of {user_course} is {difficulty_rating}")
    
