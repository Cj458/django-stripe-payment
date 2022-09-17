from django.contrib import admin
from django.urls import path
from products.views import (
    CreateCheckoutSessionView,
    ItemLandingPageView,
    SuccessView,
    CancelView,
    stripe_webhook,
    StripeIntentView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('item/<pk>', ItemLandingPageView.as_view(), name='landing-page'),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
