from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
	OPEN_STATUS = 'open'
	TASK_STATUSES = (
		(OPEN_STATUS, 'Open'),
		('in_progress', 'In progress'),
		('done', 'Done'),
	)

	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=40)  # Текстовое поле
	description = models.TextField()  # Текстовое поле
	status = models.CharField(
		max_length=20,
		choices=TASK_STATUSES,
		default=OPEN_STATUS,
	)  # Текстовое поле с возможность выбора
	updated_at = models.DateTimeField(auto_now=True)  # Дата и время которая задается автоматически при изменении записи
	created_at = models.DateTimeField(auto_now_add=True)  # Дата и время которая задается автоматически при создании записи

	def __str__(self):
		return f'{self.id} {self.title}'


class Rating(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	task = models.OneToOneField(Task, on_delete=models.CASCADE)
	id = models.AutoField(primary_key=True)
	point = models.CharField(max_length=20, choices=(
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5')
	))
	created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
	id = models.AutoField(primary_key=True)
	text = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)


class Member(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=40)
	phone = models.IntegerField()
	email = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
