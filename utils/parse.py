import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By


def parse_data(faculty: str, group_num: str) -> list:
    driver = webdriver.Edge()
    driver.get("https://ssau.ru/rasp")

    #open faculty page

    try:
        faculty_link = driver.find_element(By.LINK_TEXT, faculty).get_attribute("href")
    except:
        return "No such faculty"
    
    driver.get(faculty_link)

    #open course page

    nav_course_elem = driver.find_element(By.CLASS_NAME, "nav-course")
    courses = nav_course_elem.find_elements(By.TAG_NAME, "a")
    course_link = courses[int(group_num[1]) - 1].get_attribute("href")

    driver.get(course_link)

    #open group page

    try:
        group_link = driver.find_element(By.LINK_TEXT, group_num).get_attribute("href")
    except:
        return "No such group"

    driver.get(group_link)

    subjects = [x.text for x in driver.find_elements(By.CLASS_NAME, "schedule__item")]

    curr_day = datetime.datetime.today().weekday() + 1

    if curr_day == 0:
        return "it's weekend"
    
    today_subjects = subjects[curr_day::6]

    today_subjects = [x for x in today_subjects if x != ""]

    driver.close()
    driver.quit()

    return '\n'.join(today_subjects)

if __name__ == "__main__":
    print(parse_data("Институт информатики и кибернетики", "6312-100503D"))