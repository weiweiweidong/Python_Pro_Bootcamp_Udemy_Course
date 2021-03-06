class QuizBrain:

    # 初始化， 传入 q_list 问题列表
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    # 判断是否还有剩余问题，返回 True 或 False
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    #
    def next_question(self):
        # 提取当前题号的问题
        current_question = self.question_list[self.question_number]
        # 题号+1
        self.question_number += 1
        # 检测用户输入
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # 调用函数，检测答案是否正确
        self.check_answer(user_answer, current_question.answer)

    # 检测答案是否正确
    # 输入：用户答案，正确答案
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
