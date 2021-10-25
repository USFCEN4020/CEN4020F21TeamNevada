import unittest
import mock
from job_class import Job
from account_class import Account
from job_apply import *
from job_deletion import *


class TestCases(unittest.TestCase):
    def test_view_job_true(self):
        test_jobs = [Job("john", "job1", "description", "employer", "$1000"),
                     Job(
                         "john", "job2", "description", "employer", "$1000")]
        test_user = Account('john', 'John123!', 'John', 'Doe')

        print("-----TEST OPTION '1' TRUE-----")
        with mock.patch('builtins.input', side_effect=["1", "job1", "q"]):
            apply_job(test_user, test_jobs)

    def test_view_job_false(self):
        test_jobs = [Job("john", "job1", "description", "employer", "$1000"),
                     Job(
                         "john", "job2", "description", "employer", "$1000")]
        test_user = Account('john', 'John123!', 'John', 'Doe')

        print("-----TEST OPTION '1' FALSE-----")
        with mock.patch('builtins.input', side_effect=["1", "job3", "q"]):
            apply_job(test_user, test_jobs)

    def test_apply_job_success(self):
        test_jobs = [Job("john", "job1", "description", "employer", "$1000"),
                     Job(
                         "john", "job2", "description", "employer", "$1000"),
                     Job("", "job3", "", "", ""), ]
        test_user = Account('john', 'John123!', 'John', 'Doe')
        f = open("job_application.json", 'r')
        list_json = json.loads(f.read())
        list_json = [item for item in list_json if
                     item["job_title"] == 'job3' and item[
                         "applicant"] == "john"]
        f.close()
        f = open("job_application.json", 'w')
        f.write(json.dumps(list_json))
        f.close()

        with mock.patch('builtins.input',
                        side_effect=['2', 'job3', "10/24/2021", "10/24/2021",
                                     "q"]):
            has_apply = False
            apply_job(test_user, test_jobs)
            with open("job_application.json", 'r') as f:
                list_json = json.loads(f.read())
                for item in list_json:
                    if item["job_title"] == 'job3' and item[
                        "applicant"] == "john":
                        has_apply = True
            assert has_apply

    def test_apply_job_unavailable(self):
        test_jobs = [Job("john", "job1", "description", "employer", "$1000"),
                     Job(
                         "john", "job2", "description", "employer", "$1000")]
        test_user = Account('john', 'John123!', 'John', 'Doe')

        with mock.patch('builtins.input', side_effect=['2', 'job4', "q"]):
            has_apply = False
            apply_job(test_user, test_jobs)
            with open("job_application.json", 'r') as f:
                list_json = json.loads(f.read())
                for item in list_json:
                    if item["job_title"] == 'job4':
                        has_apply = True
            assert not has_apply

    def test_apply_job_posted(self):
        test_jobs = [Job("john", "job1", "description", "employer", "$1000"),
                     Job(
                         "john", "job2", "description", "employer", "$1000")]
        test_user = Account('john', 'John123!', 'John', 'Doe')
        f = open("job_application.json", 'r')
        list_json = json.loads(f.read())
        list_json = [item for item in list_json if
                     not (item["job_title"] == 'job2' and item[
                         "applicant"] == "john")]
        f.close()
        f = open("job_application.json", 'w')
        f.write(json.dumps(list_json))
        f.close()

        with mock.patch('builtins.input', side_effect=['2', 'job2', "q"]):
            has_apply = False
            apply_job(test_user, test_jobs)
            with open("job_application.json", 'r') as f:
                list_json = json.loads(f.read())
                for item in list_json:
                    if item["job_title"] == 'job2' and item[
                        "applicant"] == "john":
                        has_apply = True
            assert not has_apply

    def test_apply_job_saved(self):
        test_jobs = [Job("john", "job1", "description", "employer", "$1000"),
                     Job(
                         "john", "job2", "description", "employer", "$1000")]
        test_user = Account('john', 'John123!', 'John', 'Doe')
        f = open("jobs_saved.json", 'r')
        list_json = json.loads(f.read())
        list_json = [item for item in list_json if
                     not (item["job_title"] == 'job1' and item[
                         "user"] == "john")]
        f.close()
        f = open("jobs_saved.json", 'w')
        f.write(json.dumps(list_json))
        f.close()

        with mock.patch('builtins.input', side_effect=['3', 'job1', "q"]):
            has_saved = False
            apply_job(test_user, test_jobs)
            with open("jobs_saved.json", 'r') as f:
                list_json = json.loads(f.read())
                for item in list_json:
                    if item["job_title"] == 'job1' and item["user"] == "john":
                        has_saved = True
            assert has_saved

    def test_apply_job_unsaved(self):
        test_jobs = [Job("john", "job1", "description", "employer", "$1000"),
                     Job(
                         "john", "job2", "description", "employer", "$1000")]
        test_user = Account('john', 'John123!', 'John', 'Doe')
        f = open("jobs_saved.json", 'r')
        list_json = json.loads(f.read())
        list_json = [item for item in list_json if
                     item["job_title"] == 'job1' and item["user"] == "john"]
        assert len(list_json) != 0
        f.close()

        with mock.patch('builtins.input', side_effect=['4', "1", 'job1', "q"]):
            has_saved = False
            apply_job(test_user, test_jobs)
            with open("jobs_saved.json", 'r') as f:
                list_json = json.loads(f.read())
                for item in list_json:
                    if item["job_title"] == 'job1' and item["user"] == "john":
                        has_saved = True
            assert not has_saved

    def test_apply_job_view_saved(self):
        test_jobs = [Job("john", "job1", "description", "employer", "$1000"),
                     Job(
                         "john", "job2", "description", "employer", "$1000")]
        test_user = Account('john', 'John123!', 'John', 'Doe')

        with mock.patch('builtins.input', side_effect=['4', "q"]):
            apply_job(test_user, test_jobs)

    def test_delete_job(self):
        test_jobs = [Job("john", "job1", "description", "employer", "$1000"),
                     Job("mark", "job2", "description", "employer", "$1000")]
        test_user = Account('john', 'John123!', 'John', 'Doe')
        accounts = [Account('john', 'John123!', 'John', 'Doe'),
                    Account('mark', 'Mark123!', 'mark', 'Smith')]

        # prepare jobs
        with open("./jobs.txt", "w") as f:
            job = ",".join(["john", "job1", "description", "employer", "$1000"])
            job2 = ",".join(["mark", "job2", "description", "employer", "$1000"])
            f.write(job + "\n" + job2)

        with open("./job_application.json", "w") as f:
            application = [
                {"job_title": "job1", "applicant": "mark",
                 "grad_date": "10/24/2021", "start_date": "10/24/2021"},
                {"job_title": "job2", "applicant": "john",
                 "grad_date": "10/24/2021", "start_date": "10/24/2021"}
            ]
            f.write(json.dumps(application))

        with mock.patch('builtins.input', side_effect=['1', 'job1', "q"]):
            has_job = False
            delete_job(test_user, test_jobs)
            with open("jobs.txt", 'r') as f:
                list_json = f.readlines()
                for line in list_json:
                    item = line.split(",")
                    if item[1] == 'job1' and item[0] == "john":
                        has_job = True
            assert not has_job

    def test_delete_others_job(self):
        test_jobs = [Job("john", "job1", "description", "employer", "$1000"),
                     Job("mark", "job2", "description", "employer", "$1000")]
        test_user = Account('john', 'John123!', 'John', 'Doe')
        accounts = [Account('john', 'John123!', 'John', 'Doe'),
                    Account('mark', 'Mark123!', 'mark', 'Smith')]

        # prepare jobs
        with open("./jobs.txt", "w") as f:
            job = ",".join(["john", "job1", "description", "employer", "$1000"])
            job2 = ",".join(["mark", "job2", "description", "employer", "$1000"])
            f.write(job + "\n" + job2)

        with open("./job_application.json", "w") as f:
            application = [
                {"job_title": "job1", "applicant": "mark",
                 "grad_date": "10/24/2021", "start_date": "10/24/2021"},
                {"job_title": "job2", "applicant": "john",
                 "grad_date": "10/24/2021", "start_date": "10/24/2021"}
            ]
            f.write(json.dumps(application))

        with mock.patch('builtins.input', side_effect=['1', 'job2', "q"]):
            has_job = False
            delete_job(test_user, test_jobs)
            with open("jobs.txt", 'r') as f:
                list_json = f.readlines()
                for line in list_json:
                    item = line.split(",")
                    if item[1] == 'job2' and item[0] == "mark":
                        has_job = True
            assert has_job

    def test_delete_job_application(self):
        test_jobs = [Job("john", "job1", "description", "employer", "$1000"),
                     Job("mark", "job2", "description", "employer", "$1000")]
        test_user = Account('john', 'John123!', 'John', 'Doe')
        accounts = [Account('john', 'John123!', 'John', 'Doe'),
                    Account('mark', 'Mark123!', 'mark', 'Smith')]

        # prepare jobs
        with open("./jobs.txt", "w") as f:
            job = ",".join(["john", "job1", "description", "employer", "$1000"])
            job2 = ",".join(["mark", "job2", "description", "employer", "$1000"])
            f.write(job + "\n" + job2)

        with open("./job_application.json", "w") as f:
            application = [
                {"job_title": "job1", "applicant": "mark",
                 "grad_date": "10/24/2021", "start_date": "10/24/2021"},
                {"job_title": "job2", "applicant": "john",
                 "grad_date": "10/24/2021", "start_date": "10/24/2021"}
            ]
            f.write(json.dumps(application))

        with mock.patch('builtins.input', side_effect=['1', 'job1', "q"]):
            has_application = False
            delete_job(test_user, test_jobs)
            with open("./job_application.json", 'r') as f:
                list_json = json.loads(f.read())
                for item in list_json:
                    if item["job_title"] == 'job1':
                        has_application = True
            assert not has_application

if __name__ == '__main__':
    unittest.main()
