from django.db import models
import uuid
import random

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = True)
    #UUID là chuỗi 128 bit để định danh duy nhất mỗi câu hỏi trong hệ thống
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    # lưu trữ thời gian tạo và cập nhật của mỗi câu hỏi, theo dõi lịch sử
    # thay đổi của dữ liệu

    
    class Meta:
        abstract = True
        
class Types(BaseModel): #quản lý các loại type của câu hỏi
    gfg_name = models.CharField(max_length=100)
    #lưu trữ tên các loại câu hỏi
    def __str__(self) -> str: #trả về tên loại câu hỏi
        return self.gfg_name
#Type có quan hệ 1 chiều với lớp Question, 1 loại câu hỏi có thể liên kết với nhiều câu hỏi
    
class Question(BaseModel):
    gfg = models.ForeignKey(Types, related_name='gfg',on_delete= models.CASCADE)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default = 5)
    
    def __str__(self) -> str:
        return self.question
    
    def get_answers(self):
        answer_objs =  list(Answer.objects.filter(question= self))
        data = []
        random.shuffle(answer_objs)
        
        for  answer_obj in answer_objs:
            data.append({
                'answer' :answer_obj.answer, 
                'is_correct' : answer_obj.is_correct
            })
        return data
    
class Answer(BaseModel):
    question = models.ForeignKey(Question,related_name='question_answer',  on_delete =models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.answer 
    
