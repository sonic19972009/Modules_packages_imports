from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
from PIL import Image

if __name__ == '__main__':
    print(datetime.datetime.now())

    calculate_salary()
    get_employees()

    with Image.open('images/netology.png') as img:
        img.show()
