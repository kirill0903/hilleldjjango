from django import forms

from task.models import Comment, Rating, Member


class CommentForm(forms.Form):
	text = forms.CharField(max_length=2000)
	choices = forms.ChoiceField(
		choices=[
			('issues', 'Issues'),
			('comment', 'Comment')
		]
	)


class CommentModelForm(forms.ModelForm):
	class Meta:
		model = Comment  # Название модели
		fields = ['text']  # Список полей  '__all__'


class RatingModelForm(forms.ModelForm):
	class Meta:
		model = Rating
		fields = '__all__'
		labels = {
			'point': 'Rate'
		}

class MemberModelForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = '__all__'