from .__init__ import db
from sqlalchemy_serializer import SerializerMixin

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)

    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')

    serialize_rules = ('-restaurant.restaurant_pizzas', '-pizza.restaurant_pizzas',)

    def __repr__(self):
        return f'<RestaurantPizza {self.id}: Price={self.price} for Restaurant ID {self.restaurant_id} and Pizza ID {self.pizza_id}>'

