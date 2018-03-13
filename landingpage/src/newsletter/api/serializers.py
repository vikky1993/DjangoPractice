# from rest_framework import serializers

# from newsletter.models import Join 

# class JoinSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Join
# 		field = ['email']

# 	def validate_email(self, value):
# 		email = value
# 		qs = Join.objects.filter(email__iexact=email)
# 		if qs.exists():
# 			print('exists')
# 			raise serializers.ValidationError("This email already exists")
# 		return email