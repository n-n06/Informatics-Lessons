class User:
    def __init__(self, id, name, job):
        self.id = id
        self.name = name
        self.job = job

    def change_job(self, new_job):
        self.job = new_job

    def print_job(self):
        print("my job is " + self.job)


a = User(1, "John", "SE")
b = User(2, "Adam", "Janitor")

a.change_job("teamlead")
a.print_job()

array = [1,2,3,4]
print(list(map(lambda x: 2 * x,array)))
