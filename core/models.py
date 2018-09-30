
from django.db import models

# Create your models here.
class JAVATEST(models.Model):
	QUESTION_NO=models.IntegerField(default=0)
	QUESTION=models.CharField(max_length=300)
	OPTION1=models.CharField(max_length=300)
	OPTION2=models.CharField(max_length=300)
	OPTION3=models.CharField(max_length=300)
	OPTION4=models.CharField(max_length=300)
	ANSWER=models.IntegerField(default=0)

	def __str__(self):
		return str(self.QUESTION_NO)+" "+self.QUESTION+" "+self.OPTION1+" "+self.OPTION2+" "+self.OPTION3+" "+self.OPTION4+" "+str(self.ANSWER)

class CSTEST(models.Model):
	QUESTION_NO=models.IntegerField(default=0)
	QUESTION=models.CharField(max_length=300)
	OPTION1=models.CharField(max_length=300)
	OPTION2=models.CharField(max_length=300)
	OPTION3=models.CharField(max_length=300)
	OPTION4=models.CharField(max_length=300)
	ANSWER=models.IntegerField(default=0)

	def __str__(self):
		return str(self.QUESTION_NO)+" "+self.QUESTION+" "+self.OPTION1+" "+self.OPTION2+" "+self.OPTION3+" "+self.OPTION4+" "+str(self.ANSWER)

class CTEST(models.Model):
	QUESTION_NO=models.IntegerField(default=0)
	QUESTION=models.CharField(max_length=300)
	OPTION1=models.CharField(max_length=300)
	OPTION2=models.CharField(max_length=300)
	OPTION3=models.CharField(max_length=300)
	OPTION4=models.CharField(max_length=300)
	ANSWER=models.IntegerField(default=0)

	def __str__(self):
		return str(self.QUESTION_NO)+" "+self.QUESTION+" "+self.OPTION1+" "+self.OPTION2+" "+self.OPTION3+" "+self.OPTION4+" "+str(self.ANSWER)

class CPPTEST(models.Model):
	QUESTION_NO=models.IntegerField(default=0)
	QUESTION=models.CharField(max_length=300)
	OPTION1=models.CharField(max_length=300)
	OPTION2=models.CharField(max_length=300)
	OPTION3=models.CharField(max_length=300)
	OPTION4=models.CharField(max_length=300)
	ANSWER=models.IntegerField(default=0)

	def __str__(self):
		return str(self.QUESTION_NO)+" "+self.QUESTION+" "+self.OPTION1+" "+self.OPTION2+" "+self.OPTION3+" "+self.OPTION4+" "+str(self.ANSWER)



class PYTHONTEST(models.Model):
	QUESTION_NO=models.IntegerField(default=0)
	QUESTION=models.CharField(max_length=300)
	OPTION1=models.CharField(max_length=300)
	OPTION2=models.CharField(max_length=300)
	OPTION3=models.CharField(max_length=300)
	OPTION4=models.CharField(max_length=300)
	ANSWER=models.IntegerField(default=0)

	def __str__(self):
		return str(self.QUESTION_NO)+" "+self.QUESTION+" "+self.OPTION1+" "+self.OPTION2+" "+self.OPTION3+" "+self.OPTION4+" "+str(self.ANSWER)


class result(models.Model):
	sid=models.CharField(max_length=30)
	marks=models.IntegerField(default=0)
	subject=models.CharField(max_length=30)
	tdate=models.CharField(max_length=30)

	def __str__(self):
		return self.sid+" "+str(self.marks)+" "+self.subject+" "+self.tdate