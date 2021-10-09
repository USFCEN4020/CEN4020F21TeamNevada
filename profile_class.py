import json


class Profile:
    def __init__(self, username=None, title=None, major=None, university=None, about=None, jobs=None, education=None):
        self.username = username
        self.title = title
        self.major = major
        self.university = university
        self.about = about
        self.jobs = jobs
        self.education = education

    def get_profile_list(self):
        with open("profiles.json", "r") as f:
            content = json.loads(f.read())
        return content

    def get_profile_info(self, username):
        content = self.get_profile_list()
        for profile in content:
            if username == profile['username']:
                return profile
        return None

    def write_profile_info(self):
        content = self.get_profile_list()
        pro_count = -1
        for i, profile in enumerate(content):
            if self.username == profile['username']:
                pro_count = i
                break
        if pro_count == -1:
            new_profile = {
                    "username": self.username,
                    "title": self.title,
                    "major": self.major,
                    "university": self.university,
                    "about": self.about,
                    "jobs": self.jobs,
                    "education": self.education
                }
            content.append(new_profile)
            with open("profiles.json", 'w') as f:
                json.dump(content, f)
        else:
            e_profile = content[pro_count]
            e_profile['title'] = self.title
            e_profile['major'] = self.major
            e_profile['university'] = self.university
            e_profile['about'] = self.about
            e_profile['jobs'] = self.jobs
            e_profile['education'] = self.education
            with open("profiles.json", "w") as f:
                f.write(json.dumps(content))

