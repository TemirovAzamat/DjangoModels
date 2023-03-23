from oasis.models import *

user1 = User.objects.create(email='nikname21@gmail.com', password='defender42')
client = Client.objects.create(name='Азат Соколов', card_number=4147565798789009, user=user1)

user2 = User.objects.create(email='altywa1998@gmail.com', password='nono34')
worker = Worker.objects.create(name='Алтынай Алиева', position='Оператор кассы', user=user2)

food1 = Food.objects.create(name='Шаурма', start_price=50)
food2 = Food.objects.create(name='Гамбургер', start_price=25)

cheese = Ingredient.objects.create(name='Сыр', extra_price=10)
chicken = Ingredient.objects.create(name='Курица', extra_price=70)
beef = Ingredient.objects.create(name='Говядина', extra_price=80)
salad = Ingredient.objects.create(name='Салат', extra_price=15)
fries = Ingredient.objects.create(name='Фри', extra_price=15)
