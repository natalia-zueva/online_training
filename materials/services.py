import stripe
from config.settings import STRIPE_API_KEY
from users.models import Payment

stripe.api_key = STRIPE_API_KEY


def create_product(course):
    stripe_product = stripe.Product.create(
        name=course.title
    )
    return stripe_product['id']


def create_stripe_price(stripe_product_id, price_amount):
    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=int(price_amount)*100,
        product_data=stripe_product_id,
    )
    return stripe_price['id']


def create_stripe_session(stripe_price_id):
    stripe_session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{
            "price": stripe_price_id,
            "quantity": 1}],
        mode="payment",
    )

    return stripe_session['url'], stripe_session['id']
