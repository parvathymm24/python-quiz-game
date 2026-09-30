import unittest
from questions import question_SET,opt,correct_ans
from utils import see_score

class TestQuiz(unittest.TestCase):
    def testing_Q(self):
        self.assertGreater(len(question_SET),0)

def testing_QAlen(self):
    self.assertEqual(len(question_SET)), len(correct_ans)

def testing_opt(self):
    self.assertEqual(len(question_SET),len(opt))

def testing_SCORE_PERCENTAGE(self):
    score=4
    total=5
    percentage=int(score/total*100)

    self.assertEqual(percentage,80)

if __name__=="__main__":
    unittest.main()