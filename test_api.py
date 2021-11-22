from main import *
import unittest
import mock

from test_main import *

class TestApi(unittest.TestCase):
    def test_output_api(self):
        # create some accounts - code taken from test_main test_main_screen()
        test_accounts = [Account('john', 'John123!', 'John', 'Doe'),
                    Account('mark', 'Mark123!', 'Mark', 'Smith')]
        with mock.patch('builtins.input', side_effect=['3', 'John', 'Doe', 's', 'sally', 'Hill123!', 'Sally', 'Hill', "1", 'sally', 'Hill123!', 'q']):
            main_screen(test_accounts)

        # create a profile for john - code taken from test_main test_profile_creation()
        test_account = Account('john', 'John123!', 'John', 'Doe')

        with mock.patch('builtins.input',
                        side_effect=['test title', 'test major', 'test university', 'test about',
                                     'y', 'test job title', 'test employer', 'test start date',
                                     'test end date', 'test location', 'test job description', 'n',
                                     'test school name', 'test degree', '5 years', 'n']):
            profile_creation(test_account)

        # add training courses for john - code taken from test_main test_learning_ui()
        with mock.patch('builtins.input', side_effect=['1', 'y', 'q']):
            learning_ui(test_account)

        # add job to jobs.csv and output file
        with open("./jobs.txt", "w") as f:
            job = ",".join(["john", "job1", "description", "employer", "$1000", "location"])
            f.write(job)
        output_api_jobs()

        # open job_applications.json and add job application for john
        with open("job_application.json", "w") as f:
            application = [{
                "job_title": "job1", "applicant": "john", "grad_date": "10/24/2021", "start_date": "10/24/2021", "reason": "some reason", "application_date": "2021-11-19"
            }]
            json.dump(application, f)
        
        # output job applications
        output_api_applied_jobs()     

        

        