from user import User
from post import Post

Alex = User("a@a.com", "Alex", "pwd1", "DevOps")

Alex.get_user_info()
Alex.change_job_title("Developer")
Alex.get_user_info()

Carl = User("b@b.com", "Carl", "pwd2", "QA Engineer")
Carl.get_user_info()

myself = Post("i want be a programmer", Alex.name)

myself.get_post_info()