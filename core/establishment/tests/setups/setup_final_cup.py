from core.establishment.models import FinalCup, Ingredient, Recipient


def setUpFinalCup(self):
        self.ingredient1 = Ingredient.objects.create(
            name='Acai', portion='200', stock='500', price='12', unit='ml'
        )
        self.ingredient2 = Ingredient.objects.create(
            name='Morango', portion='3', stock='100', price='3', unit='un'
        )
        self.recipient = Recipient.objects.create(
            title='Medium recipient', quantity_ml='200', price='15', stock='100', content=self.ingredient1
        )
        self.final_cup = FinalCup.objects.create(
            name="CopoFeito", price="20.00", recipient=self.recipient
        )
        self.final_cup.ingredient.set([self.ingredient1, self.ingredient2])