from core.establishment.models import FinalCup, Ingredient, Recipient


def setUpFinalCup(self):
        self.ingredient1 = Ingredient.objects.create(
            name='Ingredient 1', portion='200', price='12', unit_of_measure='ml'
        )
        self.ingredient2 = Ingredient.objects.create(
            name='Ingredient 2', portion='3', price='3', unit_of_measure='un'
        )
        self.recipient = Recipient.objects.create(
            title='Medium recipient', quantity_ml='200', price='15', stock=0, content=self.ingredient1
        )
        self.final_cup = FinalCup.objects.create(
            name="CopoFeito", price="20.00", recipient=self.recipient
        )
        self.final_cup.ingredient.set([self.ingredient1, self.ingredient2])
        # create an initial Stock record used by stock tests
        from core.establishment.models import Stock

        self.stock = Stock.objects.create(
            ingredient=self.ingredient1,
            quantity=10,
            batch="InitBatch",
            expiration_date="2025-01-01",
            supplier="Init Supplier",
            batch_price="50.00",
            unit_of_measure="grams",
        )
    # end of setup for final cup