class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = str(age)
        self.tracks = str(tracks)
        self.score = str(score)
    
    def change_name(self, new_name):
        self.name = str(new_name)

    def change_age(self, new_age):
        self.age = str(new_age)

    def change_track(self, new_track):
        self.track = str(new_track)

    def get_score(self):
        return self.score
        

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
